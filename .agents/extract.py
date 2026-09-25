import re
import os

with open('../screen/proworker.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make src dirs
os.makedirs('../screen/src/v1', exist_ok=True)
os.makedirs('../screen/src/v2', exist_ok=True)
os.makedirs('../screen/src/css', exist_ok=True)
os.makedirs('../screen/src/js', exist_ok=True)

# 1. Extract CSS
css_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if css_match:
    with open('../screen/src/css/global.css', 'w', encoding='utf-8') as f:
        f.write(css_match.group(1).strip())
    html = html[:css_match.start(1)] + "<!-- INJECT_CSS -->\n    " + html[css_match.end(1):]

# 2. Extract SVGs (Find all <svg ...> ... </svg>)
svg_matches = list(re.finditer(r'<svg [^>]*>.*?</svg>', html, re.DOTALL))
print(f"Found {len(svg_matches)} SVGs")

# Assuming order: V1 Home, V1 Worker, V2 Home, V2 Worker
for i, m in reversed(list(enumerate(svg_matches))):
    svg_content = m.group(0)
    
    if i == 0:
        path = '../screen/src/v1/home.svg'
        inject_tag = '<!-- INJECT_OLD-HOME-SCREEN-SVG -->'
    elif i == 1:
        path = '../screen/src/v1/worker.svg'
        inject_tag = '<!-- INJECT_OLD-WORKER-PROFILE-SVG -->'
    elif i == 2:
        path = '../screen/src/v2/home.svg'
        inject_tag = '<!-- INJECT_HOME-SCREEN-SVG -->'
    elif i == 3:
        path = '../screen/src/v2/worker.svg'
        inject_tag = '<!-- INJECT_WORKER-PROFILE-SVG -->'

    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
        
    html = html[:m.start()] + inject_tag + html[m.end():]

# 3. Extract JS
js_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if js_match:
    js_content = js_match.group(1)
    if '// --- V1 (OLD) JS LOGIC ---' in js_content:
        parts = js_content.split('// --- V1 (OLD) JS LOGIC ---')
        v2_js = parts[0].strip()
        v1_js = '// --- V1 (OLD) JS LOGIC ---\n' + parts[1].strip()
        
        with open('../screen/src/js/v2.js', 'w', encoding='utf-8') as f:
            f.write(v2_js)
        with open('../screen/src/js/v1.js', 'w', encoding='utf-8') as f:
            f.write(v1_js)
            
        html = html[:js_match.start(1)] + "\n<!-- INJECT_JS_V2 -->\n<!-- INJECT_JS_V1 -->\n  " + html[js_match.end(1):]

# 4. Save Template
with open('../screen/src/index.template.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Extraction successful.")
