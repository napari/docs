#!/usr/bin/env python3
"""
Script to parse all release notes and extract highlights for the interactive release browser.
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json

def extract_date_from_release(content: str) -> Optional[datetime]:
    """Extract release date from markdown content."""
    # Look for date patterns in the first few lines
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
                    "%Y-%m-%d",       # 2024-07-11
                ]:
                    try:
                        return datetime.strptime(date_str, fmt)
                    except ValueError:
                        continue
            except:
                pass
    
    return None

def extract_highlights(content: str) -> List[str]:
    """Extract highlights section from markdown content."""
    lines = content.split('\n')
    highlights = []
    in_highlights = False
    in_summary = False
    
    for line in lines:
        if line.strip().lower().startswith('## highlights'):
            in_highlights = True
            continue
        elif line.strip().lower().startswith('### summary'):
            in_summary = True
            continue
        elif in_highlights and line.startswith('## '):
            # End of highlights section
            break
        elif in_highlights and line.strip():
            if line.startswith('- ') or line.startswith('* '):
                # Bullet point highlight
                highlights.append(line.strip()[2:])
            elif line.startswith('### '):
                # Subsection in highlights
                highlights.append(line.strip()[4:])
            elif not line.startswith(' ') and not line.startswith('\t'):
                # Regular paragraph text
                highlights.append(line.strip())
    
    return [h for h in highlights if h and not h.startswith('#')]

def extract_version_from_filename(filename: str) -> str:
    """Extract version number from filename."""
    match = re.search(r'release_(.+)\.md', filename)
    if match:
        return match.group(1).replace('_', '.')
    return filename

def parse_all_releases(release_dir: Path) -> Dict:
    """Parse all release files and extract information."""
    releases = []
    
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
            
            release_info = {
                'version': version,
                'title': title,
                'date': release_date.isoformat() if release_date else None,
                'highlights': highlights,
                'filename': release_file.name
            }
            
            releases.append(release_info)
            
        except Exception as e:
            print(f"Error parsing {release_file}: {e}")
    
    # Sort by version (attempt semantic sorting)
    def version_key(release):
        try:
            parts = [int(x) for x in release['version'].split('.')]
            return tuple(parts)
        except:
            return (0, 0, 0)
    
    releases.sort(key=version_key, reverse=True)
    
    return {
        'releases': releases,
        'generated_at': datetime.now().isoformat(),
        'total_releases': len(releases)
    }

if __name__ == '__main__':
    release_dir = Path(__file__).parent.parent / 'docs' / 'release'
    data = parse_all_releases(release_dir)
    
    # Save to JSON file
    output_file = Path(__file__).parent.parent / 'docs' / '_static' / 'releases_data.json'
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Parsed {data['total_releases']} releases and saved to {output_file}")
    
    # Print some stats
    releases_with_dates = [r for r in data['releases'] if r['date']]
    print(f"Releases with dates: {len(releases_with_dates)}")
    
    total_highlights = sum(len(r['highlights']) for r in data['releases'])
    print(f"Total highlights extracted: {total_highlights}")
