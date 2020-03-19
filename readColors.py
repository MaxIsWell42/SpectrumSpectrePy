import sys
import io
import os
import string
# import cpython
import webcolors
from colorthief import ColorThief
from urllib.request import urlopen

# Snippet from https://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green-with-python
# def closest_colour(requested_colour):
#     min_colours = {}
#     for key, name in webcolors.css3_hex_to_names.items():
#         r_c, g_c, b_c = webcolors.hex_to_rgb(key)
#         rd = (r_c - requested_colour[0]) ** 2
#         gd = (g_c - requested_colour[1]) ** 2
#         bd = (b_c - requested_colour[2]) ** 2
#         min_colours[(rd + gd + bd)] = name
#     return min_colours[min(min_colours.keys())]

# def get_colour_name(requested_colour):
#     try:
#         closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
#     except ValueError:
#         closest_name = closest_colour(requested_colour)
#         actual_name = None
#     return actual_name, closest_name

def colorDetect(image):
    # Read the URL into an image, future feature
    # fd = urlopen(image)
    # f = io.BytesIO(fd.read())
    
    f = "static/screenshot.png"

    # Give the package an image to analyze
    color_thief = ColorThief(f)
    
    # Get the dominant color, saved in hex color sequence as a tuple
    dominant_color = color_thief.get_color(quality=1)
    dc_name = webcolors.rgb_to_name((dominant_color[0], dominant_color[1], dominant_color[2]))

    # build a color palette
    palette = color_thief.get_palette(color_count=6)
    print("Dominant color: \n{}\nPalette: \n{}".format(dc_name, palette))

