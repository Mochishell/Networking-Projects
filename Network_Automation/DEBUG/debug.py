from netmiko import ConnectHandler
import config_modules
import getpass
import json

#start small, active debug probably won't work, lets try to just do show commands and save them to files

devices_dict = config_modules.read_devices('devices.txt')
devices_creds = config_modules.get_device_creds_unencrypted('password.txt')


session = ConnectHandler( device_type=devices_dict['192.168.0.11']['type'], ip=devices_dict['192.168.0.11']['ipaddr'],
                                username=devices_creds['192.168.0.11']['username'],
                                password=devices_creds['192.168.0.11']['password'] )

print(session.send_command('sh arp'))

#writing arp table output to file
with open('{}_arp.txt'.format(devices_dict['192.168.0.11']['name']), 'w') as f:
    f.write(session.send_command('sh arp'))
