# PyTrack-GPS-LoPy-TTN-HA_tracker

This project link a GPS tracker that sends it's coordinate by LoRa trought the TTN (The things Network), TTN decodes the payload then send it by MQTT. Home Assitant receive that MQTT message trought an JSON MQTT Device Tracker Component, you can then see it on your map or program differents interactions.

ToDo: resend the coordinate to Owntracks to be able to see it on your mobile phone. Need to reformat the payload to be owntracks compliant

You need :
* a LoPy or LoPy4 from Pycom https://pycom.io/product/lopy/
* a Pytrack from Pycom https://pycom.io/hardware/pytrack-specs/
* a TTN acount https://console.thethingsnetwork.org/
* a working Home Assistant system with a functionning MQTT broker : https://home-assistant.io/

