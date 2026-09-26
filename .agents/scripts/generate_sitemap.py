import os

def generate_tree(startpath):
    tree_str = "# Project File Map\n\n"
    tree_str += "This is an auto-generated map of the project directory structure to help AI agents locate files.\n\n"
    tree_str += "`\n"
    
    for root, dirs, files in os.walk(startpath):
        # Skip node_modules and .git
        if '.git' in root or 'node_modules' in root:
            continue
            
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree_str += f"{indent}{os.path.basename(root)}/\n"
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            # Skip media and large binary files if needed, but for now include all
            tree_str += f"{subindent}{f}\n"
            
    tree_str += "`\n"
    
    with open(os.path.join(startpath, '.agents', 'PROJECT_SITEMAP.md'), 'w', encoding='utf-8') as f:
        f.write(tree_str)

if __name__ == '__main__':
    # Run from .agents folder, so workspace root is one level up
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    generate_tree(workspace_root)
    print("PROJECT_SITEMAP.md generated successfully in .agents directory.")
