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
    device_creds_reader = csv.reader(file)
    for device in device_creds_reader:
        print(device)