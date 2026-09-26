import re
import os

svg_dir = '../screen/src'
all_svg_ids = set()
for root, dirs, files in os.walk(svg_dir):
    for f in files:
        if f.endswith('.svg'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as fh:
                content = fh.read()
            # Use single quotes in regex  
            ids = re.findall(r"id=[\"']([^\"']+)[\"']", content)
            all_svg_ids.update(ids)

# Print all IDs containing 'worker' or 'plumber' or 'scroll' or 'lightbox'
print('Relevant SVG IDs:')
for sid in sorted(all_svg_ids):
    if any(k in sid.lower() for k in ['worker', 'plumb', 'scroll', 'lightbox', 'back', 'follow', 'tab-content', 'broadcast']):
        print(f'  {sid}')
