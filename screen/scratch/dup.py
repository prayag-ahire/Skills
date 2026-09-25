import re

with open('proworker.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract the Home Screen SVG
home_match = re.search(r'<div class="device-frame">\s*<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 415 852" width="100%" height="100%" role="img" aria-labelledby="title desc">.*?</div>\s*<!-- Worker Profile Screen -->', html, re.DOTALL)
if not home_match:
    print("Could not find home match")
    exit(1)
home_html = html[home_match.start():home_match.end() - len('    <!-- Worker Profile Screen -->')]

# 2. Extract the Worker Profile SVG
worker_match = re.search(r'<!-- Worker Profile Screen -->\s*<div class="device-frame">\s*<svg id="worker-profile-svg".*?</div>\s*<script>', html, re.DOTALL)
if not worker_match:
    print("Could not find worker match")
    exit(1)
worker_html = html[worker_match.start():worker_match.end() - len('    <script>')]

# We need to strip out the Broadcast FAB and Modal from the 'Old' Home Screen
old_home_html = re.sub(r'<!-- Broadcast FAB -->.*?</g>\s*</g>\s*</g>', '', home_html, flags=re.DOTALL)

old_home_html = old_home_html.replace('id="home-screen-svg"', 'id="old-home-screen-svg"')
old_worker_html = worker_html.replace('id="worker-profile-svg"', 'id="old-worker-profile-svg"')

# Assemble Flow 1 (Old Flow)
flow1 = f'''
    <div class="flow-row">
      <div class="flow-title">V1.0 - Original Flow</div>
      {old_home_html}
      {old_worker_html}
    </div>
'''

# Assemble Flow 2 (New Flow - Current HTML)
flow2 = f'''
    <div class="flow-row">
      <div class="flow-title">V2.0 - Broadcast & Trust Badges</div>
      {home_html}
      {worker_html}
    </div>
'''

# Replace the inner canvas with the new rows
body_match = re.search(r'<div class="figma-canvas">\s*<div class="device-frame">', html, re.DOTALL)

new_html = html[:body_match.start() + len('<div class="figma-canvas">')] + flow1 + flow2 + '  </div>\n  <script>\n' + html[worker_match.end() - len('    <script>'):]

with open('proworker.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Done")
