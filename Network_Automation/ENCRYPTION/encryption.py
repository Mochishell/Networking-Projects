#!/usr/bin/env python

from simplecrypt import encrypt, decrypt
from netmiko import ConnectHandler
from config_modules import create_vlans, config_general, read_devices
import getpass
import json

devices_dict = read_devices('devices.txt')
print(devices_dict)




