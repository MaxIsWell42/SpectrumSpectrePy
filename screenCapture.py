import pyscreenshot as ImageGrab
from PIL import Image
import time

def captureDesktop():
    # Wait 3 seconds so the user can switch to another screen, while counting down
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    
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
    