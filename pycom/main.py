print("deepsleep prog")

from network import LoRa
import socket
import binascii
import struct
import time
import utime #utime

init_timer = time.time()

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)


# create an ABP authentication params , use your own !
dev_addr = struct.unpack(">l", binascii.unhexlify('00 00 00 00'.replace(' ','')))[0] #replace 00 00 00 00
nwk_swkey = binascii.unhexlify('00000000000000000000000000000000')  #replace 00000000000000000000000000000000
app_swkey = binascii.unhexlify('00000000000000000000000000000000') #replace 00000000000000000000000000000000

print("start join LoRa")
print(utime.localtime())#utime
print(utime.time())#utime
# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
lora.nvram_restore() #strange place for the restore but working.

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

while(True):
    print(".")
    # save the coordinates in a new variable
    coord = l76.coordinates()
    # verify the coordinates received
    if coord == (None,  None):
        print("Getting Location...")
        pycom.rgbled(0x7f7f00) #jaune
        print(utime.time())#utime
        continue
    # send the Coordinates to LoRA
    print("sending")
    pycom.rgbled(0x0000ff) #bleu
    s.send(struct.pack("<i",  int(coord[0]*100000))+struct.pack("<i",  int(coord[1]*100000))+struct.pack("<H",  int(utime.time())))
    time.sleep(1)
    lora.nvram_save() #nvram
    print("sent")
    print(time.time())
    print(utime.localtime())#utime
    print(utime.time())#utime
    pycom.rgbled(0x000000)
    #sleep
    print("sleep")
    py.setup_sleep(600 - time.time())
    py.go_to_sleep()
