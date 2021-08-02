from netmiko import ConnectHandler
import config_modules
import getpass
import json
import logging
import csv

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

devices_dict = config_modules.read_devices('devices.txt')
devices_creds = config_modules.get_device_creds_unencrypted('password.txt')
devices_loopbacks = []

#reading in loopbacks from csv
with open('loopback.txt') as f:
    reader = csv.reader(f)
    for row in reader:
        devices_loopbacks.append(row)

print(devices_loopbacks)
#keys are ip addresses
for device in devices_dict:

    session = ConnectHandler( device_type=devices_dict[device]['type'], ip=devices_dict[device]['ipaddr'] ,
                                username=devices_creds[device]['username'], password=devices_creds[device]['password'])

    
#TODO:

