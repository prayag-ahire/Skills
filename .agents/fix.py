import sys

def fix_svg(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    out_lines = []
    found = False
    for i in range(len(lines)):
        if "<!-- Scrollable Body -->" in lines[i]:
            # The previous line might be empty
            # The one before might be </g>
            # Let's just find the first </g> before "Scrollable Body" that is indented by 10 spaces and delete it
            idx = len(out_lines) - 1
            while idx >= 0 and out_lines[idx].strip() == '':
                idx -= 1
            if idx >= 0 and out_lines[idx].strip() == '</g>':
                print(f"Removing premature </g> at line {idx} in {filepath}")
                out_lines.pop(idx)
                found = True
        out_lines.append(lines[i])

    if found:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(out_lines)

fix_svg('../screen/src/v1/worker.svg')
fix_svg('../screen/src/v2/worker.svg')
