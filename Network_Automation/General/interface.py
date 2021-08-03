from netmiko import ConnectHandler
import config_modules
import csv

def main():
    #creating two dictionaries, one of devices and one of devices and IP addresses
    devices_dict = config_modules.read_devices('devices.txt')
    devices_creds = config_modules.get_device_creds_unencrypted('password.txt')

    devices_loopbacks_list = []
    #reading in loopbacks from csv
    with open('interface.txt') as f:
        reader = csv.reader(f)
        for row in reader:
            devices_loopbacks_list.append(row)

    #iterates through list of loopbacks, each loopback is a list with 4 items
    for loopback in devices_loopbacks_list:

        session = ConnectHandler( device_type=devices_dict[loopback[0]]['type'], ip=devices_dict[loopback[0]]['ipaddr'] ,
                                    username=devices_creds[loopback[0]]['username'],
                                    password=devices_creds[loopback[0]]['password'])
        print(session.host)

        #configuring interface/loopback for device
        config_modules.config_loopback(session, loopback[1], loopback[2],
                                            loopback[3])

if __name__ == "__main__":
    main()

