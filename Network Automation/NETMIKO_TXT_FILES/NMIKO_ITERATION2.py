#!/usr/bin/env python

from netmiko import ConnectHandler
import getpass
#basic script, ensure a connection can be made
#to switch 1

IP = ['192.168.0.11', '192.168.0.12', '192.168.0.13']

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
    print(output)
