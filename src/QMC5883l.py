import math
import machine
from ustruct import pack
from array import array
import time

class QMC5883L():
    def __init__ (self, scl=22, sda=21, address=13):
        self.i2c =i2c= machine.I2C(scl=machine.Pin(scl), sda=machine.Pin(sda), freq=100000)
        self.address=address
        # Initialize sensor.
        i2c.start()
        i2c.writeto_mem(address, 0x0, b'\x01110000')
        i2c.writeto_mem(address, 0x1, b'\x00100000')
        i2c.writeto_mem(address, 0x2, b'\x00000000')
        i2c.stop()

        # Reserve some memory for the raw xyz measurements.
        self.data = array('B', [0] * 9)
           
    def read(self):
        """performs a reading of the data in the position of momoria 0x00, by means of a buffer"""
        data = self.data
        #Read data register 00H ~ 05H.
        
        
        self.i2c.readfrom_mem_into(self.address, 0x0, data)
        time.sleep(0.005)
        #self.i2c.readfrom_mem_into(30, 0x00, temperature)
        #time.sleep(0.005)

        x = (data[1] << 8) | data[0]
        y = (data[3] << 8) | data[2]
        z = (data[5] << 8) | data[4]
        #status =data[6]
        #temperature =z = (data[8] << 8) | data[7]
        scale =1
        #temperature_offest=50.0

#        return data
        return (x / scale, y / scale, z / scale)

    def heading(self, x, y):
        heading_rad = math.atan2(y, x)
        #heading_rad += self.declination

        # Correct reverse heading.
        if heading_rad < 0:
            heading_rad += 2 * math.pi

        # Compensate for wrapping.
        elif heading_rad > 2 * math.pi:
            heading_rad -= 2 * math.pi

        # Convert from radians to degrees.
        heading = heading_rad * 180 / math.pi
        degrees = math.floor(heading)
        minutes = round((heading - degrees) * 60)
        return degrees, minutes

    def cap(self):
        x, y, z = self.read()
        
        degrees, minutes = self.heading(x=x, y=y)
        return x, y
