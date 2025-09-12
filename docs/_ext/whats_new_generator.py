"""
Sphinx extension to automatically generate a "What's New" page from release notes.

This extension scans release files and creates a MyST markdown page with
highlights organized by time periods.
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any

from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)


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


def generate_whats_new_page(app: Sphinx) -> None:
    """Generate the what's new page from release files."""
    
    # Find release directory
    docs_dir = Path(app.srcdir)
    release_dir = docs_dir / "release"
    
    releases = []
    
    # Parse all release files
    for release_file in release_dir.glob('release_*.md'):
        try:
            with open(release_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            version = extract_version_from_filename(release_file.name)
            release_date = extract_date_from_release(content)
            highlights = extract_highlights(content)
            
            # Extract title
            title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else f"napari {version}"
            
            if release_date and highlights:  # Only include releases with dates and highlights
                releases.append({
                    'version': version,
                    'title': title,
                    'date': release_date,
                    'highlights': highlights,  # Full highlights section as-is
                    'filename': release_file.stem,
                })
                
        except Exception as e:
            logger.warning(f"Error parsing {release_file}: {e}")
    
    # Sort by date (newest first)
    releases.sort(key=lambda x: x['date'], reverse=True)
    
    # Generate MyST content
    content = generate_myst_content(releases)
    
    # Write to release/whats-new.md
    output_file = docs_dir / "release" / "whats-new.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    logger.info(f"Generated what's new page with {len(releases)} releases")


def generate_myst_content(releases: List[Dict]) -> str:
    """Generate MyST markdown content from releases."""
    
    now = datetime.now()
    three_months_ago = now - timedelta(days=90)
    six_months_ago = now - timedelta(days=180)
    one_year_ago = now - timedelta(days=365)
    
    # Group releases by time periods
    recent = [r for r in releases if r['date'] >= three_months_ago]
    earlier_this_year = [r for r in releases if six_months_ago <= r['date'] < three_months_ago]
    this_year = [r for r in releases if one_year_ago <= r['date'] < six_months_ago]
    older = [r for r in releases if r['date'] < one_year_ago]
    
    content = f"""(whats-new)=

# What's New

```{{admonition}} How to use this page
:class: tip

- Browse releases organized by time periods below
- Each section shows highlights from recent releases
- Click on version links to view complete release notes
```

*Last updated: {now.strftime("%B %d, %Y")}*

"""

    if recent:
        content += "## Recent Releases (Last 3 Months)\n\n"
        content += "Latest features and improvements:\n\n"
        content += generate_release_tabs(recent)
        content += "\n\n"
    
    if earlier_this_year:
        content += "## Earlier This Year (3-6 Months Ago)\n\n"
        content += generate_release_tabs(earlier_this_year)
        content += "\n\n"
    
    if this_year:
        content += "## Earlier This Year (6-12 Months Ago)\n\n"
        content += generate_release_tabs(this_year)
        content += "\n\n"
    
    if older:
        content += "## Older Releases\n\n"
        content += "Major releases from the past:\n\n"
        content += generate_release_list(older[:10])  # Show last 10 older releases
        content += "\n\n"

    return content


def generate_release_tabs(releases: List[Dict]) -> str:
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
        date_str = release['date'].strftime("%B %Y")
        content += f"- **[{release['title']}]({release['filename']})** ({date_str})"
        
        if release['highlights']:
            # Show first few lines as preview
            first_lines = release['highlights'].split('\n')[:2]
            preview = ' '.join(first_lines).strip()
            if len(preview) > 100:
                preview = preview[:100] + "..."
            if preview:
                content += f" - {preview}"
        
        content += "\n"
    
    return content


def setup(app: Sphinx) -> Dict[str, Any]:
    """Set up the Sphinx extension."""
    
    # Connect to the build process
    app.connect('builder-inited', generate_whats_new_page)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
