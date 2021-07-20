#!/usr/bin/env python

#this file is mostly for testing out modules defined in
#config_modueles.py

from netmiko import ConnectHandler
from config_modules import create_vlans, config_general
import getpass

#accepts the name of a file instead
config_file = input("Please input the files containing config commands:")

#splitting user input into a list of config_file names
list_files = config_file.split()

#probably only need 1 devices file
with open('devices.txt') as f:
    devices = f.read().splitlines()

for host in devices:

    #creating a list of lists, which each item is a deivce
    switchX = host.split(', ')

    device = {
        'device_type': 'cisco_ios',
        'host': switchX[0],
        'username': switchX[1],
        'password': switchX[2]
    }

    #running the below line inputs the username/password
    #specified in the dictionary when sshing
    iosl2 = ConnectHandler(**device)
    output = iosl2.send_command('show ip int brief')

    for file_name in list_files:
        config_general(iosl2, file_name)


