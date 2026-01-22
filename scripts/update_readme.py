#!/usr/bin/env python3
"""
Automatically updates the README.md with a table of all analyzed interviews.
"""

import os
from pathlib import Path

WORKS_DIR = Path(__file__).parent.parent / "works"
README_PATH = Path(__file__).parent.parent / "README.md"

TABLE_START_MARKER = "<!-- INTERVIEWS_TABLE_START -->"
TABLE_END_MARKER = "<!-- INTERVIEWS_TABLE_END -->"


def folder_name_to_title(folder_name: str) -> str:
    """Convert a folder name like 'michael-levin-tim-ferriss' to 'Michael Levin Tim Ferriss'."""
    return folder_name.replace("-", " ").title()


def parse_readme_txt(readme_path: Path) -> dict:
    """Parse a readme.txt file and return metadata dict."""
    metadata = {}
    with open(readme_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if ": " in line:
                key, value = line.split(": ", 1)
                metadata[key] = value
            elif line.startswith("https://www.youtube.com/") or line.startswith("http://www.youtube.com/"):
                # Handle bare YouTube URLs
                metadata["YouTube URL"] = line
    return metadata


def get_interviews() -> list[dict]:
    """Scan works directory and collect interview data."""
    interviews = []

    for work_dir in sorted(WORKS_DIR.iterdir()):
        if not work_dir.is_dir():
            continue

        readme_txt = work_dir / "readme.txt"
        if not readme_txt.exists():
            continue

        metadata = parse_readme_txt(readme_txt)

        title = metadata.get("Title") or folder_name_to_title(work_dir.name)
        youtube_url = metadata.get("YouTube URL", "")

        analysis_compressed = work_dir / "analysis_compressed.md"
        analysis = work_dir / "analysis.md"

        interviews.append({
            "title": title,
            "youtube_url": youtube_url,
            "folder": work_dir.name,
            "has_analysis_compressed": analysis_compressed.exists(),
            "has_analysis": analysis.exists(),
        })

    return interviews


def generate_table(interviews: list[dict]) -> str:
    """Generate markdown table from interview data."""
    lines = [
        "| Interview | YouTube | Core Ideas | Full Analysis |",
        "|-----------|---------|------------|---------------|",
    ]

    for interview in interviews:
        title = f"**{interview['title']}**"

        if interview["youtube_url"]:
            youtube = f"[Link]({interview['youtube_url']})"
        else:
            youtube = "-"

        folder = interview["folder"]

        if interview["has_analysis_compressed"]:
            core_ideas = f"[View](works/{folder}/analysis_compressed.md)"
        else:
            core_ideas = "-"

        if interview["has_analysis"]:
            full_analysis = f"[View](works/{folder}/analysis.md)"
        else:
            full_analysis = "-"

        lines.append(f"| {title} | {youtube} | {core_ideas} | {full_analysis} |")

    return "\n".join(lines)


def update_readme(table: str) -> None:
    """Update README.md with the generated table."""
    with open(README_PATH, "r") as f:
        content = f.read()

    if TABLE_START_MARKER in content and TABLE_END_MARKER in content:
        # Replace existing table
        start_idx = content.index(TABLE_START_MARKER)
        end_idx = content.index(TABLE_END_MARKER) + len(TABLE_END_MARKER)
        new_content = (
            content[:start_idx]
            + TABLE_START_MARKER
            + "\n\n"
            + table
            + "\n\n"
            + TABLE_END_MARKER
            + content[end_idx:]
        )
    else:
        # Append table section
        new_content = (
            content.rstrip()
            + "\n\n## Interviews\n\n"
            + TABLE_START_MARKER
            + "\n\n"
            + table
            + "\n\n"
            + TABLE_END_MARKER
            + "\n"
        )

    with open(README_PATH, "w") as f:
        f.write(new_content)


def main():
    interviews = get_interviews()
    table = generate_table(interviews)
    update_readme(table)
    print(f"Updated README.md with {len(interviews)} interviews")


if __name__ == "__main__":
    main()
