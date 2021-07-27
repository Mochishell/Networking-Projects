from netmiko import ConnectHandler
import config_modules
import getpass
import json

#start small

devices_dict = config_modules.read_devices('devices.txt')
devices_creds = config_modules.get_device_creds_unencrypted('password.txt')


session = ConnectHandler( device_type=devices_dict['192.168.0.11']['type'], ip=devices_dict['192.168.0.11']['ipaddr'],
                                username=devices_creds['192.168.0.11']['username'],
                                password=devices_creds['192.168.0.11']['password'] )

