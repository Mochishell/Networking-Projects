#skeleton code from david bombal

from netmiko import ConnectHandler
from config_modules import create_vlans, config_general, read_devices
from simplecrypt import encrypt, decrypt
import csv
import getpass
import json

user_input = input("\nName you file that you'd like encrypted: ") or 'password.txt'
user_key = input('Input your encryption key: ') or 'cisco'

#now, need to encrypt the file
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

