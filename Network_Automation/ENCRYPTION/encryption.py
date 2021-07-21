#!/usr/bin/env python

from simplecrypt import encrypt, decrypt
from netmiko import ConnectHandler
import config_modules
import getpass
import json

devices_dict = config_modules.read_devices('devices.txt')
print(config_modules.get_device_creds('password.txt-encrypted', 'cisco'))

#TODO: decrypt password file and turn it into a dictionary



