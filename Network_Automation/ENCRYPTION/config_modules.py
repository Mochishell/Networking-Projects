def create_vlans(device, lower, upper):
    for x in range(1, 11):
        output = device.send_config_set(['vlan {}'.format(x), 'name pythonVLAN{}'.format(x)])
        print(output)

def config_general(device, config_file):

    with open(config_file) as f:
        print('\nconfiguring using {}'.format(config_file))
        commands = f.read().splitlines()
        print(device.send_config_set(commands))

#returns a list devices
def read_devices(device_file):
    with open('devices.txt') as f:
        devices = f.read().splitlines()
        return devices
