import pycom
from machine import UART
from machine import Pin
import machine
import os
from L76GNSS import L76GNSS
from pytrack import Pytrack

py = Pytrack()
l76 = L76GNSS(py, timeout=30)

pycom.heartbeat(False)
uart = UART(0, baudrate=115200)
os.dupterm(uart)


#Read the button, if pressed then not in deepsleep mode and connected to your wifi (to avoid many problem to update your code)
bouton = Pin('G4',mode=Pin.IN,pull=Pin.PULL_UP)
if bouton() == 0:
    pycom.rgbled(0xff9900) #orange
    from network import WLAN
    wlan = WLAN(mode=WLAN.STA)
    nets = wlan.scan()
    for net in nets:
        if net.ssid == 'your_ssid':
            print('Reseau trouvé!')
            wlan.connect(net.ssid, auth=(net.sec, 'your_password'), timeout=5000)
            while not wlan.isconnected():
                machine.idle() # économiser de l'energie durant les temps d'attente
            print('Connexion WLAN/WiFi OK!')
            machine.main('main2.py')
            break
else:
    pycom.rgbled(0x7f0000)
    machine.main('main.py')
