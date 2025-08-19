## Testing Pir Sensor: 
Pir sensor uses to sense motion by measuring infrared (IR) light radiating from the object in its limited view, and we are testing sensors field of view.

By using this primary code for the Pir sensor, we could detect motions:

```python
import time
from machine import Pin

pir = Pin('P18',mode=Pin.IN, pull=Pin.PULL_UP)
last_motion = -5

while True:
    if pir() == 1:
        if time.time() - last_motion > 5:
            last_motion = time.time()
            print("Motion detected")
    else:
        last_trigger = 0
        print("No motion detected")

    time.sleep(5)
```
### 1. Angle: 
* The angle for detecting the distance discovered was about 100-120 degrees. 

### 2. Distance:
* We tried to turn the distance screw to the max value, but there was no big difference. The minimum range for Pin was about 4 meters, which is so long to use in our project. 

### 3. Sensitivity:
* We tried to change the sensitivity adjustment for PIR sensor, which is longer than 6 meters. Because we don't want longer range than 50 cm. Turning the screw for the Pir clockwise makes it more sensitive. However we turned the screw for the minimum, the range stayed a few meters.

### 4. Waiting time:
* We use time.sleep()-function, to wait around one minute to calibrate, because the sensor needs time between 10 to 60 minutes to calibrate properly. When we tried to not use time.sleep() we got false results.

### 5. The time delay :
* At the first the results for output "1" or "0" lasted for about 20 seconds, so we turned the screw for the time delay for the minimum range to get best-needed results. 

![](/img/s-pir.png)  

## Sharp 2y0A02 F94:   

* This sensor is an analog, IR, distance sensor which was presumed as a suitable option.
We just managed to read the analog voltage by creating an ADC object, not further.  
For us, it is difficult to write a SharpIR library in micropython and on the other hand, we could not find an appropriate one, therefore this option was eventually neglected.  
![](/img/sharp-ir.png) 

## Testing IR barrier transmitter/receiver OPB100Z :

Testing ir sensors started with connecting the two sensors and determining how the distance affect the sensitivity of each sensor which is in the range 0-99cm and testing the Spreading angle for the transmitter which is 25 degree.
Then the two sensors were put on both sides of the gate, the front side and the inner side. The wooden wall is a good insulator between the two sensors which helps to avoid the interference between the waves of both emitters (senders) which helps to obtain a more accurate reading.
then an object was used as a bird to determine if the object was leaving the house or coming in the house by passing the object through the gate. after testing a few codes this code below was reaching.
by using the code and the two sensors the desired results were obtained by knowing which sensor was cut off first when the object passed through the gate.
finally, the result was determine if the object was going in or out and how many time each movement have been repeated.

```python
import machine
from machine import Pin
import utime
import time

ir2 = Pin('P23',mode=Pin.IN, pull=Pin.PULL_UP)
ir1 = Pin('P22',mode=Pin.IN, pull=Pin.PULL_UP)

count_in = 0
count_out = 0
while True:
    if ir1() == 1 and ir2() == 0:
        print('Out')
        count_in += 1
        print (count_in)
        time.sleep(1.5)

    elif ir1() == 0 and ir2() == 1:
        count_out += 1
        print('IN')
        print (count_out)
        time.sleep(1.5)

```

# Testing ir sensor code and pypytes:

We tried testing and editing our code to see how it´s working, we edited the code to make it simple as possible while testing the code we got a problem and it was not working properly so we worked on it a little more and fixed the problem. After trying different codes and functions, and testing we came up with this code below, but the result was not that perfect because another problem appeared with this code, when we ran the code with both sensors(ir and DHT) the code did not work, it worked when we tested each sensor separately, but not together so we need to work more on that step. 

# The code that we came up with while testing:

```python

from machine import Pin
import time
import machine
from dht import DHT



inside_ir = Pin('P23',mode=Pin.IN, pull=Pin.PULL_UP)
outside_ir = Pin('P22',mode=Pin.IN, pull=Pin.PULL_UP)


lats_ir1 = 1
last_ir2 = 1
count_in = 0
count_out = 0

# read from pin P23
# argument 0 refer to dht11
th = DHT(Pin('P21', mode=Pin.OPEN_DRAIN), 0)
time.sleep(2)


start = time.ticks_ms()

while True:
    
    result = th.read()
    while not result.is_valid() :
        time.sleep(.2)
        result = th.read()
    print('Temp:', result.temperature)
    print('RH:', result.humidity)
    pybytes.send_signal(2,result.temperature) 
    pybytes.send_signal(3,result.humidity) 



    if outside_ir() == 1 and inside_ir() == 0:
        print('Out')
        count_in += 1
        print (count_in)
        time.sleep(1.5)

    if outside_ir() == 0 and inside_ir() == 1:
        count_out += 1
        print('IN')
        print (count_out)
        time.sleep(1.5)

```



We have also checked the pybytes by sending random data via Lora to see if it´s working. By using a glue gun we fastened the sensors together in the birdhouse. We have also tested the DHT sensor and sent the temperature and humidity to pybytes via Lora, and it worked pretty well. 

# Continue with testing code:
We tried again with our code to make both sensors work together, we tried so many times but it did not work, we did not discover where the problem is but we think is not with our code, it´s with the connection on the breadboard. When we run our code only the temperature and humidity sensor will work, the ir sensor was not working at all. So we think there is something blocking the power to go through the other sensor. We have also changed between parallel connection and series connection, sometimes the ir sensors works but the DTH sensor does not, we only get zeroes for both temperature and humidity, and sometimes the DHT works, and the ir sensor does not work at all. We need to figure out where the problem is so the power can go through all sensors to get them to work properly.
