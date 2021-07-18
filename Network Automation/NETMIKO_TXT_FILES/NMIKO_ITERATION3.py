#!/usr/bin/env python

from netmiko import ConnectHandler
import getpass
#basic script, ensure a connection can be made
#to switch 1


#read places the whole text file as one string into the variable
#splitlines splits the text file into list items based on line breaks
with open('switch_ip.txt') as f:
    IP = f.read().splitlines()

for host in IP:

    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': 'brandon',
        'password': 'cisco'
    }


    #running the below line inputs the username/password
    #specified in the dictionary when sshing
    iosl2 = ConnectHandler(**device)
    output = iosl2.send_command('show ip int brief')

    #creating vlans
    for x in range(1, 11):
        iosl2.send_config_set('int vlan {}'.format(x), 'name pythonVLAN{}'.format(x))

    print(output)
