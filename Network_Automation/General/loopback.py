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

#reading in loopbacks from csv
with open('loopback.txt') as f:
    reader = csv.reader(f)
    devices_loopbacks_dict = {row[0]: (row[1], row[2]) for row in reader}


#keys are ip addresses
for device in devices_dict:

    session = ConnectHandler( device_type=devices_dict[device]['type'], ip=devices_dict[device]['ipaddr'] ,
                                username=devices_creds[device]['username'], password=devices_creds[device]['password'])
    
    #configuring loopback for device
    config_modules.config_loopback(session, devices_loopbacks_dict[device][0], devices_loopbacks_dict[device][1])    

#TODO:

