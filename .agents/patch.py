import re

with open('../screen/src/v1/workerlist.svg', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Status Bar
status_bar_v2 = '''      <!-- Status Bar -->
      <g transform="translate(0, 0)">
        <text x="32" y="32" font-family="-apple-system, sans-serif" fill="#111827" font-size="15" font-weight="600" text-anchor="middle">14:47</text>
        <rect x="126" y="11" width="123" height="35" rx="17.5" fill="#000000" />
        <g transform="translate(290, 17)" fill="#111827">
          <g transform="translate(0, 0)"><rect x="0" y="8" width="3" height="4" rx="1" /><rect x="4" y="6" width="3" height="6" rx="1" /><rect x="8" y="4" width="3" height="8" rx="1" /><rect x="12" y="2" width="3" height="10" rx="1" /></g>
          <g transform="translate(20, 0)"><path d="M8 12.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z" /><path d="M3.5 8C6.1 5.4 9.9 5.4 12.5 8l-1.5 1.5C9.4 7.9 6.6 7.9 5 9.5L3.5 8z" /><path d="M0.5 5C4.7 1.2 11.3 1.2 15.5 5l-1.5 1.5c-3.4-3-8.6-3-12 0L0.5 5z" /></g>
          <g transform="translate(42, 1)"><rect x="0" y="0" width="22" height="11" rx="3.5" fill="none" stroke="#111827" stroke-width="1.2" /><rect x="2" y="2" width="15" height="7" rx="2" /><path d="M23.5 3.5v4" stroke="#111827" stroke-width="1.5" stroke-linecap="round" /></g>
        </g>
      </g>'''

content = re.sub(r'<!-- Status Bar -->.*?<!-- Header:', status_bar_v2 + '\n\n      <!-- Header:', content, flags=re.DOTALL)


# 2. Replace Bottom Navigation
bottom_nav_v2 = '''    <!-- Bottom Tab Bar -->
    <g transform="translate(20, 748)">
      <rect x="0" y="0" width="375" height="84" fill="#FFFFFF" />
      <line x1="0" y1="0" x2="375" y2="0" stroke="#E7E5DF" stroke-width="1" />
      <g transform="translate(72, 14)">
        <use href="#icon-home" x="0" y="0" width="24" height="24" stroke="#3B82F6" stroke-width="2.5" />
        <text x="12" y="36" font-family="-apple-system, sans-serif" fill="#2563EB" font-size="11" font-weight="600" text-anchor="middle">Home</text>
      </g>
      <g transform="translate(175.5, 14)">
        <use href="#icon-store" x="0" y="0" width="24" height="24" fill="none" stroke="#64748B" stroke-width="2" />
        <text x="12" y="36" font-family="-apple-system, sans-serif" fill="#64748B" font-size="11" font-weight="500" text-anchor="middle">Store</text>
      </g>
      <g transform="translate(279, 14)">
        <use href="#icon-user" x="0" y="0" width="24" height="24" fill="none" stroke="#64748B" stroke-width="2" />
        <text x="12" y="36" font-family="-apple-system, sans-serif" fill="#64748B" font-size="11" font-weight="500" text-anchor="middle">Profile</text>
      </g>
      <rect x="127" y="70" width="120" height="5" rx="2.5" fill="#1A1A18" />
    </g>'''

content = re.sub(r'<!-- Bottom Navigation -->.*?</svg>', bottom_nav_v2 + '\n  </g>\n</svg>', content, flags=re.DOTALL)

with open('../screen/src/v1/workerlist.svg', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied to v1/workerlist.svg")
