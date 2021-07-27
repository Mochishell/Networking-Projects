from netmiko import ConnectHandler
import config_modules
import getpass
import json
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

devices_dict = config_modules.read_devices('devices.txt')
devices_creds = config_modules.get_device_creds_unencrypted('password.txt')

#keys are ip addresses
for device in devices_dict:

    session = ConnectHandler( device_type=devices_dict[device]['type'], ip=devices_dict[device]['ipaddr'] ,
                                username=devices_creds[device]['username'], password=devices_creds[device]['password'])

    config_modules.debug_arp_cache(session)
    config_modules.debug_running_config(session)

#TODO:

