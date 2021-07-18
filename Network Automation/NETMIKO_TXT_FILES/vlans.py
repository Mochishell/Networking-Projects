def create_vlans(device, lower, upper):
    for x in range(1, 11):
        output = device.send_config_set(['vlan {}'.format(x), 'name pythonVLAN{}'.format(x)])
        print(output)