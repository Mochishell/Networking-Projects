#skeleton code from david bombal
#encrypts a file
from netmiko import ConnectHandler
from config_modules import create_vlans, config_general, read_devices
from simplecrypt import encrypt, decrypt
import csv
import getpass
import json

#making the password.txt file static for simplicity
user_input = 'password.txt'
user_key = getpass.getpass('Input your encryption key: ') or 'cisco'

#creates an encrypted file, also creates a decrypted file as well, should be the same as the original
with open(user_input, 'r') as file:
    device_creds_reader = csv.reader(file, delimiter = ',')
    device_creds_list = [device for device in device_creds_reader]

encrypted_file_name = '{}-encrypted'.format(user_input)
decrypted_file_name = '{}-decrypted'.format(user_input)

with open(encrypted_file_name, 'wb') as file:
    file.write(encrypt(user_key, json.dumps(device_creds_list)))

with open(encrypted_file_name, 'rb') as file:
    decrypted_file = json.loads( decrypt( user_key, file.read()))
    print(decrypted_file)

