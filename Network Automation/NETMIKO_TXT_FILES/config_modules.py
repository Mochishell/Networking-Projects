def create_vlans(device, lower, upper):
    for x in range(1, 11):
        output = device.send_config_set(['vlan {}'.format(x), 'name pythonVLAN{}'.format(x)])
        print(output)

def config_general(device, descrp, config_file):
    with open(config_file) as f:
        print('configuring {}'.format(descrp))
        commands = f.read().splitlines()
        print(device.send_config_set(commands))

