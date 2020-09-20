import board
import neopixel

class NeoPixelStrip:
    def __init__(self):
        ORDER = neopixel.GRBW
        self.brightness = 0.5
        self.pixels = neopixel.NeoPixel(board.D18, 180, brightness=self.brightness, auto_write=False, pixel_order=ORDER)
    
    def turn_on(self):
        self.pixels.fill((128,128,128,0))
        self.pixels.show()

    def turn_off(self):
        self.pixels.fill((0,0,0,0))
        self.pixels.show()