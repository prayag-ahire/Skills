import sys

def fix_svg(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if lines[-2].strip() == '</g>':
        lines.pop(-2)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Fixed {filepath}")

fix_svg('../screen/src/v1/worker.svg')
