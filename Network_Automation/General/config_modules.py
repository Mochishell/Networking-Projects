from simplecrypt import encrypt, decrypt, DecryptionException
from netmiko import ConnectHandler
import config_modules
import getpass
import json
import csv

#configures a device with specified config_file
def config_general(session, config_file):

    with open(config_file) as f:
        print('\nconfiguring using {}'.format(config_file))
        commands = f.read().splitlines()
        print(session.send_config_set(commands))

#configures loopback with ip on specified interface
def config_loopback(session, interface, ip):
    print('Configuring loopback for {}'.format(session.host))
    commands = ['interface {}'.format(interface), 'ip address {} 255.255.255.255'.format(ip)]
    print(session.send_config_set(commands))

#returns a dictionary of devices, key is ip address of device
#each device is also a dictionary
def read_devices(device_file):
    with open(device_file) as f:
        device_dict = {}
        devices = f.read().splitlines()

        for host in devices:

            #creating a list, where each item is some aspect of that device
            switchX = host.split(',')

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

#Does the same thing as get_device_creds, but assumed unencrypted password file
def get_device_creds_unencrypted(password_file):
    with open( password_file ) as f:
        devices = csv.reader(f)
        password_dict = {}
        for row in devices:
            password_dict[row[0]] = {'username': row[1], 'password': row[2]}
        return password_dict


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

#sends sh arp command and writes it to file
#takes device and device_creds are both dictionaries
#session.ip not working
def debug_arp_cache(session):

    #writing arp table output to file for this device
    with open('{}_arp.txt'.format(session.host), 'w') as f:
        print('\n Writing to file arp cache for {}'.format(session.host))
        f.write(session.send_command('show arp'))

def debug_running_config(session):

    with open('{}_running_config.txt'.format(session.host), 'w') as f:
        print('\n Writing to file running config for {}'.format(session.host))
        f.write(session.send_command('show run'))




