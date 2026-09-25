import os

def build_html():
    with open('../screen/src/index.template.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Inject CSS
    with open('../screen/src/css/global.css', 'r', encoding='utf-8') as f:
        html = html.replace('<!-- INJECT_CSS -->', f.read())

    # Inject V1
    with open('../screen/src/v1/home.svg', 'r', encoding='utf-8') as f:
        html = html.replace('<!-- INJECT_OLD-HOME-SCREEN-SVG -->', f.read())
    with open('../screen/src/v1/worker.svg', 'r', encoding='utf-8') as f:
        html = html.replace('<!-- INJECT_OLD-WORKER-PROFILE-SVG -->', f.read())

    # Inject V2
    with open('../screen/src/v2/home.svg', 'r', encoding='utf-8') as f:
        html = html.replace('<!-- INJECT_HOME-SCREEN-SVG -->', f.read())
    with open('../screen/src/v2/worker.svg', 'r', encoding='utf-8') as f:
        html = html.replace('<!-- INJECT_WORKER-PROFILE-SVG -->', f.read())

    # Inject JS
    with open('../screen/src/js/v2.js', 'r', encoding='utf-8') as f:
        html = html.replace('<!-- INJECT_JS_V2 -->', f.read())
    with open('../screen/src/js/v1.js', 'r', encoding='utf-8') as f:
        html = html.replace('<!-- INJECT_JS_V1 -->', f.read())

    with open('../screen/proworker.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Build successful. proworker.html updated.")

if __name__ == "__main__":
    build_html()
