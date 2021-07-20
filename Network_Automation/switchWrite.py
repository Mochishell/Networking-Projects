from netmiko import ConnectHandler


f = open('switches.txt')

for IP in f:
    iosv_l2 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'david',
        'password': 'cisco'
    }

    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_command('wr')
    print (output)