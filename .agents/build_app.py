import os

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

def build_app():
    # Load template
    html = read_file('../screen/src/app.template.html')
    
    # Inject CSS
    css = read_file('../screen/src/css/global.css')
    html = html.replace('<!-- INJECT_CSS -->', f'<style>\n{css}\n</style>')
    
    # Inject SVGs for both flows
    svg_splash = read_file('../screen/src/v2/splash.svg')
    svg_v2_home = read_file('../screen/src/v2/home.svg')
    svg_v2_workerlist = read_file('../screen/src/v2/workerlist.svg')
    svg_v2_worker = read_file('../screen/src/v2/worker.svg')
    svg_v1_home = read_file('../screen/src/v1/home.svg')
    svg_v1_workerlist = read_file('../screen/src/v1/workerlist.svg')
    svg_v1_worker = read_file('../screen/src/v1/worker.svg')
    
    html = html.replace('<!-- INJECT_SPLASH_SCREEN -->', svg_splash)
    html = html.replace('<!-- INJECT_V2_HOME_SCREEN -->', svg_v2_home)
    html = html.replace('<!-- INJECT_V2_WORKERLIST_SCREEN -->', svg_v2_workerlist)
    html = html.replace('<!-- INJECT_V2_WORKER_SCREEN -->', svg_v2_worker)
    html = html.replace('<!-- INJECT_V1_HOME_SCREEN -->', svg_v1_home)
    html = html.replace('<!-- INJECT_V1_WORKERLIST_SCREEN -->', svg_v1_workerlist)
    html = html.replace('<!-- INJECT_V1_WORKER_SCREEN -->', svg_v1_worker)
    
    # Inject JS
    js_v2 = read_file('../screen/src/js/v2.js')
    js_v1 = read_file('../screen/src/js/v1.js')
    
    html = html.replace('// INJECT_JS_GLOBAL', f'{js_v2}\n{js_v1}')
    
    # Save final
    with open('../screen/app.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Build successful. app.html generated.")

if __name__ == "__main__":
    build_app()
