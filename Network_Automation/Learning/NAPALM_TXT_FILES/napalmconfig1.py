import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosl2 = driver('192.168.122.72', 'david', 'cisco')
iosl2.open()


print ('Accessing 192.168.122.72')
iosl2.load_merge_candidate(filename='ACL1.cfg')
iosl2.commit_config()
iosl2.close()


