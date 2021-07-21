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
    with open(device_file) as f:
        device_dict = {}
        devices = f.read().splitlines()

        for host in devices:

            #creating a list, where each item is some aspect of that device
            switchX = host.split(', ')

            #converting the list into a dictionary
            device = {

                'ipaddr': switchX[0],
                'type': switchX[1],
                'name': switchX[2]
            }
            device_dict[device['ipaddr']] = device
        return device_dict
