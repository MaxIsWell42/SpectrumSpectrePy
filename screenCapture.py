import pyscreenshot as ImageGrab
from PIL import Image

def captureDesktop():
    # Create a variable that stores a full screen grab
    im = ImageGrab.grab()
    
    # Save the image instance to a file
    im.save("static/screenshot.png")
    
    # Show the image in a window(for testing)
    # im.show()
    
    # Convert to jpg so it can be analyzed
    img = Image.open("static/screenshot.png")
    rgb_img = im.convert('RGB')
    rgb_img.save('static/screenshot.jpg')
    