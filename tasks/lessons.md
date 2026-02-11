# Project SUPERLEAD - Lessons Learned

**Purpose**: Document patterns, fixes, and recurring issues to prevent repeating mistakes.

---

## PowerShell and Windows Compatibility

### PowerShell Syntax Error in Session Startup Scripts

**Issue**: PowerShell syntax error when attempting to run session catchup/startup scripts
**Date**: 2026-02-04
**Context**: Trying to automate session startup process

**Error**:
```
PowerShell syntax error in session catchup script
```

**Root Cause**:
- Windows PowerShell has different syntax than Bash
- Shell script patterns from Unix don't translate directly
- Need to use PowerShell-compatible commands or Python

**Solution**:
- Use Python scripts instead of shell scripts for cross-platform compatibility
- Created `session_ingestion.py` and `claude_session_start.py` as Python-based alternatives
- Python is cross-platform and already required for source manager

**Lesson**: When building automation for Windows, prefer Python scripts over shell scripts for better cross-platform compatibility and consistent behavior.

**Prevention**:
- Default to Python for automation scripts
- Use `.bat` files only for simple command wrappers
- Test on Windows before assuming Unix commands will work

---

## Research Management Patterns

### The 2-Action Rule for Multimodal Content

**Pattern**: Multimodal content (images, PDFs, browser views) doesn't persist in context

**Rule**: After every 2 view/browser/search operations, update `tasks/context.md`

**Why This Matters**:
- Visual information is processed but not stored in conversation history
- Context resets lose all multimodal information
- Writing it down immediately ensures nothing is lost

**Implementation**:
1. Perform research operation (web search, view image, read PDF)
2. Count: "That's operation 1"
3. Perform another research operation
4. Count: "That's operation 2"
5. IMMEDIATELY update `tasks/context.md` with findings
6. Reset counter to 0

**Example Workflow**:
```
1. Search web for "GPS spoofing techniques" → Operation 1
2. Read arxiv paper on LiDAR attacks → Operation 2
3. UPDATE tasks/context.md with key findings ← MUST DO
4. Search for "autonomous drone regulations" → Operation 1 (counter reset)
...
```

**Common Mistakes**:
- ❌ "I'll update the file after I finish all research" → Context resets, information lost
- ❌ "I remember what I read, no need to write it down" → Future sessions won't have access
- ✅ "Just did 2 operations, updating context.md now" → Information preserved

---

## Documentation Cross-Reference Pattern

**Pattern**: Multiple documents often need to reference the same concept

**Problem**: Duplicate information across documents creates maintenance burden and inconsistency

**Solution**: Single Source of Truth with Cross-References

**Implementation**:
1. **Identify document ownership** using `AGENTS.md` ownership guide
2. **Write full content in primary document**
3. **Add brief summary + link in secondary documents**
4. **Update `docs/documentation_index.md`** with cross-references

**Example**:
- **Full specs** in `technical_specifications.md`:
  ```markdown
  ## Target Accuracy
  - CEP (Circular Error Probable): < 1m
  - 95% confidence: < 2m
  - Real-time: < 100ms control loop
  ```

- **Reference** in `system_architecture.md`:
  ```markdown
  ## Performance Requirements
  The system must achieve <1m CEP accuracy. See [Technical Specifications](technical_specifications.md#target-accuracy) for complete performance metrics.
  ```

**Benefits**:
- Update specs in one place
- No duplicate maintenance
- Clear authority for each topic
- Easy to find canonical information

**Anti-Pattern**:
- ❌ Copy same specs into 3 different documents
- ❌ Slightly different versions in different places
- ❌ No indication of which version is correct

---

## Source Integration Best Practices

### Check Relevance Analysis Before Manual Integration

**Problem**: Manually integrating sources without checking relevance analysis wastes time

**Solution**: Always run source manager first to see relevance scores

**Workflow**:
1. Place source in `input/` directory
2. Run `python claude_session_start.py` (or `python source_manager.py`)
3. **Check relevance analysis output**
4. **High relevance (4+)**: Integrate immediately into multiple docs
5. **Medium relevance (2-3)**: Review for specific insights, targeted updates
6. **Low relevance (0-1)**: Archive for reference, usually no integration needed

**Time Savings**:
- Don't spend 30 minutes integrating a low-relevance source
- Prioritize high-relevance sources first
- Use keyword matches to identify target sections quickly

**Example**:
```
Source: "General Introduction to Drones"
Relevance: LOW (score: 1, matches: ["drone"])
Action: Archive for reference, no immediate integration

Source: "Kalman Filtering for Autonomous Navigation Systems"
Relevance: HIGH (score: 6, matches: ["kalman", "filter", "autonomous", "navigation"])
Action: Integrate immediately into mathematical_framework.md and sensor_fusion section
```

---

## Git and Version Control

### Commit Frequently with Clear Messages

**Pattern**: Frequent, descriptive commits make it easy to track changes and rollback if needed

**Lesson from Standardization**:
- Before major restructuring, created checkpoint: `"Pre-Claude-Code-standardization snapshot"`
- Clear message documents intent and timing
- Easy to rollback if needed
- Git history shows clear progression

**Best Practices**:
1. **Checkpoint before major changes**: Always commit clean state before restructuring
2. **Descriptive messages**: Explain WHAT and WHY, not just WHAT
3. **One logical change per commit**: Don't mix unrelated changes
4. **Use imperative mood**: "Add feature" not "Added feature"

**Good Commit Messages**:
- ✅ "Add Claude Code standards with task management directory"
- ✅ "Migrate task_plan.md content to tasks/todo.md"
- ✅ "Create Python integration bridge for Claude sessions"

**Bad Commit Messages**:
- ❌ "Update files"
- ❌ "Changes"
- ❌ "WIP"

### Archive, Don't Delete

**Pattern**: Preserve original files when restructuring, don't delete history

**Implementation**:
- Created `archive/pre_standardization/` directory
- Moved original `progress.md`, `task_plan.md`, `findings.md` to archive
- Files still accessible for reference
- Git history preserved
- Can rollback if needed

**Benefits**:
- No information loss
- Easy comparison between old and new structure
- Safety net for major changes
- Historical context preserved

---

## Task Management Lessons

### Clear Completion Criteria Prevent Ambiguity

**Problem**: Tasks like "Improve documentation" are never truly complete

**Solution**: Specific, testable completion criteria

**Bad Task**:
- ❌ "Improve documentation"
- ❌ "Enhance source integration"
- ❌ "Make system better"

**Good Task**:
- ✅ "Add GPS spoofing section to docs/adversarial_threats.md with 3 specific mitigation strategies"
- ✅ "Implement duplicate detection in source_manager.py with SHA-256 hash comparison"
- ✅ "Achieve <1m CEP accuracy in simulation tests for 95% of test runs"

**Criteria Checklist**:
- [ ] Can I verify completion with a test or check?
- [ ] Is the deliverable specific (file, section, metric)?
- [ ] Would another person understand what "done" means?
- [ ] Is success measurable?

---

## Python Integration Patterns

### Use Python for Cross-Platform Automation

**Lesson**: Python scripts work consistently across Windows, Linux, and Mac

**Anti-Pattern**:
- ❌ Write Bash script, fails on Windows
- ❌ Write PowerShell script, fails on Linux
- ❌ Write separate scripts for each platform

**Better Pattern**:
- ✅ Write Python script once
- ✅ Works on all platforms
- ✅ Easier to maintain
- ✅ Better error handling
- ✅ Already required for source manager

**Example**:
Instead of `start_session.sh` and `start_session.bat` with different logic:
```python
# claude_session_start.py - works everywhere
import os
import sys
from session_ingestion import SessionIngestion

def main():
    """Cross-platform session startup"""
    ingestion = SessionIngestion()
    ingestion.run_session_ingestion()

if __name__ == "__main__":
    main()
```

---

## Documentation Quality Patterns

### Safety Analysis is Not Optional

**Lesson**: Every new feature needs safety analysis before implementation

**Why This Matters**:
- Project SUPERLEAD is autonomous projectile guidance
- Safety failures can cause property damage or injury
- Regulatory compliance requires documented safety analysis
- Ethical responsibility for responsible research

**Implementation**:
1. **Before adding feature**: Ask "What are the safety implications?"
2. **Document in safety_protocols.md**: Add safety considerations
3. **Design mitigations**: Add fail-safes, redundancy, monitoring
4. **Test safety mechanisms**: Verify fail-safes work

**Example**:
Adding GPS spoofing detection:
- ✅ Document spoofing scenarios in adversarial_threats.md
- ✅ Design mitigation strategy (multi-sensor validation)
- ✅ Add safety implications to safety_protocols.md
- ✅ Specify fail-safe behavior (switch to backup navigation)
- ✅ Test spoofing detection in simulation

**Anti-Pattern**:
- ❌ "GPS spoofing detection added" (commit message, no safety analysis)
- ❌ Feature implemented without considering edge cases
- ❌ No documentation of safety implications
- ❌ No fail-safe behavior defined

---

## Session Startup Checklist Pattern

**Pattern**: Consistent session startup ensures nothing is missed

**Checklist**:
1. [ ] Run `python claude_session_start.py`
2. [ ] Review `tasks/session_ingestion_suggestions.md` (if new sources)
3. [ ] Read `tasks/context.md` - 5-question check
4. [ ] Scan `tasks/todo.md` - identify highest priority task
5. [ ] Check `tasks/lessons.md` - scan for relevant patterns
6. [ ] Review `AGENTS.md` - check for applicable patterns

**Time**: ~5 minutes
**Value**: Full context, no missed information, ready to work efficiently

**Benefits**:
- Never start work without current context
- Catch new research sources immediately
- Identify blockers before starting work
- Apply learned patterns automatically

---

## Future Lessons

*This section will grow as we encounter new patterns and issues*

### Template for New Lessons

**Issue/Pattern Name**: Brief descriptive name

**Problem**: What goes wrong or what pattern is being documented

**Solution**: How to fix or implement the pattern

**Example**: Concrete example showing the pattern in action

**Prevention**: How to avoid the problem in future

**Related**: Links to other relevant lessons or documentation

---

**Note**: Update this file immediately when you discover a new pattern or solve a recurring issue. Fresh lessons are the most valuable.
