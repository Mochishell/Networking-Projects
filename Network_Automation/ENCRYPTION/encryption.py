#!/usr/bin/env python

#assumes only cisco ios devices
from simplecrypt import encrypt, decrypt
from netmiko import ConnectHandler
import config_modules
import getpass
import json

#creating dictionary of devices, where each device is also a dictionary
user_input = input("Please input a file containing devices: ")
devices_dict = config_modules.read_devices(user_input)

#creating a dictionary of device, where each device is also a dictionary
#separates passwords
user_password_input = input("Please input your encrypted password file: ")
user_encryption_key = input("Please input your encryption/decryption key: ")

devices_creds = config_modules.get_device_creds(user_password_input, user_encryption_key)

config_modules.get_device_config(devices_dict, devices_creds)









