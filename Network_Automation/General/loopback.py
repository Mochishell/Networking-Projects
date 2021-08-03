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

devices_loopbacks_list = []
#reading in loopbacks from csv
with open('loopback.txt') as f:
    reader = csv.reader(f)
    for row in reader:
        devices_loopbacks_list.append(row)
    #devices_loopbacks_list.append(row for row in reader)

      


print( devices_loopbacks_list)
#need to edit this to iterate through the loopback/interface list
for loopback in devices_loopbacks_list:

    session = ConnectHandler( device_type=devices_dict[loopback[0]]['type'], ip=devices_dict[loopback[0]]['ipaddr'] ,
                                username=devices_creds[loopback[0]]['username'], 
				password=devices_creds[loopback[0]]['password'])
    print(session.host)

    #configuring loopback for device
    config_modules.config_loopback(session, loopback[1], loopback[2],
					loopback[3])    
