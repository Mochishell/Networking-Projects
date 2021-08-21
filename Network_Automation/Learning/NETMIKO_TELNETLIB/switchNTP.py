from netmiko import ConnectHandler


f = open('switches.txt')

for IP in f:
    iosv_l2 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'david',
        'password': 'cisco'
    }

    #probably smarter way to do this would be through DNS
    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_command('ntp server 192.168.122.1')
    print (output)