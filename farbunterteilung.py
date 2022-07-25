from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 60     # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT,LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

for pos in range(strip.numPixels()):
    
    if pos in range(0, 9, 1):
        strip.setPixelColor(pos , Color(250, 0, 0))
        strip.setBrightness(250)
        strip.show()
    elif pos in range(10, 19, 1):
        strip.setPixelColor(pos , Color(150, 50, 50))
        strip.setBrightness(250)
        strip.show()
    elif pos in range(20, 29, 1):
        strip.setPixelColor(pos , Color(50, 150, 50))
        strip.setBrightness(250)
        strip.show()
    elif pos in range(30, 39, 1):
        strip.setPixelColor(pos , Color(0, 250, 0))
        strip.setBrightness(250)
        strip.show()
    elif pos in range(40, 49, 1):
        strip.setPixelColor(pos , Color(0, 0, 250))
        strip.setBrightness(250)
        strip.show()
    elif pos in range(50, 59, 1):
        strip.setPixelColor(pos , Color(83, 83, 83))
        strip.setBrightness(250)
        strip.show()
