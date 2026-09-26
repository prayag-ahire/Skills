"""
ProWorker SVG/JS Health Checker
Run from .agents/ directory: python check.py

Catches bugs BEFORE build:
  1. Duplicate IDs across all SVG files (causes wrong clip resolution in shared DOM)
  2. Unscoped document.querySelector in JS (hits wrong screen in canvas mode)
  3. clipPathUnits="objectBoundingBox" on avatar clips (renders invisible)
  4. Elements with y < 20 directly inside a clip group (bleeds over bezel)
  5. Unbalanced <g> / </g> tags in SVG files
  6. clipPath IDs without a namespace prefix (e.g. bare "p1-clip" instead of "v2w-p1-clip")
  7. filter/linearGradient/mask IDs without a namespace prefix
"""

import re, os, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'screen', 'src')

SVG_FILES = {
    'v1/home':       os.path.join(BASE, 'v1', 'home.svg'),
    'v1/workerlist': os.path.join(BASE, 'v1', 'workerlist.svg'),
    'v1/worker':     os.path.join(BASE, 'v1', 'worker.svg'),
    'v2/splash':     os.path.join(BASE, 'v2', 'splash.svg'),
    'v2/home':       os.path.join(BASE, 'v2', 'home.svg'),
    'v2/workerlist': os.path.join(BASE, 'v2', 'workerlist.svg'),
    'v2/worker':     os.path.join(BASE, 'v2', 'worker.svg'),
}

JS_FILES = {
    'js/v1': os.path.join(BASE, 'js', 'v1.js'),
    'js/v2': os.path.join(BASE, 'js', 'v2.js'),
}

errors = []
warnings = []

def err(file, line, msg):
    errors.append(f"  [ERR] [{file}] line {line}: {msg}")

def warn(file, line, msg):
    warnings.append(f"  [WARN] [{file}] line {line}: {msg}")

# ─────────────────────────────────────────────
# CHECK 1 & 6 & 7: Duplicate + un-namespaced IDs
# ─────────────────────────────────────────────
all_ids = {}  # id_value -> list of files it appears in

# Known safe bare IDs (intentionally shared / JS targets)
ALLOWED_BARE_IDS = {
    # navigation targets
    'screen-off', 'screen-splash',
    'screen-v1-home', 'screen-v1-workerlist', 'screen-v1-worker',
    'screen-v2-home', 'screen-v2-workerlist', 'screen-v2-worker',
    # v2 worker interactive elements
    'worker-profile-svg', 'v2w-scrollable-content',
    'follow-btn', 'menu-btn', 'back-btn-worker', 'back-btn-workerlist',
    'dropdown-menu', 'share-btn', 'report-btn',
    'tab-content-photos', 'tab-content-reviews',
    'tab-content-availability', 'tab-content-about',
    'review-stars-container', 'review-input-group', 'submit-review-btn',
    'new-review-block', 'existing-reviews', 'new-review-stars',
    'lightbox', 'lightbox-img', 'lightbox-close',
    'sticky-header', 'sticky-footer-cta',
    'broadcast-fab', 'broadcast-modal', 'broadcast-dimmer',
    'broadcast-sheet', 'broadcast-scroll-area', 'broadcast-footer',
    'broadcast-submit-btn', 'broadcast-radar-state', 'broadcast-success-state',
    'view-assigned-worker-btn', 'search-bar-btn', 'close-broadcast-btn',
    # v1 worker interactive elements (suffixed -old)
    'old-worker-profile-svg', 'scrollable-content-old',
    'follow-btn-old', 'menu-btn-old', 'back-btn-worker-old',
    'dropdown-menu-old', 'tab-content-photos-old', 'tab-content-reviews-old',
    'tab-content-availability-old', 'tab-content-about-old',
    'review-stars-container-old', 'review-input-group-old', 'submit-review-btn-old',
    'new-review-block-old', 'existing-reviews-old',
    'lightbox-old', 'lightbox-img-old', 'lightbox-close-old',
    'sticky-header-old',
    'broadcast-fab-old', 'broadcast-modal-old', 'broadcast-dimmer-old',
    'broadcast-sheet-old', 'broadcast-scroll-area-old', 'broadcast-footer-old',
    'broadcast-submit-btn-old', 'broadcast-radar-state-old',
    'broadcast-success-state-old', 'view-assigned-worker-btn-old',
    # workerlist
    'workerlist-card-1', 'workerlist-card-1-old',
    'scrollable-content-workerlist',
    'back-btn-workerlist',
    # home
    'plumber-category-btn', 'plumber-category-btn-old',
    'popular-plumber-card', 'popular-plumber-card-old',
}

# IDs that MUST be namespaced (defs elements)
DEFS_TYPES = ('clipPath', 'filter', 'linearGradient', 'radialGradient', 'mask', 'pattern', 'symbol', 'marker')

for name, path in SVG_FILES.items():
    if not os.path.exists(path):
        warn(name, 0, f"File not found: {path}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        for m in re.finditer(r'\bid="([^"]+)"', line):
            id_val = m.group(1)
            all_ids.setdefault(id_val, []).append((name, i))

        # Check 6 & 7: defs elements without namespace prefix
        for dtype in DEFS_TYPES:
            if f'<{dtype}' in line:
                m = re.search(r'id="([^"]+)"', line)
                if m:
                    id_val = m.group(1)
                    # Should start with a known screen prefix
                    prefixes = ('v1h-','v2h-','v1wl-','v2wl-','v1w-','v2w-','v2s-')
                    if not any(id_val.startswith(p) for p in prefixes):
                        warn(name, i, f'<{dtype}> id="{id_val}" has no namespace prefix '
                             f'(expected one of: {", ".join(prefixes)}). '
                             f'Will collide in shared DOM.')

# Report duplicate IDs
for id_val, locations in all_ids.items():
    if len(locations) > 1:
        files = ', '.join(f"{loc[0]}:L{loc[1]}" for loc in locations)
        err(locations[0][0], locations[0][1],
            f'Duplicate id="{id_val}" found in multiple files: {files}')

# ─────────────────────────────────────────────
# CHECK 2: Unscoped document.querySelector in JS
# ─────────────────────────────────────────────
for name, path in JS_FILES.items():
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        # Flag document.querySelector that's NOT chained off a scoped element
        if 'document.querySelector(' in line and 'getElementById' not in line:
            err(name, i,
                f'Unscoped document.querySelector() — will hit the wrong screen in canvas mode. '
                f'Scope it off getElementById("your-svg-root").querySelector(...) instead.')

# ─────────────────────────────────────────────
# CHECK 3: clipPathUnits="objectBoundingBox"
# ─────────────────────────────────────────────
for name, path in SVG_FILES.items():
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if 'clipPathUnits="objectBoundingBox"' in line:
            err(name, i,
                'clipPathUnits="objectBoundingBox" makes image clips render invisibly when '
                'the image is translated. Wrap clipPath + image in a <g transform="..."> '
                'and use userSpaceOnUse coordinates (x=0,y=0 relative to the group).')

# ─────────────────────────────────────────────
# CHECK 4: Elements with y < 20 inside clip group
# ─────────────────────────────────────────────
for name, path in SVG_FILES.items():
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()

    inside_clip = False
    inside_defs = False
    for i, line in enumerate(lines, 1):
        if '<defs' in line: inside_defs = True
        if '</defs' in line: inside_defs = False
        if inside_defs: continue

        if 'clip-path=' in line and 'screen-clip' in line: inside_clip = True

        if inside_clip:
            # Look for raw y= values that are suspicious (< 20)
            for m in re.finditer(r'\by="(-?\d+)"', line):
                y_val = int(m.group(1))
                if y_val < 20 and y_val != 0:  # y=0 is fine inside a translate group
                    # Only flag if it looks like an absolute coordinate, not inside a transform group
                    if 'translate(' not in line:
                        warn(name, i,
                             f'y="{y_val}" may be an absolute coordinate above the screen boundary '
                             f'(clip starts at y=20). If this is inside a translate() group it\'s fine.')

# ─────────────────────────────────────────────
# CHECK 5: Unbalanced <g> tags
# ─────────────────────────────────────────────
for name, path in SVG_FILES.items():
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    stack = []
    for i, line in enumerate(lines, 1):
        # Skip self-closing and commented lines
        stripped = re.sub(r'<!--.*?-->', '', line)
        opens = len(re.findall(r'<g[\s>]', stripped)) + len(re.findall(r'<g$', stripped))
        closes = len(re.findall(r'</g>', stripped))
        for _ in range(opens): stack.append(i)
        for _ in range(closes):
            if stack: stack.pop()
            else: err(name, i, 'Unmatched </g> — extra closing tag')
    if stack:
        err(name, stack[0], f'Unclosed <g> tag (started at line {stack[0]}, {len(stack)} unclosed total)')

# ─────────────────────────────────────────────
# REPORT
# ─────────────────────────────────────────────
print('\n' + '='*60)
print('  ProWorker SVG/JS Health Check')
print('='*60)

if errors:
    print(f'\n🚨 ERRORS ({len(errors)}) — fix before building:\n')
    for e in errors: print(e)
else:
    print('\n[OK] No errors found.')

if warnings:
    print(f'\n[WARN] WARNINGS ({len(warnings)}) — review these:\n')
    for w in warnings: print(w)
else:
    print('[OK] No warnings.')

print('\n' + '='*60)

if errors:
    sys.exit(1)  # Non-zero exit so build pipeline can gate on this
