from machine import Pin, SPI
import st7920
spi = SPI(1)
screen = st7920.Screen(sck=Pin(14), mosi=Pin(13), miso=Pin(12), spi=1, slaveSelectPin=Pin(15), resetDisplayPin=Pin(5))
screen.plot(5, 5)
screen.line(10, 10, 15, 15)
screen.rect(20, 20, 25, 25)
screen.fill_rect(30, 30, 40, 40)
screen.fill_rect(32, 32, 38, 38, False)
screen.redraw()