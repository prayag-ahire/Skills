with open('proworker.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Wrap the duplicated JS blocks in IIFEs to prevent variable redeclaration errors
html = html.replace('// --- V2 (NEW) JS LOGIC ---', '(() => {\n// --- V2 (NEW) JS LOGIC ---')
html = html.replace('// --- V1 (OLD) JS LOGIC ---', '})();\n(() => {\n// --- V1 (OLD) JS LOGIC ---')
html = html.replace('</script>', '})();\n</script>')

# Also wait, the original JS was: document.addEventListener('DOMContentLoaded', () => { ... });
# So the combined string looks like:
# <script>
# (() => {
# document.addEventListener('DOMContentLoaded', () => {
# ...
# });
# })();
# (() => {
# document.addEventListener('DOMContentLoaded', () => {
# ...
# });
# })();
# </script>
# Which is perfectly valid!

with open('proworker.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Scopes fixed")
