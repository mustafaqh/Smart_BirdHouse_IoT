from machine import Pin
import time
import machine
from dht import DHT

# initialize p22 and p23 and `make them an input
# Reads signal from IR Pair, placed inside of birdhouse
inside_ir = Pin('P22',mode=Pin.IN, pull=Pin.PULL_DOWN)

# Reads signal from IR Pair, placed inside of birdhouse
outside_ir = Pin('P23',mode=Pin.IN, pull=Pin.PULL_DOWN)


count_in = 0
count_out = 0

# reads from pin P23
# argument 0 refer to dht11
th = DHT(Pin('P21', mode=Pin.OPEN_DRAIN), 0)
time.sleep(2)


start = time.ticks_ms()
while True:
    result = th.read()
    # If two signals are interrupted
    if outside_ir() == 0 and inside_ir() == 0:
        # print("Obstructed entrance")
        pass
    if outside_ir() == 1 and inside_ir() == 1:
        # print("Free entrance")
        pass
    # If outside signal were interrupted
    if inside_ir() == 0 and outside_ir() == 1:
        # checks if the bird was realy in way out,
        # for instance, If a curious young bird sticks
        # its head out the opening, do nothing!
        while inside_ir()== 0:
            if outside_ir() == 1:
                pass
        print('Out')
        count_out += 1
        print (count_out)
        time.sleep(1)
    # If inside signal were interrupted, assume that
    # a bird would leave, but check wether the bird
    # would actually come in, or just was checking
    # the nest
    if outside_ir() == 0 and inside_ir() == 1:
        while outside_ir() == 0:
            if inside_ir()== 1:
                pass
        count_in += 1
        print('IN')
        print (count_in)
        time.sleep(1)

    # sends data to pybytes, every 1 hour
    if time.ticks_diff(time.ticks_ms(), start) > 3600000:
        # In and out  is a signal 3 and 4
        pybytes.send_signal(3,count_in)
        pybytes.send_signal(4,count_out)
        # checks reading of DHT-values
        if not result.is_valid():
            time.sleep(.5)
            result = th.read()
        # Temperature is a signal 0
        pybytes.send_signal(0,result.temperature)
        # Humidity is a signal 1
        pybytes.send_signal(1,result.humidity)

        # Visualizes and confirms sended data on Pymkr-console
        print('Temp:', result.temperature)
        print('RH:', result.humidity)
        print ("Send")

        count_in = 0
        count_out = 0
        start = time.ticks_ms()
