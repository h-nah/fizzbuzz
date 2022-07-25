from datetime import datetime
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

        
def sek (pos, color, strip):
    if pos == datetime.now().second:
            strip.setPixelColor(pos , Color(0, 255, 0))
            strip.show()
            
def kleinerals (pos, color, strip):
     p = 0
     while p <= pos:
        strip.setPixelColor(p , color)
        p = p + 1
        strip.show()   
        
           

    
        
# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT,LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

last = datetime.now()

while True:
    time.sleep(0.1)
    if datetime.now().second != last.second:
        last = datetime.now()
        
    sek(datetime.now().second, Color(0, 255, 0), strip)
    
    kleinerals(datetime.now().minute, Color(0, 0, 50), strip)
    
    for pos in range(strip.numPixels()):
        strip.setPixelColor(pos , Color(0, 0, 0))
        strip.setBrightness(250)
        strip.show()
         
    if datetime.now().second == 59:
        kleinerals(datetime.now().hour, Color(255, 0, 0), strip)
        strip.show()
        time.sleep(2)
            

#         if datetime.now().second > 58:
#             if pos <= datetime.now().hour:
#                 strip.setPixelColor(datetime.now().hour , Color(0, 0, 255))
#                 strip.show()
#                 time.sleep(3)
#         elif pos == datetime.now().second:
#                 strip.setPixelColor(pos , Color(0, 255, 0))
#                 strip.show()
#         elif pos <= datetime.now().minute:
#                 strip.setPixelColor(pos , Color(255, 0, 0))
#     
#                             
#               
