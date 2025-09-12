"""Generate napari "What's New" documentation from release notes.

This module provides functionality to automatically generate a "What's New" page
that summarizes recent napari releases organized by time periods. It extracts
highlights from individual release notes and creates a time-organized overview
to help users catch up on features they might have missed.

Generated Content
-----------------
- Markdown documentation file at `docs/release/whats-new.md`
- Time-organized sections (recent, earlier this year, older releases)
- Dropdown sections for each release with highlights
- Direct links to full release notes

The documentation includes:
- Recent releases (last 3 months) with full highlights
- Earlier releases (3-6 months ago) in dropdown format
- Older releases (6-12 months ago) in dropdown format
- Historical releases as a simple list with previews

Usage
-----
From command line:
    # Generate full documentation
    python update_release_docs.py

    # Generate only stub documentation (for quick builds)
    python update_release_docs.py --stubs

From another script:
    from update_release_docs import main
    main(stubs=False)  # Generate full documentation

Key Functions
-------------
extract_date_from_release(content)
    Parses release date from markdown headers in various formats.

extract_highlights(content)
    Extracts the "## Highlights" section from release markdown.

extract_version_from_filename(filename)
    Converts filename like "release_0_6_4.md" to version "0.6.4".

create_whats_new_docs(releases)
    Generates MyST markdown using Jinja2 template with time-based groupings.

main(stubs=False)
    Main entry point that coordinates the documentation generation.

Notes
-----
- Only includes releases that have both dates and highlights
- Sorts releases by date (newest first)
- Uses MyST dropdown syntax for organized presentation
- Preserves original highlights formatting from release notes
"""

import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

from jinja2 import Template

# Path constants
DOCS = Path(__file__).parent.parent.absolute()
RELEASE_PATH = DOCS / "release"

# MyST template for the release notes index page
RELEASE_INDEX_TEMPLATE = """(release-notes)=

# Release Notes

Each section shows the highlights from recent releases. Click on the version links to view the complete release notes.

*Last updated: {{ last_updated }}*

{% if recent %}
## Recent Releases (Last 3 Months)

Latest features and improvements:

{{ recent_content }}
{% endif %}
{% if earlier_this_year %}
## Releases from 3-6 Months Ago

{{ earlier_content }}
{% endif %}
{% if this_year %}
## Releases from 6-12 Months Ago

{{ this_year_content }}
{% endif %}
{% if older %}
## Older Releases

{{ older_content }}
{% endif %}
"""


def extract_date_from_release(content: str) -> Optional[datetime]:
    """Extract release date from markdown content."""
    lines = content.split('\n')[:10]
    
    for line in lines:
        # Pattern for dates like "*Thursday, Jul 11, 2024*"
        date_match = re.search(r'\*([^*]+)\*', line)
        if date_match:
            date_str = date_match.group(1).strip()
            try:
                # Try different date formats
                for fmt in [
                    "%A, %b %d, %Y",  # Thursday, Jul 11, 2024
                    "%a, %b %d, %Y",  # Thu, Jul 11, 2024
                    "%B %d, %Y",      # July 11, 2024
                    "%b %d, %Y",      # Jul 11, 2024
                ]:
                    try:
                        return datetime.strptime(date_str, fmt)
                    except ValueError:
                        continue
            except:
                pass
    
    return None


def extract_highlights(content: str) -> str:
    """Extract highlights section from markdown content, preserving structure."""
    lines = content.split('\n')
    highlights_lines = []
    in_highlights = False
    
    for line in lines:
        if line.strip().lower().startswith('## highlights'):
            in_highlights = True
            continue
        elif in_highlights and line.startswith('## '):
            # End of highlights section
            break
        elif in_highlights:
            # Keep the original formatting including headers
            highlights_lines.append(line)
    
    # Join back into a single string, preserving original formatting
    return '\n'.join(highlights_lines).strip()


def extract_version_from_filename(filename: str) -> str:
    """Extract version number from filename."""
    match = re.search(r'release_(.+)\.md', filename)
    if match:
        return match.group(1).replace('_', '.')
    return filename


def generate_release_dropdowns(releases: List[Dict]) -> str:
    """Generate dropdown sections for releases."""  
    content = ""
    
    for release in releases[:6]:  # Max 6 releases to avoid clutter
        date_str = release['date'].strftime("%B %Y")
        
        # Use dropdown/details instead of tabs
        content += f"````{{dropdown}} {release['title']} ({date_str})\n"
        content += ":open:\n\n"
        
        # Add the full highlights content
        if release['highlights']:
            highlights = release['highlights'].strip()
            content += f"{highlights}\n\n"
        
        content += f"[View full release notes →]({release['filename']})\n\n"
        content += "````\n\n"
    
    return content


def generate_release_list(releases: List[Dict]) -> str:
    """Generate simple list for older releases."""
    content = ""
    
    for release in releases:
        if release['date']:
            date_str = release['date'].strftime("%B %Y")
            content += f"- **[{release['title']}]({release['filename']})** ({date_str})"
        else:
            # For releases without dates, just show the title
            content += f"- **[{release['title']}]({release['filename']})**"
        
        if release['highlights']:
            # Show first few lines as preview
            first_lines = release['highlights'].split('\n')[:2]
            preview = ' '.join(first_lines).strip()
            if len(preview) > 150:
                preview = preview[:150] + "..."
            if preview:
                content += f" - {preview}"
        
        content += "\n"
    
    return content


def parse_releases() -> List[Dict]:
    """Parse all release files and extract information."""
    releases_with_dates = []
    releases_without_dates = []
    
    # Parse all release files
    for release_file in RELEASE_PATH.glob('release_*.md'):
        with open(release_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        version = extract_version_from_filename(release_file.name)
        release_date = extract_date_from_release(content)
        highlights = extract_highlights(content)
        
        # Extract title
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else f"napari {version}"
        
        if highlights:  # Include releases with highlights (even without dates)
            release_info = {
                'version': version,
                'title': title,
                'date': release_date,
                'highlights': highlights,  # Full highlights section as-is
                'filename': release_file.stem,
            }
            
            if release_date:
                releases_with_dates.append(release_info)
            else:
                releases_without_dates.append(release_info)

    # Sort releases with dates by date (newest first)
    releases_with_dates.sort(key=lambda x: x['date'], reverse=True)
    
    # Sort releases without dates by version (attempt semantic sorting, newest first)
    def version_key(release):
        try:
            parts = [int(x) for x in release['version'].split('.')]
            # Pad to ensure consistent comparison
            while len(parts) < 3:
                parts.append(0)
            return tuple(parts)
        except:
            return (0, 0, 0)

    releases_without_dates.sort(key=version_key, reverse=True)

    # Return dated releases first, then undated ones
    return releases_with_dates + releases_without_dates


def create_release_index_docs():
    """Create release index docs from release files using a jinja template."""
    
    # Parse all releases
    releases = parse_releases()
    
    # Group releases by time periods
    now = datetime.now()
    three_months_ago = now - timedelta(days=90)
    six_months_ago = now - timedelta(days=180)
    one_year_ago = now - timedelta(days=365)
    
    # Separate releases with and without dates
    dated_releases = [r for r in releases if r['date'] is not None]
    undated_releases = [r for r in releases if r['date'] is None]
    
    # Group dated releases by time periods
    recent = [r for r in dated_releases if r['date'] >= three_months_ago]
    earlier_this_year = [r for r in dated_releases if six_months_ago <= r['date'] < three_months_ago]
    this_year = [r for r in dated_releases if one_year_ago <= r['date'] < six_months_ago]
    older_dated = [r for r in dated_releases if r['date'] < one_year_ago]
    
    # Combine older dated releases with undated releases for the "Older Releases" section
    older = older_dated + undated_releases
    
    # Generate content for each section
    template_vars = {
        'last_updated': now.strftime("%B %d, %Y"),
        'recent': recent,
        'recent_content': generate_release_dropdowns(recent) if recent else "",
        'earlier_this_year': earlier_this_year,
        'earlier_content': generate_release_dropdowns(earlier_this_year) if earlier_this_year else "",
        'this_year': this_year,
        'this_year_content': generate_release_dropdowns(this_year) if this_year else "",
        'older': older,
        'older_content': generate_release_list(older) if older else "",  # Show all older releases
    }
    
    # Generate the page content
    text = Template(RELEASE_INDEX_TEMPLATE).render(**template_vars)
    
    # Write the file
    output_file = RELEASE_PATH / "index.md"
    output_file.write_text(text, encoding='utf-8')


def main(stubs=False):
    """Main entry point for generating release notes documentation."""
    if stubs:
        # Generate stub file
        file_path = RELEASE_PATH / "index.md"
        if not file_path.exists():  # Avoid overwriting existing files
            file_path.write_text(
                "(release-notes)=\n# Release Notes\nThis is a stub. The real file is autogenerated in a full build.",
                encoding="utf-8",
            )
    else:
        create_release_index_docs()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Update release notes index.")
    parser.add_argument(
        "--stubs",
        action="store_true",
        help="Generate stub version of the release notes index.",
    )
    args = parser.parse_args()

    main(stubs=args.stubs)
