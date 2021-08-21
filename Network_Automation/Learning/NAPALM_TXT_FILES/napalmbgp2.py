import json
import sys
from napalm import get_network_driver


IPs = ['192.168.122.29', '192.168.122.72']
orig_stdout = sys.stdout

for x in IPs:

    driver = get_network_driver('ios')
    iosvl2 = driver(str(x), 'david', 'cisco')
    iosvl2.open()


    bgp_neighbors = iosvl2.get_bgp_neighbors()

    with open('bgp2.txt', 'a') as f:
        sys.stdout = f
        print(json.dumps(bgp_neighbors, indent=4))
        sys.stdout = orig_stdout
    iosvl2.close()