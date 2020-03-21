from readColors import colorDetect
from screenCapture import captureDesktop

# Test file
# file = "static/Peacock-1-650x425.jpg"

# Test link
# file = "https://assets.wordpress.envato-static.com/uploads/2017/02/RGB-1.jpg"
# file = "static/screenshot.png"

if __name__ == "__main__":
    file = captureDesktop()
    colorDetect(file)
    