# hc-020k
HC020K光电测速模块 micropython

使用PICO RP2040 在micropython的1.20下测试通过，上传hc020k.py 到你的PICO上 调用即可。

c.count 接收到的计数，
c.RV 每秒钟转动的大小

速度=c.RV[0]*轮子的周长


### 简单使用

```
import time
from hc020k import HC020k

c=HC020k(0)
while True:
   print("累计:",c.counts)
   print("转速:",c.RV)
   time.sleep(1)
#将GP0和HC020K测速模块的OUT引脚相连

累计: [0]
转速: [0.0]

```

### 需要安装多个测速模块

```
import time
from hc020k import HC020k

c=HC020k([0,1])
while True:
   print("累计:",c.counts)
   print("转速:",c.RV)
   time.sleep(1)
#将GP0、GP1分别和两个HC020K测速模块的OUT引脚相连

#累计: [0, 0]
#转速: [0.0, 0.0]

```
