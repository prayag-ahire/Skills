import re

with open('proworker.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the NEW worker profile
match = re.search(r'<div class="flow-title">V2\.0 - Broadcast & Trust Badges</div>.*?<svg id="worker-profile-svg"', html, re.DOTALL)
if match:
    start_idx = match.end() - len('<svg id="worker-profile-svg"')
    
    # 1. Add Trust Badge to Name
    new_html = html[:start_idx] + html[start_idx:].replace(
        '<text x="16" y="82" class="font-sans" fill="#111827" font-size="24" font-weight="700">Prayag ahire</text>',
        '<text x="16" y="82" class="font-sans" fill="#111827" font-size="24" font-weight="700">Prayag ahire</text>\n          <g transform="translate(160, 64)">\n            <circle cx="10" cy="10" r="10" fill="#10B981" />\n            <path d="M5 10 l3 3 l7 -7" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />\n          </g>\n          <text x="185" y=\"78\" class=\"font-sans\" fill=\"#10B981\" font-size=\"13\" font-weight=\"600\">ID Verified</text>'
    )
    
    # 2. Add Completed Tasks
    new_html = new_html[:start_idx] + new_html[start_idx:].replace(
        '<text x="54" y="106" class="font-sans" fill="#111827" font-size="14" font-weight="600">3.5</text>\n             <text x="80" y="106" class="font-sans" fill="#6B7280" font-size="14">(2 reviews)</text>',
        '<text x="54" y="106" class="font-sans" fill="#111827" font-size="14" font-weight="600">3.5</text>\n             <text x="80" y="106" class="font-sans" fill="#6B7280" font-size="14">(2 reviews)  ·  150+ Jobs Done</text>'
    )
    
    # 3. Add Transparent Pricing to Hero
    new_html = new_html[:start_idx] + new_html[start_idx:].replace(
        '<text x="16" y="106" class="font-sans text-secondary" font-size="15">Plumber</text>',
        '<text x="16" y="106" class="font-sans text-secondary" font-size="15">Plumber</text>\n             <rect x="230" y="90" width=\"95\" height=\"24\" rx=\"12\" fill=\"#FEF3C7\" />\n             <text x=\"240\" y=\"107\" class=\"font-sans\" fill=\"#D97706\" font-size=\"12\" font-weight=\"600\">₹399 / visit</text>'
    )

    # 4. Add Sticky CTA Footer to the Worker Profile
    footer_svg = '''
        <!-- Sticky CTA Footer -->
        <g transform="translate(0, 724)" id="sticky-footer-cta">
          <rect x="0" y="0" width="375" height="88" fill="#FFFFFF" />
          <line x1="0" y1="0" x2="375" y2="0" stroke="#E5E7EB" stroke-width="1" />
          <rect x="24" y="16" width="327" height="56" rx="28" fill="#111827" />
          <text x="187.5" y="50" class="font-sans" fill="#FFFFFF" font-size="16" font-weight="700" text-anchor="middle">Call Prayag Ahire</text>
        </g>
    '''
    
    # We find the closing </g> before </svg> in the new_html (Worker Profile)
    worker_end_match = re.search(r'</g>\s*</svg>', new_html[start_idx:])
    if worker_end_match:
        insert_pos = start_idx + worker_end_match.start()
        new_html = new_html[:insert_pos] + footer_svg + '\n' + new_html[insert_pos:]
    
    with open('proworker.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Patched")
else:
    print("Not found")
