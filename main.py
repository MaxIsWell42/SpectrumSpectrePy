import sys
from readColors import colorDetect
from screenCapture import captureDesktop
from absl import flags

# Test file
# file = "static/Peacock-1-650x425.jpg"

# Test link
# file = "https://assets.wordpress.envato-static.com/uploads/2017/02/RGB-1.jpg"
# file = "static/screenshot.png"

# Define the global flags
FLAGS = flags.FLAGS

# Flags
flags.DEFINE_boolean('ss', True, 'Waits 3 seconds, takes a screenshot of main desktop and uses that for spectrum analysis.')
flags.DEFINE_string('link', None, 'Takes a link for spectrum analysis.')

if __name__ == "__main__":
    # Parse the flags
    FLAGS(sys.argv)
    
    # Implement flags
    if FLAGS.link:
        colorDetect(FLAGS.link)

    elif FLAGS.ss:
        file = captureDesktop()
        colorDetect(file)