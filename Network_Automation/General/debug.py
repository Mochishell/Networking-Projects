from netmiko import ConnectHandler
import config_modules
import time


def main():

    start = time.time()

    #creating 2 dictionaries, one of devices and one of devices and passwords, keys are IP addresses
    devices_dict = config_modules.read_devices('devices.txt')
    devices_creds = config_modules.get_device_creds_unencrypted('password.txt')

    #configuring multi-threading
    config_threads_list = []
    config_param_list = []
    #keys are ip addresses
    for device in devices_dict:

        session = ConnectHandler( device_type=devices_dict[device]['type'], ip=devices_dict[device]['ipaddr'] ,
                                    username=devices_creds[device]['username'], password=devices_creds[device]['password'])

        config_modules.debug_arp_cache(session)
        config_modules.debug_running_config(session)

    #printing elapsed time
    print ( 'Time elapsed: {} seconds'.format(time.time() - start))
if __name__ == "__main__":
    main()

