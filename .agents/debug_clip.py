# The clipPath for the avatar is defined INSIDE a <g transform="translate(36, 136)">
# clipPath coords are in root SVG space, so the clip rect should be at:
# x = 36 + 24 = 60, y = 136 + 24 = 160, but since scrollable-content also translates (0,0) initially, this holds
# The REAL fix: move clipPath to defs with correct root-space coords
# avatar-clip rect: x=24,y=24,w=80,h=80 inside translate(36,136) => root coords x=60,y=160
# BUT scrollable-content group can translate on scroll => the clipPath will NOT follow the scroll!
# This means as the user scrolls, the clip stays fixed at root coords while the image moves - causing the bleed

# CORRECT APPROACH: Use clipPathUnits="objectBoundingBox" or use a nested clipPath that moves with the element
# Simplest fix: Remove the clipPath and use rx on the rect behind the image instead, relying on overflow:hidden
# OR: use SVG pattern/mask or set preserveAspectRatio + use the background rect corner radius as visual mask

# ACTUAL simplest fix for prototype: 
# 1. Keep the grey background rect with rx=16 (acts as visual rounded corner background)
# 2. The image just needs the clipPath to work correctly
# The issue is the clipPath is INSIDE a transformed group - SVG spec: clipPath is relative to SVG viewport
# So x=24,y=24 in a group translate(36,136) means the clip ACTUALLY clips at SVG coord (24,24) not (60,160)

print("Analysis complete:")
print("clipPath x=24,y=24 in SVG means clip at ABSOLUTE SVG position (24,24)")
print("Image is at SVG position (36+24=60, 136+24=160)")
print("So the clipPath is clipping a completely different area of the screen")
print("Result: image appears unclipped at its actual position")
