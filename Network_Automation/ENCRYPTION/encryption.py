#!/usr/bin/env python


from netmiko import ConnectHandler
from config_modules import create_vlans, config_general, read_devices
import getpass

devices = read_devices('devices.txt')
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

    #running the below line inputs the username/password
    #specified in the dictionary when sshing
    iosl2 = ConnectHandler(**device)
    print(iosl2.send_command('sh ip int brief'))



