# Project SUPERLEAD - Automatic Session Ingestion System

## Overview

The Automatic Session Ingestion System provides a streamlined workflow for integrating new research sources into the Project SUPERLEAD documentation. It runs automatically at the start of every research session to ensure all new materials are processed and incorporated.

## Features

### 🔍 Automatic Discovery
- Scans all `input/` subdirectories for new files
- Supports multiple file formats: `.md`, `.pdf`, `.txt`, `.json`, `.csv`
- Identifies changes to existing files using hash comparison
- Detects and processes new research sources automatically

### 📊 Intelligent Analysis
- Extracts metadata and content from research sources
- Performs relevance analysis using keyword matching
- Maps content to appropriate documentation sections
- Generates integration recommendations

### 📝 Documentation Integration
- Provides specific recommendations for documentation updates
- Maps sources to relevant sections (System Architecture, Threat Assessment, etc.)
- Maintains source attribution and citation tracking
- Preserves original files in `sources/` directory

### 📈 Session Tracking
- Records all ingestion sessions with timestamps
- Tracks source categories and relevance scores
- Maintains complete audit trail of integration activities
- Provides session summary with system status

## Usage

### Starting a Research Session

**Windows Users:**
```cmd
start_session.bat
```

**Linux/Mac Users:**
```bash
./start_session.sh
```

**Manual Execution:**
```bash
python session_ingestion.py
```

### Adding New Research Sources

1. **Academic Papers**: Place in `input/papers/` (`.pdf`, `.txt`)
2. **Research Briefings**: Create in `input/briefings/` (`.md` with front matter)
3. **Data Files**: Add to `input/data/` (`.json`, `.csv`)
4. **References**: Place in `input/references/` (`.md`)

### Front Matter Template for Briefings

```markdown
---
title: "Research Title"
author: "Research Team"
date: "2025-01-15"
tags: ["keyword1", "keyword2", "keyword3"]
priority: "high"
---

## Key Findings
- Important research finding 1
- Important research finding 2

## Technical Specifications
- Technical detail 1
- Technical detail 2

## Integration Recommendations
This research is directly applicable to:
- System component 1
- Documentation section 2
```

## Session Output

### 1. Source Discovery
Reports the number and type of new sources found:
```
Found 2 new source(s):
  1. Advanced PID Control for Spinning Projectiles
     Category: briefings
     File: input\briefings\advanced_pid_research.md
  2. Quantum Sensors for Navigation Systems
     Category: briefings
     File: input\briefings\quantum_sensors.md
```

### 2. Integration Results
Displays relevance analysis and keyword matching:
```
Source: Advanced PID Control for Spinning Projectiles
   Relevance: HIGH
   Score: 9/10
   Keywords: projectile, trajectory, navigation, ballistics, guidance
   Suggested Updates: 5 sections
```

### 3. Documentation Recommendations
Provides specific update recommendations:
```
Recommended documentation updates:
  Document: docs/system_architecture.md
     Add 2 source(s) to planning_layer
     Add 1 source(s) to actuation_layer
  Document: docs/mathematical_framework.md
     Add 1 source(s) to control_theory
```

### 4. Session Summary
Comprehensive summary with system status:
```
New Sources Ingested: 2
By Category:
   briefings: 2
By Relevance:
   high: 2

System Status:
   Source Database: Active
   Config File: Active
   Documentation: 7 documents
```

## File Management

### Input Directory Structure
```
input/
├── papers/          # Academic papers (.pdf, .txt)
├── briefings/       # Research summaries (.md)
├── data/           # Research data (.json, .csv)
└── references/     # Citations and sources (.md)
```

### Archive Structure
```
sources/                    # Archived processed sources
├── advanced_pid_research.md
├── quantum_sensors.md
└── [other processed sources]
```

### Tracking Files
- `source_database.json`: Complete source tracking database
- `integration_report.md`: Session-by-session integration log
- `source_integration.log`: Detailed processing log

## Relevance Scoring

The system uses keyword matching to assess research relevance:

### High-Relevance Keywords (Score: 2-3 points each)
- autonomous, projectile, guidance, trajectory, ballistics
- drone, multi-agent, sensor fusion, control theory
- communication, telemetry, gps, navigation, optimization

### Medium-Relevance Keywords (Score: 1 point each)
- kalman, filter, prediction, correction, aerodynamics

### Scoring Levels
- **High**: 8+ points (immediate integration recommended)
- **Medium**: 4-7 points (review for relevant sections)
- **Low**: 0-3 points (archive for future reference)

## Section Mapping

Sources are automatically mapped to documentation sections:

| **Keywords** | **Documentation Sections** |
|--------------|--------------------------|
| autonomous, projectile, guidance | planning_layer, actuation_layer |
| drone, multi-agent | communication_layer, system_architecture |
| sensor, kalman, fusion | perception_layer, sensor_fusion |
| mathematical, optimization | mathematical_framework |
| gps, navigation | perception_layer, adversarial_threats |
| control, pid, mpc | planning_layer, actuation_layer |
| communication, telemetry | communication_layer |
| threat, jamming, spoofing | adversarial_threats |
| safety, regulatory | safety_protocols |
| commercial, cost, drone | commercial_options |

## Integration Workflow

### 1. Automatic Detection
- New files detected in input directories
- Hash comparison prevents duplicate processing
- File type verification for supported formats

### 2. Content Processing
- Markdown front matter extraction for briefings
- Text extraction from papers and data files
- Metadata parsing and normalization

### 3. Relevance Analysis
- Keyword matching against research vocabulary
- Score calculation and level determination
- Section recommendation mapping

### 4. Integration and Archival
- Source database updates with full metadata
- File archival to sources directory
- Integration report generation
- Documentation update recommendations

### 5. Session Logging
- Complete session audit trail
- System status verification
- Quick access command suggestions

## Advanced Features

### Session Recovery
- Tracks all ingestion sessions with timestamps
- Maintains complete history of source processing
- Enables rollback if needed

### System Health Monitoring
- Verifies database integrity
- Checks configuration file availability
- Monitors documentation file counts

### Unicode Support
- Handles international characters and special symbols
- Compatible across Windows, Linux, and macOS
- Robust encoding handling

### Error Handling
- Graceful handling of malformed files
- Detailed error reporting and logging
- Continuation processing despite individual file errors

## Troubleshooting

### Common Issues

**Unicode Encoding Errors:**
- Use UTF-8 encoded text files
- Ensure system locale supports Unicode
- Check file encoding before adding to input directory

**No Sources Found:**
- Verify files are in correct input subdirectories
- Check file extensions are supported
- Ensure files are not already processed

**Low Relevance Scores:**
- Include relevant keywords in titles and content
- Use proper front matter tags for briefings
- Ensure content clearly describes applications

**Integration Report Not Updating:**
- Check file permissions on integration_report.md
- Verify source_database.json is writable
- Ensure sufficient disk space

### Manual Override

If automatic ingestion fails, manual integration is available:
```bash
python source_manager.py
```

This provides detailed error reporting and manual file processing.

## Future Enhancements

### Planned Improvements
- **Machine Learning Relevance**: Enhanced relevance scoring using NLP
- **Automated Documentation**: Direct integration into documentation files
- **Web Interface**: Browser-based source management
- **API Integration**: RESTful interface for external systems
- **Collaborative Features**: Multi-user source sharing and review

### Extensibility
The system is designed for easy extension:
- Custom relevance scoring algorithms
- Additional file format support
- New documentation section mappings
- Custom processing pipelines

## Conclusion

The Automatic Session Ingestion System provides a robust, automated workflow for research source integration. It ensures that new materials are consistently processed, analyzed, and incorporated into the documentation with full attribution and tracking.

The system enables researchers to focus on analysis and implementation while maintaining comprehensive documentation of all integrated sources and their relevance to the autonomous projectile guidance research framework.