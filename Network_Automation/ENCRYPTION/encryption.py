#!/usr/bin/env python

from simplecrypt import encrypt, decrypt
from netmiko import ConnectHandler
import config_modules
import getpass
import json

devices_dict = config_modules.read_devices('devices.txt')

#should print a dictionary of dictionaries
device_creds = config_modules.get_device_creds('password.txt-encrypted', 'cisco')

IP = ['192.168.0.11', '192.168.0.12', '192.168.0.13']
session = ConnectHandler( device_type=devices_dict['192.168.0.11']['type'], ip=devices_dict['192.168.0.11']['ipaddr'],
                        username=device_creds['192.168.0.11']['username'],
                        password=device_creds['192.168.0.11']['password'] )

print(session.send_command('sh ip int brief'))




