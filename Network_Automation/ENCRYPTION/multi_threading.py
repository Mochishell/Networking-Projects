#!/usr/bin/env python

#assumes only cisco ios devices
from simplecrypt import encrypt, decrypt
from netmiko import ConnectHandler
import config_modules
import getpass
import json
import threading
from multiprocessing.dummy import Pool as ThreadPool
#limiting number of threads
num_threads = 5
#creating dictionary of devices, where each device is also a dictionary
#creating a dictionary of device, where each device is also a dictionary
#separates passwords
user_input = input("Please input a file containing devices: ")
user_password_input = input("Please input your encrypted password file: ")
user_encryption_key = input("Please input your encryption/decryption key: ")



devices_dict = config_modules.read_devices(user_input)
devices_creds = config_modules.get_device_creds(user_password_input, user_encryption_key)

#config_modules.get_devices_config(devices_dict, devices_creds)

config_threads_list = []
config_param_list = []
#each item(device) is itself a dictioanry
for item in devices_dict:
    config_param_list.append( (devices_dict[item], devices_creds[item]))


#creating thread pool, need to use starmap instead of map for methods with multiple arguments
threads = ThreadPool(num_threads)
final = threads.starmap(config_modules.get_device_config_thread, config_param_list)

threads.close()
threads.join()







