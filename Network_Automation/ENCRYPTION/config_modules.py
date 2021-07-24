from simplecrypt import encrypt, decrypt, DecryptionException
from netmiko import ConnectHandler
import config_modules
import getpass
import json

#function that creates vlans for a given device
def create_vlans(device, lower, upper):
    for x in range(lower, upper):
        output = device.send_config_set(['vlan {}'.format(x), 'name pythonVLAN{}'.format(x)])
        print(output)

#configures a device with specified config_file
def config_general(device, config_file):

    with open(config_file) as f:
        print('\nconfiguring using {}'.format(config_file))
        commands = f.read().splitlines()
        print(device.send_config_set(commands))

#returns a dictionary of devices, key is ip address of device
#each device is also a dictionary
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
#assumes password file is encrypted, format is
#IP_ADDRESS,USERNAME_PASSWORD for each row
def get_device_creds(encrypted_password_file, key):
    with open(encrypted_password_file, 'rb') as file:
        #todo: convert encrypted file back into list and format into dictionary

        try:
            decrypted_file = json.loads(decrypt(key, file.read()))
        except(DecryptionException):
            print('Bad encryption key or corrupt data. Exiting script.')
            exit()

        cred_dict = {}

        for device in decrypted_file:
            #format of list item is IP, username, password
            cred_dict[device[0]] = {'username': device[1], 'password': device[2]}
        return cred_dict

#Writes the running config for each device in devices_txt to a separate file
#devices_dict: dictionary of dictionaries, key is IP Address
#devices_creds: dictionary of dictionaries, key is IP address
def get_devices_config(devices_dict, devices_creds):

    for device_ip in devices_dict.keys():

        session = ConnectHandler( device_type=devices_dict[device_ip]['type'], ip=devices_dict[device_ip]['ipaddr'],
                                username=devices_creds[device_ip]['username'],
                                password=devices_creds[device_ip]['password'] )



        if devices_dict[device_ip]['type'] == 'cisco_ios':
            print ('this is a cisco router')

        #writing to file the running config of the current switch, file name corresponds to switch
        with open( "{}".format(devices_dict[device_ip]['name']) + '.cfg', 'w') as f:
            print('Writing running config to file {}'.format(devices_dict[device_ip]['name']) + '.cfg')
            f.write(session.send_command('sh run'))

#Method intended to run as a thread (for a single device)
#device: dictionary of device details,
#device_creds: dictionary: username, password of device
def get_device_config_thread(device, device_creds):
    IP = device['ipaddr']
    creds = device_creds
    session = ConnectHandler( device_type=device['type'], ip=device['ipaddr'],
                                username=creds['username'],
                                password=creds['password'] )
    with open( "{}".format(device['name']) + '.cfg', 'w') as f:
            print('Connecting to {} '.format(device['ipaddr']))
            print('Writing running config to file {}'.format(device['name']) + '.cfg\n')
            f.write(session.send_command('sh run'))



