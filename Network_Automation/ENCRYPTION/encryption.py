#!/usr/bin/env python


from netmiko import ConnectHandler
from config_modules import create_vlans, config_general, read_devices
import getpass
import json

devices = read_devices('devices.txt')
device_dict = {}
for host in devices:

    #creating a list, where each item is some aspect of that device
    switchX = host.split(', ')

    #converting the list into a dictionary
    device = {
        'device_type': 'cisco_ios',
        'host': switchX[0],
        'username': switchX[1],
        'password': switchX[2]
    }

    #dictionary of devices, where each value per key is a dictionary containing device info
    #key is the device IP address
    device_dict[device['host']] = device

    #running the below line inputs the username/password
    #specified in the dictionary when sshing
    iosl2 = ConnectHandler(**device)

print (json.dumps(device_dict, indent = 4))



