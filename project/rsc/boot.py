from network import LoRa
import time
import binascii


lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = binascii.unhexlify('0000000000000000')

#The device information **DevEUI**  from the pycom device:
app_key = binascii.unhexlify('FD2246DBBE450F4BD4EAE5418F59141E')


lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

print('Network joined!')