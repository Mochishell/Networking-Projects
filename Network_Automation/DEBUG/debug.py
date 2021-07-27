from netmiko import ConnectHandler
import config_modules
import getpass
import json

#start small

devices_dict = config_modules.read_devices('devices.txt')
devices_creds = config_modules.get_device_creds_unencrypted('password.txt')
print(devices_creds)
