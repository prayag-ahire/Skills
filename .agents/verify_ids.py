import re
import os

src_dir = '../screen/src'
all_ids = {}

for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith('.svg'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
            ids = re.findall(r'id=""([^""]+)""', content)
            for id_val in ids:
                if id_val not in all_ids:
                    all_ids[id_val] = []
                all_ids[id_val].append(os.path.basename(path))

# Find any duplicates
dupes = {k: v for k, v in all_ids.items() if len(v) > 1}
if dupes:
    print('DUPLICATE IDs FOUND:')
    for k, v in dupes.items():
        print(f'  {k}: {v}')
else:
    print('All IDs are unique across all SVGs!')
