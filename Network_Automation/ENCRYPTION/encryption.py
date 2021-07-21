#!/usr/bin/env python


from netmiko import ConnectHandler
from config_modules import create_vlans, config_general, read_devices
from simplecrypt import encrypt, decrypt
import csv
import getpass
import json

devices = read_devices('devices.txt')
device_dict = {}
for host in devices:

    #creating a list, where each item is some aspect of that device
    switchX = host.split(', ')

    #converting the list into a dictionary
    device = {

        'ipaddr': switchX[0],
        'type': switchX[1],
        'name': switchX[2]
    }

    #adding device to master dictionary, key is ip of device
    device_dict[device['ipaddr']] = device

    #running the below line inputs the username/password
    #specified in the dictionary when sshing
    #iosl2 = ConnectHandler(**device)

print (json.dumps(device_dict, indent = 4))



