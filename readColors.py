import sys
import io
import os
import string
import webcolors
from colorthief import ColorThief
from urllib.request import urlopen

# list_of_colors = [[255,0,0],[150,33,77],[75,99,23],[45,88,250],[250,0,255]]
# color = [155,155,155]

# Snippet from https://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green-with-python
def closest_colour(requested_colour):
    """Get the closest color as an rgb value, takes in RGB value like (42, 43, 51)"""
    min_colours = {}
    # Change the html4 in this line to css3 for more but unsupported colors. This only uses the 16 essential colors.
    for key, name in webcolors.html4_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    """Get the closest color's human name """
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    if actual_name:
        return actual_name
    else: 
        return closest_name

def colorDetect(image):
    # Read the URL into an image, future feature
    # fd = urlopen(image)
    # f = io.BytesIO(fd.read())
    
    f = "static/screenshot.png"

    # Give the package an image to analyze
    color_thief = ColorThief(f)
    
    # Get the dominant color, saved in RGB color sequence as a tuple
    dominant_color = color_thief.get_color(quality=1)
    # print(dominant_color)
    dc_name = get_colour_name(dominant_color)

    # Build a color palette, and run get_colour_name on each
    palette_list = []
    palette = color_thief.get_palette(color_count=2, quality=5)
    for tup in palette:
        palette_list.append(get_colour_name(tup))

    print("Dominant color: \n{}\nPalette: \n{}".format(dc_name, palette_list))

def colorCase(color):
    colors = {
        1: "Red",
        2: "Blue",
        3: "Green",
        4: "Black",
        5: "Silver",
        6: "Gray",
        7: "White",
        8: "Maroon",
        9: "Purple",
        10: "Fuchsia",
        11: "Lime",
        12: "Olive",
        13: "Yellow",
        14: "Navy",
        15: "Teal",
        16: "Aqua"
    }