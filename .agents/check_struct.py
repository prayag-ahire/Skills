def check_structure(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"\n=== {filepath} ===")
    for i, line in enumerate(lines):
        stripped = line.strip()
        if any(k in stripped for k in ['clip-path', 'screen-clip', 'scrollable-content', 'sticky', 'Bottom Nav', 'Lightbox', 'End Screen']):
            print(f"L{i+1}: {stripped[:120]}")

check_structure('../screen/src/v2/workerlist.svg')
