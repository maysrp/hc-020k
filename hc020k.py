from machine import Pin,Timer
import time
import micropython

micropython.alloc_emergency_exception_buf(100)
class HC020K(object):
    def __init__(self,apin,freq=10):
        self.tc=[]
        self.pin_nums=[]
        self.pins=[]
        self.counts=[]
        self.cal_counts=[]
        self.jug=[]
        self.RV=[]
        if isinstance(apin,int):
            self.add_one_Pin(apin)
        if isinstance(apin,list):
            self.add_list(apin)
        self.Timer=Timer(freq=freq,mode=Timer.PERIODIC, callback=lambda t:self.callback_RV(freq/40))
    def add_list(self,li):
        for i in li:
            self.add_one_Pin(i)
    def add_one_Pin(self,pin_num):
        if pin_num not in self.pin_nums:
            self.pin_nums.append(pin_num)
            self.add_ob_pin(pin_num)
    def add_ob_pin(self,pin_num):
        self.counts.append(0)
        self.tc.append(time.ticks_us())
        self.jug.append(0)
        self.RV.append(0)
        self.cal_counts.append(0)
        pin=Pin(pin_num,Pin.IN,Pin.PULL_DOWN)
        pin.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING, handler=lambda t:self.callback_count(self.pin_nums.index(pin_num)))
        self.pins.append(pin)
    def callback_count(self,pin_num_index):
        ee=time.ticks_us()
        if(ee-self.tc[pin_num_index]>500):
            self.counts[pin_num_index]=self.counts[pin_num_index]+1
            self.tc[pin_num_index]=ee
    def callback_RV(self,cvz):
            for i in range(len(self.pin_nums)):
                count_now=self.counts[i]
                self.RV[i]=(count_now-self.cal_counts[i])*cvz
                self.cal_counts[i]=count_now

if __name__=="__main__":
     c=HC020K([0,1],2)
     while True:
         print("累计:",c.counts)
         print("转速:",c.RV)
         time.sleep(1)
