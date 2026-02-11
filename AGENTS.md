# Project SUPERLEAD - Agent Knowledge Base

**Purpose**: Document recurring issues, solutions, and project-specific patterns for autonomous agents working on this project.

## Recurring Issues and Solutions

### Python Integration

**Issue**: Session ingestion script fails with "config.yaml not found"
- **Cause**: Script executed from wrong directory
- **Solution**: Always run from project root (`C:\ai\superlead\`)
- **Prevention**: Use `claude_session_start.py` which handles directory context

**Issue**: Source files not detected during automatic ingestion
- **Cause**: Files placed in wrong subdirectory or unsupported format
- **Solution**:
  - Check file is in correct `input/` subdirectory (papers, briefings, data, references)
  - Verify format is supported (see `config.yaml` for list)
  - Run `python source_manager.py` manually to see detailed error messages

**Issue**: Relevance analysis shows low scores for clearly relevant sources
- **Cause**: Keyword list in `source_manager.py` doesn't match source terminology
- **Solution**:
  - Review source content manually
  - Consider updating keyword list in `source_manager.py:221-226`
  - Check if source uses alternative terminology (e.g., "UAV" vs "drone")

### Documentation Updates

**Issue**: Duplicate content across multiple technical documents
- **Cause**: Multiple documents cover overlapping topics
- **Solution**:
  - Check `docs/documentation_index.md` for cross-references
  - Use cross-links between documents instead of duplicating
  - Each document should own specific aspects (architecture owns design, math owns equations)

**Issue**: Missing citations for research claims
- **Cause**: Integration rushed without checking source database
- **Solution**:
  - Always check `source_database.json` for source details
  - Use format: `[Source Title](sources/filename.ext)`
  - Add citation metadata (author, date) when available

**Issue**: Outdated technical specifications after new research
- **Cause**: Multiple documents contain specs, not all updated
- **Solution**:
  - `technical_specifications.md` is source of truth for specs
  - Search all docs for the spec being updated: `grep -r "CEP" docs/`
  - Update all references or add note pointing to specs doc

### Task Management

**Issue**: Context file becomes stale during long research sessions
- **Cause**: Multiple discoveries not captured incrementally
- **Solution**:
  - Follow 2-Action Rule: Update `tasks/context.md` every 2 research operations
  - Use section structure: "Recent Discoveries" for new items
  - Archive old context to `tasks/archive/` when starting new phase

**Issue**: Todo items lack clear completion criteria
- **Cause**: Tasks written at too high a level
- **Solution**:
  - Include specific deliverables (e.g., "Add GPS spoofing section to adversarial_threats.md")
  - Use checkboxes for multi-step tasks
  - Reference specific files and sections

### Git Operations

**Issue**: PowerShell syntax errors when running git commands via scripts
- **Cause**: Windows PowerShell vs Bash syntax differences
- **Solution**:
  - Use direct commands instead of shell scripts
  - Use `git` commands directly instead of shell wrappers
  - See `tasks/lessons.md` for documented PowerShell workarounds

## Project-Specific Patterns

### Research Source Integration Pattern

**When**: New research source added to `input/` directory

**Standard workflow**:
1. Place file in appropriate `input/` subdirectory
2. Run `python claude_session_start.py`
3. Review `tasks/session_ingestion_suggestions.md`
4. Identify target documentation section(s)
5. Read current content in target doc
6. Integrate findings with citations
7. Update `tasks/context.md` with key discoveries
8. Mark task complete in `tasks/todo.md`

**Common mistakes**:
- Skipping step 5 (reading current content) → duplicates
- Forgetting step 7 (update context) → lost discoveries
- Not checking relevance analysis → miss better target sections

### Documentation Update Pattern

**When**: Adding new technical content to documentation

**Standard workflow**:
1. Check `docs/documentation_index.md` for existing coverage
2. Identify primary document (owns the content)
3. Identify secondary documents (cross-reference the content)
4. Update primary document with full details
5. Add cross-references to secondary documents
6. Update `documentation_index.md` if adding new major section
7. Check safety implications and update `docs/safety_protocols.md` if needed

**Document ownership guide**:
- **system_architecture.md**: Design decisions, layer interactions
- **mathematical_framework.md**: Equations, algorithms, theoretical proofs
- **technical_specifications.md**: Hardware specs, performance metrics, APIs
- **commercial_options.md**: Cost analysis, platform comparisons
- **adversarial_threats.md**: Security analysis, threat models, mitigations
- **safety_protocols.md**: Safety requirements, risk assessment, procedures

### Session Startup Pattern

**When**: Starting new Claude Code session

**Standard workflow**:
1. Run `python claude_session_start.py` (generates session context)
2. Review generated `tasks/session_ingestion_suggestions.md`
3. Read `tasks/context.md` for current research state
4. Scan `tasks/todo.md` for active work items
5. Check `tasks/lessons.md` for relevant patterns
6. Execute highest priority task from todo list

**Context check (5 questions)**:
- Where am I? → Current phase from `tasks/context.md`
- Where am I going? → Next milestone from `tasks/todo.md`
- What's the goal? → Project goal from `CLAUDE.md`
- What have I learned? → Recent discoveries from `tasks/context.md`
- What have I done? → Completed tasks from `tasks/todo.md`

### Relevance Analysis Pattern

**When**: Assessing if research source is relevant to project

**High relevance indicators** (score 4+):
- Contains 4+ project keywords
- Directly addresses autonomous systems or ballistics
- Includes technical specifications or mathematical models
- Provides implementation details or algorithms

**Medium relevance indicators** (score 2-3):
- Contains 2-3 project keywords
- Related to sensors, control, or communications
- Discusses similar systems or approaches
- Provides tangential technical context

**Low relevance indicators** (score 0-1):
- Few or no project keywords
- Generic information available elsewhere
- Not technical (policy, opinion, news)
- Wrong domain (not autonomous systems)

**Action by relevance**:
- **High**: Immediate integration, update multiple docs
- **Medium**: Review for specific insights, targeted updates
- **Low**: Archive for reference, no immediate integration

## Domain-Specific Knowledge

### Autonomous Projectile Guidance

**Key subsystems**:
1. **Perception**: Sensor fusion, object detection, environment mapping
2. **Planning**: Trajectory optimization, path planning, collision avoidance
3. **Control**: PID control, MPC, adaptive control
4. **Communication**: Telemetry, command & control, mesh networking
5. **Safety**: Fault detection, fail-safes, redundancy

**Critical constraints**:
- Real-time performance: <100ms control loop
- Accuracy: <1m CEP (Circular Error Probable)
- Range: 20km+ communication
- Duration: 30+ minutes mission time
- Safety: Multiple redundancy layers

### Non-Military Applications Focus

**Approved use cases**:
- Atmospheric research and weather monitoring
- Materials science testing and analysis
- Autonomous systems research and development
- Ballistics research for scientific purposes
- Academic research and educational applications

**Red flags to avoid**:
- Weaponization or military applications
- Targeting of people or property
- Surveillance without consent
- Export control violations
- Unethical research conduct

## Anti-Patterns to Avoid

### Research Integration Anti-Patterns

❌ **Copy-paste without synthesis**: Don't just copy source content into docs
✅ **Synthesize and integrate**: Understand content, integrate with existing knowledge

❌ **Duplicate information**: Don't repeat same content across multiple docs
✅ **Cross-reference**: Put content in one place, link from others

❌ **Missing context**: Don't add technical details without explaining relevance
✅ **Contextualize**: Explain how new information fits into system design

❌ **Orphaned sources**: Don't add sources without integrating into docs
✅ **Complete integration**: Ensure every source contributes to documentation

### Documentation Anti-Patterns

❌ **Shallow coverage**: Don't just list facts without analysis
✅ **Deep analysis**: Explain implications, trade-offs, design decisions

❌ **Outdated cross-references**: Don't leave broken links or outdated references
✅ **Maintain links**: Update all cross-references when moving content

❌ **Specs without rationale**: Don't state requirements without justification
✅ **Explain choices**: Document why specs were chosen, what alternatives considered

❌ **Safety as afterthought**: Don't add features without safety analysis
✅ **Safety-first**: Analyze safety implications before implementing features

## Quick Decision Trees

### "Should I create a new document?"

```
Is this a major new topic? (e.g., new subsystem, new domain)
  Yes → Create new doc in docs/, update documentation_index.md
  No ↓
Does existing doc cover this topic?
  Yes → Update existing doc with new section
  No ↓
Is this a variant/extension of existing topic?
  Yes → Add subsection to existing doc
  No → Check with user before creating new structure
```

### "Where should this research finding go?"

```
What is the primary focus?
  Design/Architecture → system_architecture.md
  Math/Algorithms → mathematical_framework.md
  Hardware/Performance → technical_specifications.md
  Cost/Platforms → commercial_options.md
  Security/Threats → adversarial_threats.md
  Safety/Ethics → safety_protocols.md
  Process/Workflow → ingestion_system.md

Multiple focuses?
  → Add to primary doc, cross-reference from others
```

### "How urgent is this task?"

```
Is it blocking other work?
  Yes → P0: Do immediately
  No ↓
Does it affect safety?
  Yes → P1: Do in current session
  No ↓
Is it integrating new research?
  Yes → P2: Do within 1-2 sessions
  No ↓
Is it cleanup/improvement?
  Yes → P3: Add to backlog, do when convenient
```

## Success Metrics

### Quality indicators for research integration:
- ✅ All sources have relevance analysis
- ✅ High-relevance sources integrated within 1 session
- ✅ All technical claims have citations
- ✅ Documentation cross-references are bidirectional
- ✅ Safety implications analyzed for new features

### Quality indicators for task management:
- ✅ Context file updated after every 2 research operations
- ✅ Todo items have clear completion criteria
- ✅ Lessons captured for recurring issues
- ✅ Archive maintains historical context
- ✅ Session startup takes <5 minutes

### Quality indicators for documentation:
- ✅ Each document has clear ownership and scope
- ✅ No duplicate content across documents
- ✅ All cross-references valid and current
- ✅ Technical depth appropriate for audience
- ✅ Code examples work as documented

---

**Note**: This file should be updated whenever new patterns are discovered or recurring issues are encountered. Capture lessons immediately while they're fresh.
