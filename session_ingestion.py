#!/usr/bin/env python3
"""
Automatic Session Ingestion System
Runs at start of every session to scan for and ingest new research sources
"""

import os
import sys
import json
import yaml
from datetime import datetime
from pathlib import Path
from source_manager import SourceManager

class SessionIngestion:
    """Automatic ingestion system for session startup"""
    
    def __init__(self):
        self.source_manager = SourceManager()
        self.session_start = datetime.now()
        
    def run_session_ingestion(self):
        """Main ingestion process for session startup"""
        print("=" * 60)
        print("AUTOMATIC SESSION INGESTION SYSTEM")
        print("=" * 60)
        print(f"Session started: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Step 1: Check for new sources
        print("Step 1: Scanning for new research sources...")
        new_sources = self.source_manager.scan_input_directory()
        
        if not new_sources:
            print("No new sources found")
            self.display_session_summary()
            return
        
        print(f"Found {len(new_sources)} new source(s):")
        for i, source in enumerate(new_sources, 1):
            print(f"  {i}. {source.get('title', 'Unknown Title')}")
            print(f"     Category: {source['category']}")
            print(f"     File: {source['file_path']}")
            print()
        
        # Step 2: Analyze and integrate sources
        print("Step 2: Analyzing sources and integrating...")
        self.source_manager.integrate_sources(new_sources)
        
        # Step 3: Display integration results
        print("\nStep 3: Integration Results")
        print("-" * 40)
        
        for source in new_sources:
            relevance = source.get('relevance', {})
            print(f"Source: {source.get('title', 'Unknown')}")
            print(f"   Relevance: {relevance.get('level', 'unknown').upper()}")
            print(f"   Score: {relevance.get('score', 0)}/10")
            print(f"   Keywords: {', '.join(relevance.get('matches', []))}")
            print(f"   Suggested Updates: {len(relevance.get('recommended_sections', []))} sections")
            print()
        
        # Step 4: Update documentation recommendations
        print("Step 4: Documentation Update Recommendations")
        print("-" * 50)
        self.generate_documentation_recommendations(new_sources)
        
        # Step 5: Update integration report
        print("\nStep 5: Updating integration report...")
        self.update_integration_report(new_sources)
        
        # Step 6: Display session summary
        self.display_session_summary(new_sources)
        
        print("\nIngestion complete! Ready for research session.")
        
    def generate_documentation_recommendations(self, new_sources):
        """Generate specific recommendations for documentation updates"""
        
        # Map sources to documentation sections
        section_updates = {}
        
        for source in new_sources:
            relevance = source.get('relevance', {})
            sections = relevance.get('recommended_sections', [])
            
            for section in sections:
                if section not in section_updates:
                    section_updates[section] = []
                section_updates[section].append(source)
        
        if not section_updates:
            print("  No immediate documentation updates required")
            return
        
        print("  Recommended documentation updates:")
        
        section_docs = {
            'perception_layer': 'docs/system_architecture.md',
            'mathematical_framework': 'docs/mathematical_framework.md',
            'planning_layer': 'docs/system_architecture.md',
            'actuation_layer': 'docs/system_architecture.md',
            'communication_layer': 'docs/system_architecture.md',
            'sensor_fusion': 'docs/technical_specifications.md',
            'target_prediction': 'docs/mathematical_framework.md',
            'commercial_options': 'docs/commercial_options.md',
            'adversarial_threats': 'docs/adversarial_threats.md',
            'safety_protocols': 'docs/safety_protocols.md'
        }
        
        for section, sources in section_updates.items():
            doc_file = section_docs.get(section, 'docs/documentation_index.md')
            print(f"    Document: {doc_file}")
            print(f"       Add {len(sources)} source(s) to {section}")
            
            for source in sources:
                print(f"       - {source.get('title', 'Unknown')}")
        
        print("\n  Tip: Use 'python source_manager.py' to see detailed integration report")
    
    def update_integration_report(self, new_sources):
        """Update the integration report with session information"""
        
        # Read existing report
        report_path = "integration_report.md"
        if os.path.exists(report_path):
            with open(report_path, 'r') as f:
                report_content = f.read()
        else:
            report_content = "# Source Integration Report\n\n"
        
        # Add session information
        session_section = f"""
---
## Session Ingestion - {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}

**Sources Processed**: {len(new_sources)}
**Session Type**: Automatic Session Startup
**Integration Status**: Complete

### Newly Integrated Sources
"""
        
        for source in new_sources:
            relevance = source.get('relevance', {})
            session_section += f"""
- **{source.get('title', 'Unknown')}**
  - Category: {source['category']}
  - Relevance: {relevance.get('level', 'unknown')}
  - Keywords: {', '.join(relevance.get('matches', []))}
  - Archived: {source.get('archived_path', 'Not archived')}
"""
        
        # Update report
        with open(report_path, 'w') as f:
            f.write(report_content + session_section)
        
        print(f"  Updated: {report_path}")
    
    def display_session_summary(self, new_sources=None):
        """Display session summary"""
        print("\n" + "=" * 60)
        print("SESSION SUMMARY")
        print("=" * 60)
        
        if new_sources:
            print(f"New Sources Ingested: {len(new_sources)}")
            
            # Count by category
            categories = {}
            for source in new_sources:
                cat = source['category']
                categories[cat] = categories.get(cat, 0) + 1
            
            print("By Category:")
            for cat, count in categories.items():
                print(f"   {cat}: {count}")
            
            # Count by relevance
            relevance_counts = {}
            for source in new_sources:
                relevance = source.get('relevance', {}).get('level', 'unknown')
                relevance_counts[relevance] = relevance_counts.get(relevance, 0) + 1
            
            print("By Relevance:")
            for relevance, count in relevance_counts.items():
                print(f"   {relevance}: {count}")
        
        # System status
        print("\nSystem Status:")
        print(f"   Source Database: {'Active' if os.path.exists('source_database.json') else 'Not Found'}")
        print(f"   Config File: {'Active' if os.path.exists('config.yaml') else 'Not Found'}")
        print(f"   Documentation: {len([f for f in os.listdir('docs/') if f.endswith('.md')])} documents")
        
        # Quick access commands
        print("\nQuick Access:")
        print("   View Documentation: ls docs/")
        print("   Integration Report: cat integration_report.md")
        print("   Source Database: cat source_database.json")
        print("   Manual Integration: python source_manager.py")
        
        print("\n" + "=" * 60)

def main():
    """Main ingestion function"""
    try:
        ingestion = SessionIngestion()
        ingestion.run_session_ingestion()
    except Exception as e:
        print(f"Ingestion failed: {e}")
        print("Please check system configuration and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()