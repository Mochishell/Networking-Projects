from simplecrypt import encrypt, decrypt
from netmiko import ConnectHandler
import config_modules
import getpass
import json


def create_vlans(device, lower, upper):
    for x in range(1, 11):
        output = device.send_config_set(['vlan {}'.format(x), 'name pythonVLAN{}'.format(x)])
        print(output)

#configures a device with specified config_file
def config_general(device, config_file):

    with open(config_file) as f:
        print('\nconfiguring using {}'.format(config_file))
        commands = f.read().splitlines()
        print(device.send_config_set(commands))

#returns a dictionary of devices, key is ip address of device
def read_devices(device_file):
    with open(device_file) as f:
        device_dict = {}
        devices = f.read().splitlines()

        for host in devices:

            #creating a list, where each item is some aspect of that device
            switchX = host.split(', ')

            #converting the list into a dictionary
            device = {

                'ipaddr': switchX[0],
                'type': switchX[1],
                'name': switchX[2]
            }
            device_dict[device['ipaddr']] = device
        return device_dict

#returns dictionary of devices, where key is ip
def get_device_creds(encrypted_password_file, key):
    with open(encrypted_password_file, 'rb') as file:
        #todo: convert encrypted file back into list and format into dictionary
        decrypted_file = json.loads(decrypt(key, file.read()))
        cred_dict = {}

        for device in decrypted_file:
            #format of list item is IP, username, password
            cred_dict[device[0]] = {'username': device[1], 'password': device[2]}
        return cred_dict

