#!/usr/bin/env python

from simplecrypt import encrypt, decrypt
from netmiko import ConnectHandler
import config_modules
import getpass
import json

#creating dictionary of devices, where each device is also a dictionary
devices_dict = config_modules.read_devices('devices.txt')

#creating a dictionary of device, where each device is also a dictionary
#separates passwords
device_creds = config_modules.get_device_creds('password.txt-encrypted', 'cisco')

for device_ip in devices_dict.keys():

    session = ConnectHandler( device_type=devices_dict[device_ip]['type'], ip=devices_dict[device_ip]['ipaddr'],
                            username=device_creds[device_ip]['username'],
                            password=device_creds[device_ip]['password'] )



    if devices_dict[device_ip]['type'] == 'cisco_ios':
        print ('this is a cisco router')

    #writing to file the running config of the current switch, file name corresponds to switch
    with open( "{}".format(devices_dict[device_ip]['name']) + '.cfg', 'w') as f:
        print('Writing running config to file {}'.format(devices_dict[device_ip]['name']) + '.cfg')
        f.write(session.send_command('sh run'))








