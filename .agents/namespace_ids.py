import re, os

# Namespace map: each SVG file gets a unique prefix for all its IDs
files = {
    '../screen/src/v1/home.svg':       'v1h',
    '../screen/src/v1/workerlist.svg': 'v1wl',
    '../screen/src/v1/worker.svg':     'v1w',
    '../screen/src/v2/home.svg':       'v2h',
    '../screen/src/v2/workerlist.svg': 'v2wl',
    '../screen/src/v2/worker.svg':     'v2w',
    '../screen/src/v2/splash.svg':     'v2s',
}

# IDs that are commonly shared across SVGs and need namespacing
shared_ids = [
    'screen-clip', 'screen-clip-2',
    'shadow-resting', 'shadow-resting-2', 'shadow-floating', 'shadow-floating-2',
    'card-shadow', 'device-shadow',
    'avatar-clip', 'avatar-clip-1', 'avatar-clip-2', 'avatar-clip-3',
    'list-avatar-clip',
    'scrollable-content',
]

def namespace_svg(filepath, prefix):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    count = 0
    
    for sid in shared_ids:
        # Replace id="sid" with id="prefix-sid"
        new_def = f'id="{prefix}-{sid}"'
        old_def = f'id="{sid}"'
        if old_def in content:
            content = content.replace(old_def, new_def)
            count += 1
        
        # Replace url(#sid) with url(#prefix-sid)
        new_ref = f'url(#{prefix}-{sid})'
        old_ref = f'url(#{sid})'
        if old_ref in content:
            content = content.replace(old_ref, new_ref)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Namespaced {count} IDs in {os.path.basename(filepath)} with prefix '{prefix}'")
    else:
        print(f"No changes needed in {os.path.basename(filepath)}")

for path, prefix in files.items():
    namespace_svg(path, prefix)
