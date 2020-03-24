import sys
import io
import os
import string
import webcolors
from colorthief import ColorThief
from urllib.request import urlopen
from absl import flags

# list_of_colors = [[255,0,0],[150,33,77],[75,99,23],[45,88,250],[250,0,255]]
# color = [155,155,155]

# Define the global flags
FLAGS = flags.FLAGS

# Snippet from https://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green-with-python
def closest_colour(requested_colour):
    """Get the closest color as an rgb value, takes in RGB value like (42, 43, 51)"""
    min_colours = {}
    # Change the html4 in this line to css3 for more but unsupported colors. This only uses the 16 essential colors.
    # Uses Euclidian formula: dist((x, y), (a, b)) = √(x - a)² + (y - b)²
    for key, name in webcolors.html4_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    """Get the color's human name. Returns the actual color if present, or just gives the closest one available."""
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
    """Detect the colors in the image, format them to human names, and output them with descriptions."""
    # Flag: Read the URL into an image
    if FLAGS.link:
        fd = urlopen(image)
        f = io.BytesIO(fd.read())
    
    # Flag: Use screenshot for spectrum analysis
    elif FLAGS.ss:
        f = "static/screenshot.png"

    # Give the package an image to analyze
    color_thief = ColorThief(f)
    
    # Get the dominant color, saved in RGB color sequence as a tuple
    dominant_color = color_thief.get_color(quality=1)
    dc_name = get_colour_name(dominant_color)

    # Build a color palette, and run get_colour_name on each
    palette_list = []
    palette = color_thief.get_palette(color_count=2, quality=5)
    for tup in palette:
        palette_list.append(get_colour_name(tup))
        
    # Print out the colors and descriptions for them   
    print("Dominant color: \n   {}\n".format(colorCase(dc_name)))
    print("Color palette: ")
    for name in palette_list:
        color_description = colorCase(name)
        print("     Color name: {}\n".format(color_description))

def colorCase(color):
    """Switch argument handler for the colors and their descriptions. """
    colors = {
        "red": "Red: Influences you to act. Red is the color of passion, and makes you want to act on desires such as hunger, frustration or satisfaction by buying or consuming. It can increase your heartrate and make you excited. This is why it is prevalent in almost all fast food logos.",
        "blue": "Blue: Inspires calm and rational thought, blue is usually paired with few other colors as it's effect is most prevalent in simplicity.",
        "green": "Green: Another calm color, green inspires us to relax and take it easy. This can possibly be used to trick you into not thinking enough about a decision. Can also be used as a vibrant color",
        "black": "Black: Black is a quintessential 'sad' color with grey, usually used with muted cool colors. In Western culture it symbolizes mourning, whereas in East Asian cultures it means purity and rebirth. Can also be used to convey sophistication.",
        "silver": "Silver: The metallic version of grey, it still keeps the coolness but is also more lively and playful. Used to convey an industrial, high-tech elegance or ornate glamourousness. It can help our minds with things like public speaking and eloquence.",
        "grey": "Grey: A muted, sad color, grey is usually used with black to draw out feelings of somber and sadness, or can be used to convey seriousness and professionalism.",
        "white": "White: Creates a minimalist aesthetic. Simple, clean and usually modern, white is pretty neutral and is usually paired with other colors to make their effects more pronounced.",
        "maroon": "Maroon: Maroon is a dark red-brown color is used like red, but more reserved. It influences us to think something is sophisticated, luxurious and reserved, with a hint of pridefulness.",
        "purple": "Purple: A mixture of blue(calm) and red(intense), purple is usually used to spark creative thinking.",
        "fuchsia": "Fushsia: A vibrant combination of red and purple, this color can influence you to be more excited and creative, and draw out more action from that excitement.",
        "lime": "Lime: A vibrant version of green, this a 'happy' color aimed to grab your attention and make you feel energized and alert.",
        "olive": "Olive: A muted green, it can be used to represent growth, freshness and uniqueness. A good example of dark green being used is the Starbuck's logo.",
        "yellow": "Yellow: The brightest and lightest of the 'happy' colors, yellow influences us to feel joy and optimism. Usually combined with other happy colors to have a vibrant, youthful effect to get you excited.",
        "navy": "Navy: A dark blue, navy is usually used to convey importance and power, as well as intelligence, unity and stability.",
        "teal": "Teal: A deep, muted blue-green color, teal is used in design as a less-basic blue with a splash of sophistication. It encourages calm and reflection, and is sometimes used to contrast with other 'sophisticated' colors. Can also be used to convey reliability.",
        "aqua": "Aqua: A vibrant blue-green color, aqua makes us feel refreshed and calm, ready to take on anything. It connects to our expression and is associated with purity and openness.",
    }
    return colors.get(color, "Invalid Color")

# Links used for color study:
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4383146/
# https://99designs.com/blog/tips/how-color-impacts-emotions-and-behaviors/
# https://www.verywellmind.com/color-psychology-2795824
# https://www.bourncreative.com/meaning-of-the-color-silver/
# https://colorpsychologymeaning.com/color-maroon-burgundy/
# https://www.colorpsychology.org/teal/


