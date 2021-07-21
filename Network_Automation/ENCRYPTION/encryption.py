#!/usr/bin/env python

from simplecrypt import encrypt, decrypt
from netmiko import ConnectHandler
import config_modules
import getpass
import json

devices_dict = config_modules.read_devices('devices.txt')

#should print a dictionary of dictionaries
print(config_modules.get_device_creds('password.txt-encrypted', 'cisco'))





