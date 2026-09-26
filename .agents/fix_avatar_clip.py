# Fix for both v1 and v2 worker.svg:
# The avatar is inside: g(translate(36,136)) > image(x=24,y=24,w=80,h=80)
# Absolute coords = (60, 160, 80, 80)
# We need the clipPath to clip AT those absolute coords with rx=16

def fix_avatar_clip(filepath, clip_id):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove the inline clipPath definition (it's inside a transformed group which makes its coords wrong)
    old_clip_def = f'<clipPath id="{clip_id}">\n              <rect x="24" y="24" width="80" height="80" rx="16" />\n            </clipPath>\n'
    # 2. Replace the clip-path attribute on the image with clipPathUnits approach
    # Instead, just use a nested SVG or use the simpler approach:
    # Change the clipPath to use clipPathUnits="objectBoundingBox" which makes coords relative to the image
    
    # Simplest working fix: Add clipPathUnits="objectBoundingBox" to the clipPath
    # and change rect to use 0-1 coordinates (full extent = 0,0,1,1 with rx relative)
    # rx="16" px on 80px wide = rx=0.2 in objectBoundingBox
    
    new_clip = f'<clipPath id="{clip_id}" clipPathUnits="objectBoundingBox">\n              <rect x="0" y="0" width="1" height="1" rx="0.2" />\n            </clipPath>\n'
    
    if old_clip_def in content:
        content = content.replace(old_clip_def, new_clip)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")
    else:
        # Try to find and print what we have
        idx = content.find(clip_id)
        if idx >= 0:
            print(f"Found {clip_id} at {idx}, context: {repr(content[idx-5:idx+200])}")
        else:
            print(f"Could not find {clip_id} in {filepath}")

fix_avatar_clip('../screen/src/v1/worker.svg', 'worker-avatar-clip-v1')
fix_avatar_clip('../screen/src/v2/worker.svg', 'worker-avatar-clip-v2')
