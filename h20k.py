from machine import Pin,Timer
import time

class H20K(object):
    def __init__(self,pin_num,freq=10):
        self.tc=time.ticks_us()
        self.RV=0
        self.count=0
        self.cal_count=0
        self.pin=Pin(pin_num,Pin.IN,Pin.PULL_DOWN)
        self.pin.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING, handler=lambda t:self.callback_count())
        self.Timer=Timer(freq=freq,mode=Timer.PERIODIC, callback=lambda t:self.callback_RV(freq/40))
    def callback_count(self):
        ee=time.ticks_us()
        if(ee-self.tc>500):
            self.count=self.count+1
            self.tc=ee
    def callback_RV(self,cvz):
        count_now=self.count
        self.RV=(count_now-self.cal_count)*cvz
        self.cal_count=count_now
    
if __name__=="__main__":
     c=H20K(0)
     e=H20K(1)
     while True:
         print("累计:",c.count,e.count)
         print("转速:",c.RV,e.RV)
         time.sleep(1)

