# Project SUPERLEAD - Template Reusability Guide

**Purpose**: This document explains how to use Project SUPERLEAD as a template for other scientific research projects.

---

## What Makes This Project Reusable

Project SUPERLEAD provides a comprehensive framework for autonomous scientific research projects:

### Core Infrastructure ✅
- **Automated source integration system** - Scans, analyzes, and archives research sources
- **Claude Code workflow integration** - Task management, context tracking, lessons learned
- **Git-based version control** - Full history tracking and collaboration support
- **Comprehensive documentation structure** - 8 technical documents covering all aspects
- **Safety-first design philosophy** - Ethics and safety integrated at every level

### Customizable Components 🔧
- **Keywords and relevance analysis** - Easily adapted to different research domains
- **Documentation templates** - Structured but flexible for various topics
- **Source categories** - Can be customized for different research types
- **Task management templates** - Adaptable to different project workflows

---

## Template Components

### Core Infrastructure (Keep As-Is)
These components work for any scientific research project:

1. **Python Automation System**
   - `source_manager.py` - File scanning, metadata extraction, archiving
   - `session_ingestion.py` - Automatic session startup workflow
   - `claude_session_start.py` - Claude Code integration bridge
   - `config.yaml` - Configuration file

2. **Claude Code Integration**
   - `CLAUDE.md` - Project configuration and workflow
   - `AGENTS.md` - Recurring patterns and solutions
   - `.claudeignore` - File exclusion patterns
   - `tasks/` directory structure

3. **Directory Structure**
   - `docs/` - Technical documentation
   - `input/` - Source intake with categorization
   - `sources/` - Archived integrated sources
   - `tasks/` - Task management and context
   - `archive/` - Historical files

### Project-Specific Components (Customize)
These need to be adapted for each new domain:

1. **Keywords** (in `source_manager.py:221-226`)
   ```python
   relevant_keywords = [
       'autonomous', 'projectile', 'guidance', 'trajectory', 'ballistics',
       'drone', 'multi-agent', 'sensor fusion', 'control theory',
       # ... customize for your domain
   ]
   ```

2. **Documentation Topics** (create domain-specific documents)
   - Current: system architecture, ballistics, adversarial threats, etc.
   - Climate Science Example: climate models, data collection, analysis methods
   - Biomedical Example: protocols, data privacy, regulatory compliance

3. **Safety Considerations** (adapt to domain-specific risks)
   - Current: autonomous systems, physical safety, aviation regulations
   - Lab Research Example: chemical safety, biosafety levels, waste disposal
   - Data Science Example: privacy, bias, ethical AI use

---

## Customization Guide

### Step 1: Copy Template Structure

**Option A: Use Existing Project as Base**
```bash
# Copy entire project structure
cd C:\ai\
cp -r superlead my_new_project
cd my_new_project

# Clean out project-specific content
rm -rf docs/*.md
rm -rf input/*
rm -rf sources/*
rm -rf tasks/*.md
rm source_database.json
```

**Option B: Use Clean Template Package**
```bash
# Copy from template directory
cd C:\ai\
cp -r science_project_template my_new_project
cd my_new_project
```

### Step 2: Customize Configuration

**Update `config.yaml`**:
```yaml
# Change project name and paths
PROJECT_NAME: "My New Research Project"
PROJECT_TYPE: "climate_science"  # or "biomedical", "materials", etc.

# Keep standard structure
INPUT_DIR: "input"
DOCS_DIR: "docs"
SOURCES_DIR: "sources"
# ...
```

**Update `CLAUDE.md`**:
- Change project overview and purpose
- Update research focus areas
- Modify key technical constraints
- Adapt documentation standards for your domain

### Step 3: Customize Keywords

**Edit `source_manager.py`** (line 221-226):
```python
# FOR CLIMATE SCIENCE EXAMPLE:
relevant_keywords = [
    'climate', 'atmospheric', 'greenhouse', 'carbon', 'emissions',
    'temperature', 'precipitation', 'weather', 'modeling',
    'satellite', 'sensor', 'data collection', 'trend analysis',
    'policy', 'mitigation', 'adaptation', 'scenarios'
]

# FOR BIOMEDICAL EXAMPLE:
relevant_keywords = [
    'protein', 'genome', 'gene expression', 'clinical trial',
    'patient', 'diagnosis', 'treatment', 'drug', 'therapy',
    'biomarker', 'imaging', 'pathology', 'epidemiology',
    'regulatory', 'FDA', 'IRB', 'consent', 'privacy'
]
```

**Update section mapping** in `source_manager.py:259-286`:
```python
# FOR CLIMATE SCIENCE EXAMPLE:
section_map = {
    'climate': ['climate_models', 'data_analysis'],
    'atmospheric': ['atmospheric_science', 'measurement_systems'],
    'emissions': ['emissions_modeling', 'policy_analysis'],
    # ... map keywords to your document sections
}
```

### Step 4: Create Documentation Structure

**Create domain-specific documents in `docs/`**:

**Climate Science Example**:
- `climate_models.md` - Modeling approaches and validation
- `data_collection.md` - Sensor systems and data sources
- `analysis_methods.md` - Statistical and computational methods
- `policy_implications.md` - Policy analysis and recommendations
- `validation_protocols.md` - Data quality and validation
- `collaboration_framework.md` - Multi-institution coordination

**Biomedical Example**:
- `research_protocols.md` - Experimental design and procedures
- `data_privacy.md` - HIPAA compliance and privacy protection
- `regulatory_compliance.md` - FDA, IRB, GCP requirements
- `statistical_methods.md` - Analysis approaches and validation
- `clinical_applications.md` - Translation to clinical practice
- `ethical_considerations.md` - Ethics and patient safety

### Step 5: Update Safety and Ethics

**Adapt `docs/safety_protocols.md`** for your domain:

**For Lab Research**:
- Chemical safety and MSDS protocols
- Biosafety levels and containment
- PPE requirements and training
- Waste disposal procedures
- Emergency response plans

**For Data Science**:
- Data privacy and security
- Algorithmic bias detection and mitigation
- Transparency and explainability
- Ethical AI principles
- Regulatory compliance (GDPR, CCPA, etc.)

### Step 6: Initialize Git Repository

```bash
# Initialize new Git repository
git init

# Add initial files
git add .
git commit -m "Initial commit: [Project Name] based on SUPERLEAD template"

# Create GitHub repository (optional)
gh repo create [username]/[project-name] --private --source=. --remote=origin --push
```

### Step 7: Test the Workflow

```bash
# Test Python system
python source_manager.py

# Test session startup
python claude_session_start.py

# Verify directory structure
ls tasks/
ls docs/
ls input/

# Check Claude Code files
cat CLAUDE.md
cat tasks/todo.md
```

---

## Use Case Examples

### Example 1: Climate Science Research Platform

**Project Goal**: Analyze climate data from multiple sources, model future scenarios

**Customizations**:
- Keywords: climate, atmospheric, greenhouse gases, temperature, precipitation
- Documents: climate_models.md, data_collection.md, satellite_systems.md
- Input categories: satellite data, weather station data, model outputs, research papers
- Safety focus: Data accuracy, model validation, policy implications

**Workflow**:
1. Collect satellite data and weather station readings → `input/data/`
2. Add climate research papers → `input/papers/`
3. Session ingestion analyzes relevance to climate keywords
4. Integrate findings into climate models and analysis docs
5. Track modeling decisions in `tasks/context.md`

### Example 2: Biomedical Research Project

**Project Goal**: Analyze protein structures and predict drug interactions

**Customizations**:
- Keywords: protein, genome, structure, drug, binding, clinical, patient
- Documents: research_protocols.md, data_privacy.md, regulatory_compliance.md
- Input categories: protein databases, clinical trial data, research papers, regulatory guidance
- Safety focus: Data privacy, regulatory compliance, ethical considerations

**Workflow**:
1. Import protein structure data → `input/data/`
2. Add research papers on drug interactions → `input/papers/`
3. Session ingestion flags high-relevance sources
4. Integrate into research protocols and methods
5. Document ethical considerations and compliance requirements

### Example 3: Materials Science Testing

**Project Goal**: Test new materials under various conditions, document properties

**Customizations**:
- Keywords: material, alloy, composite, strength, fatigue, thermal, chemical
- Documents: material_properties.md, testing_protocols.md, analysis_methods.md
- Input categories: test data, material specifications, research papers, standards
- Safety focus: Handling procedures, disposal, environmental impact

**Workflow**:
1. Import test data from experiments → `input/data/`
2. Add material science papers → `input/papers/`
3. Add standards and specifications → `input/references/`
4. Session ingestion maps sources to material types
5. Update material property databases and testing protocols

---

## Template Maintenance Guidelines

### Keeping Template Updated

**When to update template**:
- New Python automation features added
- Better patterns discovered in `AGENTS.md`
- Claude Code workflow improvements
- Documentation structure refinements

**How to update**:
1. Make improvements in Project SUPERLEAD first
2. Test thoroughly to ensure they work
3. Extract generic components to template
4. Document changes in template CHANGELOG
5. Update `TEMPLATE_GUIDE.md` with new features

### Version Management

**Template versioning**:
- Use Git tags for template versions: `v1.0`, `v1.1`, etc.
- Document breaking changes in CHANGELOG
- Maintain backward compatibility when possible
- Provide migration guides for major changes

### Contributing Improvements

**Share template enhancements**:
1. Document the problem solved
2. Show before/after examples
3. Explain why it's generally applicable
4. Test on multiple domains if possible
5. Submit as improvement to template repository

---

## Template Comparison

### Project SUPERLEAD (Autonomous Systems)
- **Domain**: Autonomous projectile guidance
- **Keywords**: autonomous, ballistics, trajectory, sensor fusion
- **Focus**: Real-time control, safety-critical systems, adversarial threats
- **Documents**: System architecture, mathematical framework, adversarial threats

### Climate Science Template (Hypothetical)
- **Domain**: Climate modeling and analysis
- **Keywords**: climate, atmospheric, emissions, modeling
- **Focus**: Data collection, long-term trends, policy implications
- **Documents**: Climate models, data collection, satellite systems

### Biomedical Template (Hypothetical)
- **Domain**: Biomedical research
- **Keywords**: protein, clinical, patient, drug, regulatory
- **Focus**: Privacy, regulatory compliance, ethical research
- **Documents**: Research protocols, data privacy, regulatory compliance

**Common Infrastructure** (all templates):
- Python automation system
- Claude Code integration
- Git-based version control
- Task management workflow
- Safety and ethics focus

---

## Success Checklist

**Template is ready when**:
- [ ] Python scripts run without errors
- [ ] Session ingestion detects and processes test sources
- [ ] Keywords are customized for target domain
- [ ] Documentation structure matches domain needs
- [ ] Safety considerations adapted to domain risks
- [ ] `CLAUDE.md` reflects project specifics
- [ ] `tasks/todo.md` has initial project tasks
- [ ] Git repository initialized and first commit made
- [ ] Test workflow runs end-to-end successfully

---

## Getting Help

**If you encounter issues**:
1. Check `tasks/lessons.md` for similar problems
2. Review `AGENTS.md` for patterns and solutions
3. Verify `config.yaml` settings are correct
4. Test Python scripts individually to isolate issues
5. Check Git history for working versions
6. Consult Project SUPERLEAD for reference implementation

---

## Template Package Location

**Clean template package**: `C:\ai\science_project_template\`

This is a minimal, ready-to-customize version with:
- All Python automation scripts
- Generic configuration with placeholders
- Empty but structured directories
- Template documentation files
- Starter task management files
- Customization checklist

**To create new project**:
```bash
cd C:\ai\
cp -r science_project_template my_new_project
cd my_new_project
# Follow customization guide above
```

---

**Note**: This template represents dozens of hours of research, development, and refinement. Use it to accelerate your scientific research projects while maintaining high standards for documentation, safety, and reproducibility.
