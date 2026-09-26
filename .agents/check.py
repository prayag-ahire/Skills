import re

def check_tags(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    stack = []
    for i, line in enumerate(lines):
        for m in re.finditer(r'<g\b[^>]*>|<\/g>', line):
            if m.group(0).startswith('<g'):
                stack.append(i + 1)
            else:
                if not stack:
                    print(f"Unmatched </g> at line {i + 1} in {filepath}")
                else:
                    stack.pop()
    
    if stack:
        print(f"Unmatched <g> started at lines {stack} in {filepath}")
        
check_tags('../screen/src/v1/worker.svg')
