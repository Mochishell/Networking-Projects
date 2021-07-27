from netmiko import ConnectHandler
import config_modules
import getpass
import json

#start small, active debug probably won't work, lets try to just do show commands and save them to files

devices_dict = config_modules.read_devices('devices.txt')
devices_creds = config_modules.get_device_creds_unencrypted('password.txt')

#keys are ip addresses
for device in devices_dict:
    config_modules.debug_arp_cache(devices_dict[device], devices_creds[device])
#writing arp table output to file

