#!/usr/bin/env python3
import re

# Read the original file
with open('/workspaces/penance/docs/index.html', 'r') as f:
    content = f.read()

# Read the replacement timeline
with open('/workspaces/penance/tools/timeline-replacement.txt', 'r') as f:
    new_timeline = f.read()

# Find and replace the timeline section
pattern = r'(<div class="timeline">.*?</div>\s*</div>\s*</div>\s*</section>)'
match = re.search(pattern, content, re.DOTALL)

if match:
    # Find the start and end of the timeline div
    timeline_start = content.find('<div class="timeline">')
    timeline_end = content.find('</div>', content.find('</div>', content.find('</div>', timeline_start) + 1) + 1)

    # Replace
    new_content = content[:timeline_start] + new_timeline.strip() + content[timeline_end + 6:]

    # Write back
    with open('/workspaces/penance/docs/index.html', 'w') as f:
        f.write(new_content)

    print("Timeline updated successfully!")
else:
    print("Could not find timeline section")
