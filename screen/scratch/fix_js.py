import re

with open('proworker.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken script tag
html = html.replace('  <script>\n\n\n  <script>', '  <script>')
html = html.replace('</script>\n</script>', '</script>')
html = html.replace('</div>\n    </div>\n  </div>\n  <script>', '</div>\n  <script>')


# List of IDs used in the JS
js_ids = [
    'follow-btn', 'menu-btn', 'dropdown-menu', 'tab-content-photos',
    'tab-content-reviews', 'tab-content-availability', 'tab-content-about',
    'lightbox', 'lightbox-img', 'lightbox-close', 'review-stars-container',
    'review-input-group', 'submit-review-btn', 'new-review-block', 'existing-reviews',
    'scrollable-content', 'broadcast-fab', 'broadcast-modal', 'broadcast-dimmer',
    'close-broadcast-btn', 'broadcast-sheet', 'broadcast-scroll-area',
    'broadcast-footer', 'broadcast-submit-btn', 'broadcast-radar-state',
    'broadcast-success-state', 'view-assigned-worker-btn'
]

# We need to suffix these IDs in the OLD flow.
# The Old flow is inside <div class="flow-title">V1.0 - Original Flow</div>
v1_match = re.search(r'<div class="flow-title">V1\.0 - Original Flow</div>.*?(?=<div class="flow-row">)', html, re.DOTALL)
if v1_match:
    v1_html = v1_match.group(0)
    for i in js_ids:
        # replace id="something" with id="something-old"
        v1_html = v1_html.replace(f'id="{i}"', f'id="{i}-old"')
    
    html = html[:v1_match.start()] + v1_html + html[v1_match.end():]

# Now let's extract the JS block
js_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if js_match:
    js_code = js_match.group(1)
    
    # Create the old JS version
    old_js_code = js_code
    for i in js_ids:
        old_js_code = old_js_code.replace(f"getElementById('{i}')", f"getElementById('{i}-old')")
    
    # We also need to change 'worker-profile-svg' to 'old-worker-profile-svg'
    old_js_code = old_js_code.replace("getElementById('worker-profile-svg')", "getElementById('old-worker-profile-svg')")
    # Same for home-screen-svg
    old_js_code = old_js_code.replace("getElementById('home-screen-svg')", "getElementById('old-home-screen-svg')")

    # Combine them
    combined_js = f"""
    // --- V2 (NEW) JS LOGIC ---
    {js_code}

    // --- V1 (OLD) JS LOGIC ---
    {old_js_code}
    """
    
    html = html[:js_match.start()] + "<script>" + combined_js + "</script>" + html[js_match.end():]

with open('proworker.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("JS Fixed")
