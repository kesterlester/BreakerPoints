#!/usr/bin/env python3

import sys
import csv
import math
from PIL import Image
import matplotlib.pyplot as plt

POINT_NAMES = [
    "a_upper_din",
    "b_lower_din",
    "c_upper_opening",
    "d_lower_opening",
    "e_max_upper",
    "f_max_forward",
    "g_max_lower"
]

clicked = []

def canonical_transform(points):
    a = points[0]
    b = points[1]

    # translate so b becomes origin
    translated = [(x - b[0], y - b[1]) for x, y in points]

    ax_, ay_ = translated[0]

    # angle of b->a
    angle = math.atan2(ay_, ax_)

    # rotate so b->a points straight up (+y)
    rot = math.pi / 2 - angle
    c = math.cos(rot)
    s = math.sin(rot)

    rotated = []
    for x, y in translated:
        xr = x * c - y * s
        yr = x * s + y * c
        rotated.append((xr, yr))

    # scale to 35 mm DIN height
    axr, ayr = rotated[0]
    length = math.hypot(axr, ayr)
    scale = 35.0 / length

    scaled = [(x * scale, y * scale) for x, y in rotated]

    # enforce point c has positive x
    if scaled[2][0] < 0:
        scaled = [(-x, y) for x, y in scaled]

    return scaled


def onclick(event):
    if event.xdata is None or event.ydata is None:
        return

    clicked.append((event.xdata, event.ydata))
    idx = len(clicked) - 1

    ax.plot(event.xdata, event.ydata, 'ro')
    ax.text(event.xdata, event.ydata, POINT_NAMES[idx][0], color='red')

    if len(clicked) < len(POINT_NAMES):
        ax.set_title(f"Click: {POINT_NAMES[len(clicked)]}")
        fig.canvas.draw()
    else:
        plt.close()


if len(sys.argv) < 2:
    print("usage: python breaker_points.py imagefile [output.csv]")
    sys.exit(1)

imagefile = sys.argv[1]
outfile = sys.argv[2] if len(sys.argv) > 2 else None

img = Image.open(imagefile)
if img.mode not in ("RGB", "RGBA"):
    img = img.convert("RGB")

fig, ax = plt.subplots()
ax.imshow(img)
ax.set_title(f"Click: {POINT_NAMES[0]}")
fig.canvas.mpl_connect("button_press_event", onclick)

plt.show()

if len(clicked) != 7:
    print("Error: seven points required")
    sys.exit(1)

result = canonical_transform(clicked)

rows = []
for name, (x, y) in zip(POINT_NAMES, result):
    rows.append([name, round(x, 3), round(y, 3)])

if outfile:
    with open(outfile, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["point", "x_mm", "y_mm"])
        w.writerows(rows)
else:
    print("point,x_mm,y_mm")
    for row in rows:
        print(",".join(map(str, row)))
