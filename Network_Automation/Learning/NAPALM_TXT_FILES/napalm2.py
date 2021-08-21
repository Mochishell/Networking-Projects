import json
import sys

from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver( '192.168.122.72', 'david', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
ios_output2 = iosvl2.get_arp_table()
#print (json.dumps(ios_output, indent=4))

original_stdout = sys.stdout

with open('output.txt', 'w') as f:
    sys.stdout = f
    print(json.dumps(ios_output, indent=)4)
    print(json.dumps(ios_output2, indent=4))
    sys.stdout =original_stdout
