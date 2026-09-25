with open('proworker.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the malformed text node
html = html.replace(
    '<text x="265" y="340" class="font-sans" fill="#2563EB" font-size="14" font-weight="700" text-anchor="middle              <text x="265" y="340" class="font-sans" fill="#2563EB" font-size="14" font-weight="700" text-anchor="middle">₹199</text>',
    '<text x="265" y="340" class="font-sans" fill="#2563EB" font-size="14" font-weight="700" text-anchor="middle">₹199</text>'
)

# Fix the malformed closing tags
html = html.replace(
    '        </g> <!-- End Screen Clip -->\n      </svg>\n    </div>/svg>\n    </div>\n  </div>',
    '        </g> <!-- End Screen Clip -->\n      </svg>\n    </div>\n  </div>'
)

with open('proworker.html', 'w', encoding='utf-8') as f:
    f.write(html)
