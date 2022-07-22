import time
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


for Zahl in range(1,60,1):
    if Zahl%5 == 0 and Zahl%3 == 0:
        print("Fizzbuzz")
    elif  Zahl%5 == 0:
        print("Buzz")
    elif  Zahl%3 == 0:
        print("Fizz")
    else:
        print(Zahl)
                
for pos in range(strip.numPixels()):
    time.sleep(0.5)
    if pos%5 == 0 and pos%3 == 0:
        strip.setPixelColor(pos , Color(0, 255, 0))
    elif  pos%5 == 0:
        strip.setPixelColor(pos , Color(0, 0, 255))
    elif  pos%3 == 0:
        strip.setPixelColor(pos , Color(255,0, 0))
    else:
        strip.setPixelColor(pos , Color(50, 50, 50))
    strip.show()

       