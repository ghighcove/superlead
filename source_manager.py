#!/usr/bin/env python3
"""
Source Integration System for Autonomous Projectile Guidance Research
Manages incorporation of external research sources into documentation
"""

import os
import json
import yaml
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import re
import logging

class SourceManager:
    """Manages research sources and their integration into documentation"""
    
    def __init__(self, config_file: str = "config.yaml"):
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.setup_logging()
        self.setup_directories()
        self.source_db = self.load_source_database()
        
    def setup_logging(self):
        """Configure logging system"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('source_integration.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def setup_directories(self):
        """Ensure all required directories exist"""
        for dir_path in [
            self.config['INPUT_DIR'],
            self.config['DOCS_DIR'],
            self.config['SOURCES_DIR'],
            self.config['ASSETS_DIR'],
            f"{self.config['INPUT_DIR']}/papers",
            f"{self.config['INPUT_DIR']}/briefings",
            f"{self.config['INPUT_DIR']}/data",
            f"{self.config['INPUT_DIR']}/references"
        ]:
            os.makedirs(dir_path, exist_ok=True)
    
    def load_source_database(self) -> Dict:
        """Load or create the source tracking database"""
        db_path = "source_database.json"
        if os.path.exists(db_path):
            with open(db_path, 'r') as f:
                return json.load(f)
        return {"sources": {}, "last_update": None}
    
    def save_source_database(self):
        """Save the source tracking database"""
        with open("source_database.json", 'w') as f:
            json.dump(self.source_db, f, indent=2)
    
    def scan_input_directory(self) -> List[Dict]:
        """Scan input directory for new or updated sources"""
        new_sources = []
        input_dir = Path(self.config['INPUT_DIR'])
        
        for category_dir in input_dir.iterdir():
            if not category_dir.is_dir():
                continue
                
            category = category_dir.name
            if category not in ['papers', 'briefings', 'data', 'references']:
                continue
            
            for file_path in category_dir.glob('*'):
                if file_path.is_file() and self._is_supported_format(file_path, category):
                    source_info = self._process_file(file_path, category)
                    if source_info:
                        new_sources.append(source_info)
        
        return new_sources
    
    def _is_supported_format(self, file_path: Path, category: str) -> bool:
        """Check if file format is supported for the category"""
        supported = self.config['SUPPORTED_FORMATS'].get(category, [])
        return file_path.suffix.lower() in supported
    
    def _process_file(self, file_path: Path, category: str) -> Optional[Dict]:
        """Process a single source file and extract metadata"""
        try:
            file_hash = self._calculate_file_hash(file_path)
            cwd = Path.cwd().resolve()
            try:
                relative_path = str(file_path.relative_to(cwd))
            except ValueError:
                # If file is not under cwd, use absolute path
                relative_path = str(file_path)
            
            # Check if file already exists
            if relative_path in self.source_db['sources']:
                existing_hash = self.source_db['sources'][relative_path].get('hash')
                if existing_hash == file_hash:
                    return None  # File unchanged
            
            source_info = {
                'file_path': relative_path,
                'category': category,
                'hash': file_hash,
                'added_date': datetime.now().isoformat(),
                'status': 'new'
            }
            
            # Extract content based on file type
            if category == 'briefings' and file_path.suffix == '.md':
                content = self._extract_markdown_content(file_path)
                source_info.update(content)
            elif category == 'data' and file_path.suffix in ['.json', '.yaml', '.yml']:
                content = self._extract_structured_data(file_path)
                source_info.update(content)
            elif category == 'papers' and file_path.suffix == '.txt':
                content = self._extract_text_content(file_path)
                source_info.update(content)
            
            # Update database
            self.source_db['sources'][relative_path] = source_info
            
            return source_info
            
        except Exception as e:
            self.logger.error(f"Error processing {file_path}: {e}")
            return None
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of file"""
        hash_sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
    def _extract_markdown_content(self, file_path: Path) -> Dict:
        """Extract content from markdown briefing files"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract front matter
        front_matter = {}
        if content.startswith('---'):
            try:
                end_index = content.find('---', 3)
                if end_index != -1:
                    yaml_content = content[3:end_index].strip()
                    front_matter = yaml.safe_load(yaml_content)
                    content = content[end_index + 3:].strip()
            except:
                pass
        
        # Extract sections
        sections = {}
        for match in re.finditer(r'^#+ (.+)$\n(.*?)(?=\n# |$)', content, re.MULTILINE | re.DOTALL):
            section_title = match.group(1).strip()
            section_content = match.group(2).strip()
            sections[section_title.lower().replace(' ', '_')] = section_content
        
        return {
            'title': front_matter.get('title', file_path.stem),
            'author': front_matter.get('author', ''),
            'date': front_matter.get('date', ''),
            'tags': front_matter.get('tags', []),
            'priority': front_matter.get('priority', 'medium'),
            'sections': sections,
            'summary': sections.get('key_findings', '')[:500] if 'key_findings' in sections else content[:500]
        }
    
    def _extract_structured_data(self, file_path: Path) -> Dict:
        """Extract content from structured data files"""
        if file_path.suffix == '.json':
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:  # YAML
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        
        return {
            'title': data.get('title', file_path.stem),
            'type': data.get('type', 'structured_data'),
            'schema': list(data.keys()) if isinstance(data, dict) else 'array',
            'summary': str(data)[:500] if isinstance(data, (str, int, float)) else json.dumps(data, indent=2)[:500],
            'data': data
        }
    
    def _extract_text_content(self, file_path: Path) -> Dict:
        """Extract content from plain text files"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic text analysis
        lines = content.split('\n')
        words = content.split()
        
        return {
            'title': file_path.stem,
            'type': 'text_document',
            'line_count': len(lines),
            'word_count': len(words),
            'summary': content[:500],
            'content': content
        }
    
    def analyze_relevance(self, source_info: Dict) -> Dict:
        """Analyze how relevant a source is to existing documentation"""
        relevance_score = 0
        matches = []
        
        # Keywords that indicate relevance to our project
        relevant_keywords = [
            'autonomous', 'projectile', 'guidance', 'trajectory', 'ballistics',
            'drone', 'multi-agent', 'sensor fusion', 'control theory',
            'communication', 'telemetry', 'gps', 'navigation', 'optimization',
            'kalman', 'filter', 'prediction', 'correction', 'aerodynamics'
        ]
        
        # Check title and summary for keywords
        text_to_check = f"{source_info.get('title', '')} {source_info.get('summary', '')}".lower()
        for keyword in relevant_keywords:
            if keyword in text_to_check:
                relevance_score += 1
                matches.append(keyword)
        
        # Boost score based on tags
        tags = source_info.get('tags', [])
        for tag in tags:
            if tag.lower() in relevant_keywords:
                relevance_score += 2
                matches.append(tag)
        
        # Determine relevance level
        if relevance_score >= 4:
            level = 'high'
        elif relevance_score >= 2:
            level = 'medium'
        else:
            level = 'low'
        
        return {
            'score': relevance_score,
            'level': level,
            'matches': matches,
            'recommended_sections': self._suggest_sections(matches)
        }
    
    def _suggest_sections(self, matches: List[str]) -> List[str]:
        """Suggest which documentation sections this source should update"""
        section_map = {
            'autonomous': ['system_architecture', 'planning_layer'],
            'projectile': ['actuation_layer', 'mathematical_framework'],
            'guidance': ['planning_layer', 'communication_layer'],
            'trajectory': ['mathematical_framework', 'planning_layer'],
            'ballistics': ['mathematical_framework'],
            'drone': ['perception_layer', 'commercial_options'],
            'multi-agent': ['communication_layer', 'system_architecture'],
            'sensor': ['perception_layer', 'sensor_fusion'],
            'control': ['actuation_layer', 'planning_layer'],
            'communication': ['communication_layer'],
            'telemetry': ['communication_layer'],
            'gps': ['perception_layer', 'adversarial_threats'],
            'navigation': ['perception_layer', 'planning_layer'],
            'optimization': ['mathematical_framework', 'planning_layer'],
            'kalman': ['sensor_fusion', 'target_prediction'],
            'filter': ['sensor_fusion'],
            'prediction': ['target_prediction'],
            'correction': ['actuation_layer'],
            'aerodynamics': ['mathematical_framework']
        }
        
        suggested_sections = set()
        for match in matches:
            if match in section_map:
                suggested_sections.update(section_map[match])
        
        return list(suggested_sections)
    
    def integrate_sources(self, new_sources: List[Dict]):
        """Integrate new sources into the documentation system"""
        for source in new_sources:
            relevance = self.analyze_relevance(source)
            source['relevance'] = relevance
            
            # Copy file to sources directory
            source_file = Path(source['file_path'])
            if source_file.exists():
                dest_path = Path(self.config['SOURCES_DIR']) / source_file.name
                import shutil
                shutil.copy2(source_file, dest_path)
                source['archived_path'] = str(dest_path)
            
            self.logger.info(f"Integrated source: {source['title']} (Relevance: {relevance['level']})")
        
        # Save updated database
        self.source_db['last_update'] = datetime.now().isoformat()
        self.save_source_database()
    
    def generate_integration_report(self) -> str:
        """Generate a report of recently integrated sources"""
        report = ["# Source Integration Report\n"]
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        recent_sources = [
            src for src in self.source_db['sources'].values()
            if src.get('status') == 'new'
        ]
        
        if not recent_sources:
            report.append("No new sources to integrate.\n")
            return "\n".join(report)
        
        report.append("## Recently Integrated Sources\n")
        
        for source in recent_sources:
            report.append(f"### {source['title']}")
            report.append(f"- **Category:** {source['category']}")
            report.append(f"- **Relevance:** {source.get('relevance', {}).get('level', 'unknown')}")
            report.append(f"- **Keywords:** {', '.join(source.get('relevance', {}).get('matches', []))}")
            report.append(f"- **Suggested Sections:** {', '.join(source.get('relevance', {}).get('recommended_sections', []))}")
            report.append(f"- **Summary:** {source.get('summary', '')[:200]}...")
            report.append("")
        
        return "\n".join(report)
    
    def run_integration_cycle(self):
        """Run a complete integration cycle"""
        self.logger.info("Starting source integration cycle...")
        
        # Scan for new sources
        new_sources = self.scan_input_directory()
        
        if new_sources:
            self.logger.info(f"Found {len(new_sources)} new sources")
            self.integrate_sources(new_sources)
            
            # Generate integration report
            report = self.generate_integration_report()
            
            # Save report
            with open("integration_report.md", 'w') as f:
                f.write(report)
            
            self.logger.info("Integration cycle completed successfully")
        else:
            self.logger.info("No new sources found")


if __name__ == "__main__":
    # Run integration system
    manager = SourceManager()
    manager.run_integration_cycle()