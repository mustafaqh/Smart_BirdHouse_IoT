**Group members**  
```
Awad Marah  
Bakir Shaimaa  
Habeb Mustafa  
Mohamad Baker  
```


## `Smart BirdHouse`  
### (collect data about inner climate and bird's traffic)

## Abstract:
-----------
The project goal is to provide a smart way to detect the bird's movement into and out of the birdhouse using ir-sensors and measure temperature and humidity inside the house using  DHT sensor.  
This project will help the researchers in the biology department at lnu university in kalmar to study the birds behavior.  

## Background and idea  
--------
The birdhouse project is a part of the Kalmar Dämme project.

Kalmar Dämme is a wetland located on the south entrance of Kalmar city which functions as nature's own treatment plan for ```a sustainable future```.  

The main goal of the Kalmar Dämmet project is to clean and reduce the nutrients in the water before it flows back to the Baltic Sea in the Kalmar Strait.  
The development of Kalmar Dämme will also help to create a better environment for fish and many sorts of birds which will increase biodiversity. [Read more](https://kalmarolandairport.se/hallbarhet/kalmar-damme/) 


Kalmar Municipality and Linnaeus University have signed a letter of intent to build the environmental technology center which will be located by the dam. 
[Read more](https://sverigesradio.se/artikel/5555465) 


A basic part of the Kalmar-dämme project is to study the behavior of birds in the area, like when they fly from/to their houses, how many times, and how it is related to the weather and temperature.
It would be impossible to study and measure all of this data by hand and without smart and technical aids.

Our project plan is also to measure temperature and humidity in real-time from the birdhouse, and how many times the bird flies to/ from the house.

Our project’s idea came up in collaboration between the IoT- department and biology department at Linnaeus university under the Kalmar-dämme project.  
We have been ispired by ```Magnus Elfwing , Fredrik Ahlgren``` watch [Project proposal](https://www.youtube.com/watch?v=zfM1ALGcsaI).



 

 

## links 
------------
* [Hardware](/doc/hardware.md)
* [Requirements](/doc/requirements.md)
* [Set up](/doc/setup.md)
* [Test](/doc/test.md)
* [Timelog](/doc/timelog.md)

## Results 
-----------------
[Presentaion video on youtube](https://www.youtube.com/watch?v=x6OeRoGavVY) 

### Wiring  
IR sender: GND->> resistor ->> Emitter(LED)(cathode-> anode)->> 3V3.  
IR reciever: GND ->>phototransistor (collector=white)->(emitter=green) ->>VIN.  
![](/img/IR-.png)

The transmitter requires resistance adapted to the driving voltage. for more information, please, read in [Hardware](/doc/hardware.md) under title ```IR barrier transmitter / receiver ```.  
The second pair is connected in parallel to the first. Each pair, sender, and receiver  are placed in front of each other as seen in the image below

### Imeges of the birdhouse and pycom device connecting:

![](/img/pro2.png) ![](/img/pro4.jpg) 


### Imeges of the birdhouse and the pycom device in the box we printed:

![](/img/birdbox.jpeg)
![](/img/birdbox1.jpeg)
![](/img/birdbox2.jpeg)
 

### Data visualization:
In dashboard, we have chosen two widgets, temperature and humidity, for DHT sensor,  where two graphs show how recieved data changes over time. Bird in/out traffic is visualized in two tables in dashbord.  

![](/img/signal.png)  

The following picture shows four graphs that visualize received data (temperature, humidity, and birds in/out traffic).   
Bird's traffic is shown in two separate graphs "Bird in" and "Bird out" where each point represents how many times the   
bird has left or come back to its house during the last hour.
![](/img/graph1.png)  

Folowing picture shows device's location(in our case linnaeus university).
![](/img/graph.png)  

For instance, the marked point on the graph in folowing picture shows that  
the bird has left its house five times during the last hour.  

![](/img/graph4.png)



  
 
----
## Discussion of results
----
### Sensors we used:
### Pir sensor inside and ir sensor outside: 
We tested many motion sensors, at the first pir sensor to get the best results possible.  
The plan was to use a pir sensor in the house or in front of the birdhouse to detect any motion there.  
The Pir sensor was sensitive but it was hard to use in the house because it gives only high or low.  
If we use pir sensor on the inside and an ir sensor outside. If the bird is in the house we get always high in pir-output when he moves.  
The good part was that we make use of the house´s wood, which isolates detecting movement outside of the house.  
By using pir sensor can know if there is a bird inside or not, but the problem was that it is impossible to know  
how many birds there are inside and it is hard to make sure if the bird gets out or in because of the big angle for detecting the distance discovered is about 100-120 degrees. 

### Two pairs ir sensors:  

The best result is by using two pairs of ir sensors one pair -sender and receiver- outside and another pair inside. We put them on both sides of the gate. The spreading angle for the transmitter is 25 degrees, which serves our interests in the project. If an object cuts off the signal for one pair we get ``0``, otherwise, the output is ``1``.


### Why Pybytes?  
- At the beginnig, there were several options like datacake, ubidots ...etc on the table, but at the end we chose pybytes for our IoT project.  
- Pybytes is a device management platform, cloud-based, free and available for all pycom productions, (development boards and modules).  
- It provides an easy way to connect your Lopy4 via both WiFi and LoRa and receives data collected by sensors.  
- It offers an online pymakr plugin, i.e. you can modify the code from the cloud.  
we are aware of that functionality of pybytes is, somewhat, limited.  
- It offers ```location``` of the used device.  
It enables easily a good estimation of battery power.  
- According our last evaluation of required data in this early stage of birdhouse project, check
[Requirements](/doc/requirements.md), we presume that Pybytes is a good choice, i.e. efficient.  


###  Thoughts:
We are generally satisfied with our final results, we think we have achieved a big part of requirements such as: 

1. Measuring humidity 
2. Measuring temperature 
3. Detecting bird traffic -entering or exiting- from the house hole. 
4. Counting how many times the bird leaves and comes back during one hour.
5. Sending data via Lora every hour. 
6. Visualizing data with graphs.
7. The device is battery-powered. 
 


  
### Defects and appropriate improvments:
This device and circuit consume high energy from the battery.  
We thought we could use machine.deep.sleep-function to solve this problem, but we did not  
have enough time and we were not sure that it would work.  
This kind of ir sensor has to be active all the time to detect the motions.  
This problem could be partly solved by installing solar cells on the top of the birdhouse which  
can recharge the battery used to feed the device and circuit(sensors and lopy4).

We think if we had more time, we would be able to improve our project by improving the code or using more advanced sensors  
such as low loadcell sensors which can be used to determine bird's quantity and monitor the growth of small birds.
 


