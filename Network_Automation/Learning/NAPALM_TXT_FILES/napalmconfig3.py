import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosl2 = driver('192.168.122.72', 'david', 'cisco')
iosl2.open()


print ('Accessing 192.168.122.72')

iosl2.load_merge_candidate(filename='ACL2.cfg')
diffs = iosl2.compare_config()

print(diffs)

if len(diffs) > 0:
    print('comitting config')
    iosl2.commit_config()
else:
    print('discarding config')
    iosl2.discard_config()

iosl2.load_merge_candidate(filename='ospf1.cfg')
diffs = iosl2.compare_config()

if len(diffs) > 0:
    print ('differences detected')
    print(diffs)
    iosl2.commit_config()
else:
    print( 'No OSPF changes required.')
    iosl2.discard_config()

iosl2.close()


