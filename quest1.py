#PS_CSC_19_0051
from d1motor import Motor
from machine import I2C, Pin
from time import sleep
from rotary_irq_esp import *
sda = 21 
scl = 22
sw = Pin(5,Pin.IN)
r = RotaryIRQ(pin_num_clk=18, 
              pin_num_dt=23, 
              min_val=0, 
              max_val=100, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_WRAP)



i2c = I2C(1,sda=Pin(sda),scl=Pin(scl))

print(i2c.scan())
print(i2c)
a12 = Motor(0, i2c)
print(r.value())


def changeDirection():
    # def handle_interrupt(pin):
    #         rotateL(abs(val))
    #     
    #  
    # sw.irq(trigger = Pin.IRQ_FALLING, handler = handle_interrupt)
def motorSpeed():
    def rotateR(val):
        a12.speed(val)
        print(r.value())
    def rotateL(val):
        a12.speed(val*-1)
        print(r.value())
    

    while True:
        val = r.value()
        if val != 0:
            rotateR(val*100)
        elif val ==0:
            a12.brake()
            print(r.value())
            
        sleep(1)
motorSpeed()