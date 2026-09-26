import re
import os

js_files = ['../screen/src/js/v1.js', '../screen/src/js/v2.js']
svg_dir = '../screen/src'

# Collect all SVG IDs
all_svg_ids = set()
for root, dirs, files in os.walk(svg_dir):
    for f in files:
        if f.endswith('.svg'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as fh:
                content = fh.read()
            ids = re.findall(r'id=""([^""]+)""', content)
            all_svg_ids.update(ids)

# Check JS references
print('Checking JS getElementById references...')
issues = []
for js_file in js_files:
    with open(js_file, 'r', encoding='utf-8') as fh:
        content = fh.read()
    refs = re.findall(r"getElementById\('([^']+)'\)", content)
    for ref in refs:
        if ref not in all_svg_ids:
            issues.append(f'{os.path.basename(js_file)}: references ID not found in any SVG -> {ref}')

if issues:
    print('BROKEN REFERENCES:')
    for i in issues:
        print(f'  {i}')
else:
    print('All JS getElementById references are valid!')
