"""
Your very own pixel art program

Finish the code below. Then run it to make the computer display and save
your pixel art.
"""

from pygame import Color
from pixel_art_maker import PixelArtMaker

# Choose a title for your pixel art:
title_for_your_art = "FEPP Logo"

# Define your colors:
r = Color("#fd7a3d")
w = Color("#ffffff")

# Write down your pixel sequence:
data = [
    [w, w, w, w, w, w, w, w, r, r, r, r, r, r, r, r, r, w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, r, r, r, r, r, r, r, r, r, r, r, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, r, r, r, w, w, r, r, r, r, r, r, r, r, w, w, w, w, w, w],
    [w, w, w, w, w, w, r, r, r, w, w, r, r, r, r, r, r, r, r, w, w, w, w, w, w],
    [w, w, w, w, w, w, r, r, r, r, r, r, r, r, r, r, r, r, r, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, r, r, r, r, r, r, w, w, w, w, w, w],
    [w, w, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, w, r, r, r, w, w],
    [w, r, r, r, r, r, r, r, r, r, w, w, w, w, w, r, r, r, r, w, r, r, r, r, w],
    [w, r, r, r, r, r, r, r, r, w, r, r, r, r, r, w, r, r, r, w, r, r, r, r, w],
    [r, r, r, r, r, r, r, r, w, r, r, r, r, r, r, r, w, r, r, w, r, r, r, r, r],
    [r, r, r, r, r, r, r, r, w, r, w, w, r, w, w, r, w, r, w, r, r, r, r, r, r],
    [r, r, r, r, r, r, r, w, r, r, w, w, r, w, w, r, r, w, w, r, r, r, r, r, r],
    [r, r, r, r, r, r, w, w, r, r, r, r, r, r, r, r, r, w, r, r, r, r, r, r, r],
    [r, r, r, r, r, r, w, r, w, r, w, w, w, w, w, r, w, r, r, r, r, r, r, r, r],
    [r, r, r, r, r, w, r, r, w, r, r, w, w, w, r, r, w, r, r, r, r, r, r, r, r],
    [w, r, r, r, r, w, r, r, r, w, r, r, r, r, r, w, r, r, r, r, r, r, r, r, w],
    [w, r, r, r, r, w, r, r, r, r, w, w, w, w, w, r, r, r, r, r, r, r, r, r, w],
    [w, w, r, r, r, w, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, w, w],
    [w, w, w, w, w, w, r, r, r, r, r, r, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, r, r, r, r, r, r, r, r, r, r, r, r, r, w, w, w, w, w, w],
    [w, w, w, w, w, w, r, r, r, r, r, r, r, r, r, w, w, r, r, w, w, w, w, w, w],
    [w, w, w, w, w, w, r, r, r, r, r, r, r, r, r, w, w, r, r, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, r, r, r, r, r, r, r, r, r, r, r, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w, r, r, r, r, r, r, r, r, r, w, w, w, w, w, w, w, w]
]

PixelArtMaker.make_my_pixel_art(title_for_your_art, data)
