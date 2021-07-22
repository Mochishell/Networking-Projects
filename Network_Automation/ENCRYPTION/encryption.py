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

for device_ip in IP:

    session = ConnectHandler( device_type=devices_dict[device_ip]['type'], ip=devices_dict[device_ip]['ipaddr'],
                            username=device_creds[device_ip]['username'],
                            password=device_creds[device_ip]['password'] )

    print(session.send_command('sh ip int brief'))

    if devices_dict[device_ip]['type'] == 'cisco_ios':
        print ('this is a cisco router')






