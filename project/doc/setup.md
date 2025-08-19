Visula Studio Code och Pymakr:
- Install Visual Studio Code https://code.visualstudio.com/Download
- Install NodeJS https://nodejs.org 
- Install PyMakr plugin in VScode (using the Extensions manager)
- Install pymakr plugin for Atom https://atom.io

Pycom:

- Connect the pycom device to the computer via USB
- Start VSCode or Atom 
- Creat a project folder
- Upload the project to the pycom device


The Things Network (TTN):

- Creat an account https://www.thethingsnetwork.org/
- Creat an application by clicking on Creat an application
- Add the pycom device to the application
- Run this code to get your DevEUI:

```python

from network import LoRa
import binascii

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))

```

The output should look similar to this:

  70B3D54997C25011

-  fill AppEUI with zeros by pressing 00
- Press add end device
- Connect to TTS with the pycom device and run this code:

```python

from network import LoRa
import time
import binascii

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = binascii.unhexlify('0000000000000000')
app_key = binascii.unhexlify('00000000000000000000000000000000')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

print('Network joined!')

# Your old code from main.py should be here

```
(Remeber to replace the zeros in app_key with your own app-key)

- Example to sending message through TTS:

```python

import socket
import time

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)


# Your old code from main.py should be here

# EXAMPLE: Create a DHT object, collect data in the loop and send it

while True:
    temperature = 23    # Mock value
    humidity = 40       # Mock value
    s.send(bytes([temperature, humidity]))
    print('sent temperature:', temperature)
    print('sent humidity:', humidity)
    time.sleep(900)     # wait 900 seconds (15 minutes) before sending again

```

## Pybytes 2.0:
### Create a pybytes account  

If you do not have an pybytes account, create one by going to Pybytes  [sign up](https://sso.pycom.io/register?client_id=pycom&redirect_uri=https%3A%2F%2Fpyauth.pybytes.pycom.io%2Fauth_code%2Fcallback&scope=profile&response_type=code&state=pybytes-browser).  

### Add device and networks
There is a helpful tutorial with pictures at the Pycom website. where you can:  
- add your device using, for instance, USB. We use Lopy4 + expantionboard 3.1
- select your network options with your network credentials, this will be used to connect your device with a WiFi or LORa network to access pybytes.  
Notice prioritization! Move LoRa option upp, if you would like use LoRa network. Choose LoRa OTAA at LoRa activation type.  
- rename your device.  
### Provision your device
- you will need to provision your device, using the Firmware Updater Tool. By this procedure, the Pycom tell your device about the Pybytes connection and how to set it up.
- To connect to your WiFi and send data to Pybytes, you have to create the pybytes_config.json file. That is why Activation Token is needed when provisoning.
- In our case we have provisioned Offline provisioning.  
- by rebooting, reset button on Lopy4, your device, the Pybytes connection shall be activated automatically.  
* An image shows that pybytes connection is succeeded: 
![](/img/pybytes-connection.png)
### Send signal  
- In [Pybytes Device](https://pybytes.pycom.io/devices), select your device.  
- In the ```signals``` tab, you can define new signal, there your signal will show up on Pybytes. 
- Add a widget for the signal
- To test signal sending, add the following code to ```main.py``` file in your project in *Pymakr*
``` 
# Import what is necessary to create a thread
import time
import math

# Send data continuously to Pybytes
while True:
    for i in range(0,20):
        pybytes.send_signal(1, math.sin(i/10*math.pi))
        print('sent signal {}'.format(i))
        time.sleep(10)

``` 
Note: you can also send sensor data at this point.  
- For our project we define 4 signals, i.e. we send data through 4 channels, 0 for temperature, 1 for humidity and 2 for bird traffic.  


###  Visualise data from your device
For detailed instructions with pictures and info about this step or pervious, please visit [disply data on pybytes](https://docs.pycom.io/pybytes/dashboard/) .  

