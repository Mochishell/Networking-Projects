import json
import sys
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'david', 'cisco')
iosvl2.open()

orig_stdout = sys.stdout

bgp_neighbors = iosvl2.get_bgp_neighbors()

with open('bgp1.txt', 'w') as f:
    sys.stdout = f
    print(json.dumps(bgp_neighbors, indent=4))

iosvl2.close()