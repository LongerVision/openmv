# MQTT Example.
# This example shows how to use the MQTT library.
#
# 1) Copy the mqtt.py library to OpenMV storage.
# 2) Install the mosquitto client on PC and run the following command:
#    mosquitto_sub -h test.mosquitto.org -t "openmv/test" -v
#
# Note: If the mosquitto broker is down (OSError -12) try a different one (ex: broker.hivemq.com)
import time, network
from mqtt import MQTTClient

SSID='' # Network SSID
KEY=''  # Network key

# Init wlan module and connect to network
print("Trying to connect... (may take a while)...")

wlan = network.WINC()
wlan.connect(SSID, key=KEY, security=wlan.WPA_PSK)

# We should have a valid IP now via DHCP
print(wlan.ifconfig())

client = MQTTClient("openmv", "test.mosquitto.org", port=1883)
client.connect()

while (True):
    client.publish("openmv/test", "Hello World!")
    time.sleep(1000)
