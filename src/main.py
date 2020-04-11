from machine import Pin, SPI
import st7920

screen = st7920.Screen(sck=Pin(14), mosi=Pin(13), miso=Pin(12), resetDisplayPin=Pin(15), baudrate=900000)

screen.clear()

screen.plot(10, 12)
screen.fill_rect(10,12, 50, 52)

screen.redraw()