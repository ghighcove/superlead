# Project SUPERLEAD - Claude Code Configuration

## Project Overview

**What**: Scientific autonomous projectile guidance research platform for non-military applications

**Purpose**: Comprehensive research system for atmospheric research, materials testing, and autonomous systems development

**Key Differentiators**:
- Automated Python source integration system
- 8 comprehensive technical documents
- Research briefing ingestion with relevance analysis
- Git-tracked research history with 5-phase methodology

## Session Startup Protocol

**Automatic Workflow (Recommended)**:
1. Run: `python claude_session_start.py` (or `start_session.bat` on Windows)
2. System automatically:
   - Scans `input/` for new research sources
   - Analyzes relevance using keyword matching
   - Generates `tasks/session_ingestion_suggestions.md`
   - Creates integration recommendations
3. Review generated suggestions in `/tasks/` directory
4. Check `tasks/context.md` for current research state
5. Review `tasks/todo.md` for active work items
6. Scan `tasks/lessons.md` for recurring patterns

**Manual Workflow**:
```bash
python source_manager.py          # Process sources manually
cat tasks/context.md              # Review current state
cat tasks/todo.md                 # Check active tasks
cat integration_report.md         # View integration results
```

## Directory Structure

```
C:\ai\superlead\
├── docs/                         # 8 comprehensive technical documents
│   ├── system_architecture.md    # 5-layer design framework
│   ├── commercial_options.md     # Cost-optimized platform analysis
│   ├── adversarial_threats.md    # Security and countermeasures
│   ├── mathematical_framework.md # Ballistic equations & algorithms
│   ├── technical_specifications.md # Hardware specs & APIs
│   ├── safety_protocols.md       # Safety & ethics guidelines
│   ├── ingestion_system.md       # Source integration workflow
│   └── documentation_index.md    # Document cross-reference
├── input/                        # Research source intake (monitored)
│   ├── papers/                   # Academic papers (.pdf, .txt)
│   ├── briefings/                # Research summaries (.md)
│   ├── data/                     # Research data (.json, .csv)
│   └── references/               # Citations and sources
├── sources/                      # Archived integrated sources
├── tasks/                        # Claude Code task management
│   ├── todo.md                   # Active work items
│   ├── context.md                # Current research session state
│   ├── lessons.md                # Patterns, fixes, recurring issues
│   └── archive/                  # Completed task archives
├── archive/                      # Historical project files
│   └── pre_standardization/      # Original files before migration
├── source_manager.py             # Source integration engine
├── session_ingestion.py          # Automatic session startup
└── claude_session_start.py       # Claude Code integration bridge
```

## Automated Systems Overview

### Source Integration System

**What it does**:
- Monitors `input/` directory for new research files
- Extracts metadata and content from multiple formats
- Analyzes relevance using keyword matching (20+ keywords)
- Suggests documentation sections for integration
- Archives sources to `sources/` directory
- Maintains `source_database.json` with full history

**Supported Formats**:
- **Briefings**: `.md` (with YAML front matter)
- **Papers**: `.txt`, `.pdf` (text extracted)
- **Data**: `.json`, `.yaml`, `.csv`
- **References**: `.md`, `.txt`

**Relevance Analysis**:
- Scores sources on 10-point scale
- Matches 20+ project-specific keywords
- Categorizes as HIGH (4+), MEDIUM (2-3), LOW (0-1)
- Maps keywords to specific documentation sections

### Session Ingestion

**Automatic startup workflow**:
1. Scans for new sources since last session
2. Processes and analyzes each source
3. Generates integration recommendations
4. Updates `integration_report.md`
5. Creates Claude-friendly summary in `tasks/session_ingestion_suggestions.md`

**What gets generated**:
- Session timestamp and source count
- Relevance scores for each source
- Recommended documentation updates
- Keyword matches and context
- Suggested next actions

## Research Workflow Guide

### Adding New Research Sources

**Step 1**: Place files in appropriate `input/` subdirectory
- `input/papers/` - Academic research papers
- `input/briefings/` - Research summaries and briefings
- `input/data/` - Datasets and structured data
- `input/references/` - Citations and reference materials

**Step 2**: Run session startup
```bash
python claude_session_start.py
```

**Step 3**: Review suggestions
```bash
cat tasks/session_ingestion_suggestions.md
```

**Step 4**: Update documentation
- Review recommended sections
- Integrate relevant findings
- Update technical documents in `docs/`
- Cross-reference in `documentation_index.md`

**Step 5**: Update task tracking
- Mark completed items in `tasks/todo.md`
- Update research state in `tasks/context.md`
- Log any new patterns in `tasks/lessons.md`

### Documentation Update Pattern

**When integrating new research**:
1. Identify target document(s) from suggestions
2. Read current section to understand existing content
3. Add new information with proper citations
4. Update cross-references in related documents
5. Add source to `documentation_index.md`
6. Update `tasks/context.md` with key discoveries

## Commands Quick Reference

### Session Management
```bash
python claude_session_start.py    # Start new session (recommended)
python session_ingestion.py       # Run ingestion only
python source_manager.py          # Manual source processing
```

### Status Checks
```bash
cat tasks/context.md              # Current research state
cat tasks/todo.md                 # Active work items
cat tasks/lessons.md              # Known patterns and fixes
cat integration_report.md         # Latest integration results
cat source_database.json          # Full source history
```

### Documentation Access
```bash
ls docs/                          # List all technical documents
cat docs/documentation_index.md   # Document cross-reference
```

### Git Operations
```bash
git status                        # Check repository state
git log --oneline -10             # Recent commits
git diff                          # View uncommitted changes
```

## Integration Notes for Python Systems

### How Python and Claude Work Together

**Python handles**:
- File monitoring and scanning
- Content extraction from multiple formats
- Relevance analysis and scoring
- Database management (JSON)
- Source archiving

**Claude handles**:
- Documentation writing and updates
- Research synthesis and analysis
- Task planning and tracking
- Pattern recognition in lessons
- High-level research strategy

**Bridge point**: `claude_session_start.py`
- Runs Python ingestion system
- Generates Claude-friendly markdown summaries
- Creates task directory structure if needed
- Provides quick-start guidance

### When to Run What

**Every session start**: `python claude_session_start.py`
**After adding sources**: Automatic (included in session start)
**Manual integration**: `python source_manager.py` (when needed)
**Check status**: Read files in `tasks/` directory

## Project-Specific Context

### Research Focus Areas
1. **Autonomous Systems**: Multi-agent coordination, sensor fusion
2. **Ballistic Theory**: Trajectory optimization, prediction algorithms
3. **Safety Protocols**: Risk assessment, fail-safe mechanisms
4. **Communication**: Telemetry, frequency hopping, encryption
5. **Adversarial Threats**: GPS spoofing, jamming, cyber threats

### Key Technical Constraints
- **Non-military applications only**: Atmospheric research, materials testing
- **Budget optimization**: $2K-35K platform tiers
- **Regulatory compliance**: FAA Part 107, EASA, FCC
- **Safety-first design**: Multiple redundancy layers
- **Real-time performance**: <100ms control loop, <1m CEP

### Documentation Standards
- All claims must have citable sources
- Cross-reference related documents
- Include practical implementation details
- Document assumptions and constraints
- Maintain comprehensive safety analysis

## Common Operations

### Starting a New Research Session
```bash
# 1. Start session with automatic ingestion
python claude_session_start.py

# 2. Review session suggestions
cat tasks/session_ingestion_suggestions.md

# 3. Check current research state
cat tasks/context.md

# 4. Review active tasks
cat tasks/todo.md

# 5. Scan for known patterns
cat tasks/lessons.md
```

### Integrating Research Findings
1. Identify target documentation section
2. Read current content in relevant `docs/*.md` file
3. Add findings with source citations
4. Update `tasks/context.md` with key discoveries
5. Mark task complete in `tasks/todo.md`
6. Commit changes to Git

### Creating New Documentation
1. Check `docs/documentation_index.md` for gaps
2. Create new document in `docs/` directory
3. Follow existing document structure
4. Add cross-references to related docs
5. Update `documentation_index.md`
6. Update `README.md` if adding major section

## Safety and Ethics Reminders

- **All research is for non-military scientific purposes**
- **Comply with all aviation and communications regulations**
- **Prioritize safety in all design decisions**
- **Never compromise on ethical research standards**
- **Document all safety considerations thoroughly**

## Troubleshooting

### Python Integration Issues
- **Error**: "config.yaml not found"
  - **Fix**: Ensure working directory is project root
- **Error**: "No module named 'yaml'"
  - **Fix**: `pip install pyyaml`
- **Error**: Source not detected
  - **Fix**: Check file is in correct `input/` subdirectory and supported format

### Task Management
- **Context file outdated**: Review and update `tasks/context.md` manually
- **Stale todo items**: Archive completed tasks to `tasks/archive/`
- **Lost session state**: Check Git history and `archive/` directory

### Documentation Conflicts
- **Duplicate information**: Check `documentation_index.md` for cross-references
- **Outdated specs**: Review `tasks/context.md` for latest decisions
- **Missing citations**: Check `source_database.json` for source details

---

**Ready to start**: Run `python claude_session_start.py` to begin your research session
