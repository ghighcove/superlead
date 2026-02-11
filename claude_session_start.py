#!/usr/bin/env python3
"""
Claude Code Integration Bridge
Connects Python automation with Claude Code workflow
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from session_ingestion import SessionIngestion

class ClaudeSessionBridge:
    """Bridge between Python ingestion and Claude Code workflow"""

    def __init__(self):
        self.session_start = datetime.now()
        self.tasks_dir = Path("tasks")

    def ensure_task_structure(self):
        """Ensure /tasks/ directory structure exists"""
        directories = [
            self.tasks_dir,
            self.tasks_dir / "archive"
        ]

        for directory in directories:
            directory.mkdir(exist_ok=True)

        # Ensure required files exist
        required_files = {
            'todo.md': self.tasks_dir / "todo.md",
            'context.md': self.tasks_dir / "context.md",
            'lessons.md': self.tasks_dir / "lessons.md"
        }

        for file_name, file_path in required_files.items():
            if not file_path.exists():
                print(f"⚠️  Warning: {file_name} not found. Run full setup first.")

    def run_session_ingestion(self):
        """Run Python ingestion system"""
        print("=" * 60)
        print("CLAUDE CODE SESSION STARTUP")
        print("=" * 60)
        print(f"Session: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        # Ensure directory structure
        self.ensure_task_structure()

        # Run Python ingestion
        print("Running source ingestion system...")
        print("-" * 40)
        ingestion = SessionIngestion()
        ingestion.run_session_ingestion()

    def generate_claude_suggestions(self, new_sources):
        """Generate Claude-friendly suggestions file"""
        suggestions_path = self.tasks_dir / "session_ingestion_suggestions.md"

        with open(suggestions_path, 'w', encoding='utf-8') as f:
            f.write("# Session Ingestion Suggestions\n\n")
            f.write(f"**Generated**: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            if not new_sources:
                f.write("## No New Sources\n\n")
                f.write("No new research sources detected since last session.\n\n")
                f.write("**Next Steps**:\n")
                f.write("1. Review `tasks/todo.md` for active work items\n")
                f.write("2. Check `tasks/context.md` for current research state\n")
                f.write("3. Continue with highest priority task\n")
                return

            f.write(f"## New Sources Detected: {len(new_sources)}\n\n")

            # Group by relevance
            high_rel = [s for s in new_sources if s.get('relevance', {}).get('level') == 'high']
            med_rel = [s for s in new_sources if s.get('relevance', {}).get('level') == 'medium']
            low_rel = [s for s in new_sources if s.get('relevance', {}).get('level') == 'low']

            if high_rel:
                f.write("### 🔴 High Relevance (Integrate Immediately)\n\n")
                for source in high_rel:
                    self._write_source_detail(f, source)

            if med_rel:
                f.write("### 🟡 Medium Relevance (Review for Insights)\n\n")
                for source in med_rel:
                    self._write_source_detail(f, source)

            if low_rel:
                f.write("### 🟢 Low Relevance (Archive for Reference)\n\n")
                for source in low_rel:
                    self._write_source_detail(f, source)

            # Recommended actions
            f.write("\n## Recommended Next Actions\n\n")

            if high_rel:
                f.write("**Priority 1**: Integrate high-relevance sources\n")
                for source in high_rel:
                    sections = source.get('relevance', {}).get('recommended_sections', [])
                    if sections:
                        f.write(f"- Update {sections[0]} section with findings from '{source.get('title', 'Unknown')}'\n")

            if med_rel:
                f.write("\n**Priority 2**: Review medium-relevance sources for specific insights\n")
                for source in med_rel[:3]:  # Limit to top 3
                    f.write(f"- Scan '{source.get('title', 'Unknown')}' for relevant details\n")

            f.write("\n**After Integration**:\n")
            f.write("1. Update `tasks/context.md` with key discoveries (2-Action Rule)\n")
            f.write("2. Mark completed tasks in `tasks/todo.md`\n")
            f.write("3. Add any new patterns to `tasks/lessons.md`\n")

        print(f"\n✅ Claude suggestions generated: {suggestions_path}")

    def _write_source_detail(self, f, source):
        """Write source details to file"""
        relevance = source.get('relevance', {})

        f.write(f"**{source.get('title', 'Unknown')}**\n")
        f.write(f"- Category: {source.get('category', 'unknown')}\n")
        f.write(f"- Relevance Score: {relevance.get('score', 0)}/10\n")
        f.write(f"- Keywords: {', '.join(relevance.get('matches', []))}\n")

        sections = relevance.get('recommended_sections', [])
        if sections:
            f.write(f"- Suggested Sections: {', '.join(sections)}\n")

        summary = source.get('summary', '')
        if summary:
            f.write(f"- Summary: {summary[:200]}...\n")

        f.write("\n")

    def display_quick_start(self):
        """Display quick start guide for Claude"""
        print("\n" + "=" * 60)
        print("CLAUDE CODE QUICK START")
        print("=" * 60)

        print("\n📋 **Files to Review**:")
        print("   1. tasks/session_ingestion_suggestions.md - Integration recommendations")
        print("   2. tasks/context.md - Current research state")
        print("   3. tasks/todo.md - Active work items")
        print("   4. tasks/lessons.md - Known patterns and fixes")

        print("\n🎯 **Recommended Workflow**:")
        print("   1. Review session_ingestion_suggestions.md for new sources")
        print("   2. Check context.md - Answer 5-question context check")
        print("   3. Scan todo.md - Identify highest priority task")
        print("   4. Check lessons.md - Apply relevant patterns")
        print("   5. Execute task with full context")

        print("\n📁 **Quick Commands**:")
        print("   cat tasks/session_ingestion_suggestions.md")
        print("   cat tasks/context.md")
        print("   cat tasks/todo.md")
        print("   cat tasks/lessons.md")

        print("\n🔗 **Integration Report**:")
        if Path("integration_report.md").exists():
            print("   cat integration_report.md")
        else:
            print("   (No integration report yet)")

        print("\n" + "=" * 60)
        print("Ready for research session! 🚀")
        print("=" * 60 + "\n")

def main():
    """Main entry point for Claude Code session startup"""
    try:
        bridge = ClaudeSessionBridge()

        # Run ingestion
        bridge.run_session_ingestion()

        # Check for new sources and generate suggestions
        # Note: SessionIngestion already processed sources, we need to read results
        import json
        if os.path.exists('source_database.json'):
            with open('source_database.json', 'r') as f:
                db = json.load(f)
                new_sources = [
                    src for src in db.get('sources', {}).values()
                    if src.get('status') == 'new'
                ]
                bridge.generate_claude_suggestions(new_sources)
        else:
            bridge.generate_claude_suggestions([])

        # Display quick start guide
        bridge.display_quick_start()

    except Exception as e:
        print(f"\n❌ Error during session startup: {e}")
        print("Please check system configuration and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
