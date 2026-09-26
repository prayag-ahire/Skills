import sys

def fix_svg(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    out_lines = []
    found = False
    for i in range(len(lines)):
        if "<!-- STICKY HEADER -->" in lines[i]:
            # The previous line is </g>
            # The line before that is </g>
            # The line before that is </g>
            
            # Let's search backward and remove the first </g> we find before STICKY HEADER
            idx = len(out_lines) - 1
            while idx >= 0:
                if out_lines[idx].strip() == '</g>':
                    print(f"Removing </g> before STICKY HEADER at line {idx} in {filepath}")
                    out_lines.pop(idx)
                    found = True
                    break
                idx -= 1
        out_lines.append(lines[i])

    if found:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(out_lines)

fix_svg('../screen/src/v1/worker.svg')
