import board
import neopixel
import time 
class NeoPixelStrip:
    def __init__(self, LED_COUNT):
        ORDER = neopixel.GRBW
        self.brightness = 0.05
        self.pixels = neopixel.NeoPixel(board.D18, LED_COUNT, brightness=self.brightness, auto_write=True, pixel_order=ORDER)
    
    def switch(self, red, green, blue, white):
        self.pixels.fill((int(red),int(green),int(blue),int(white)))
        self.pixels.show()

    def turn_off(self):
        self.pixels.fill((0,0,0,0))
        self.pixels.show()
    
    def change_brightness(self, brightness):
        self.pixels.brightness = brightness

if __name__ == '__main__':
    neo_strip = NeoPixelStrip()
    neo_strip.switch(100, 150, 0, 10)