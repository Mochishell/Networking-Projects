from netmiko import ConnectHandler
import config_modules
from multiprocessing.dummy import Pool as ThreadPool
import threading

num_threads = 6

def main():

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
        config_param_list.append( session )
        #config_modules.debug_arp_cache(session)
        #config_modules.debug_running_config(session)
        #config_threads_list.append(threading.Thread(target=config_modules.debug_arp_cache, args=session))

    threads = ThreadPool( num_threads )
    arp_results = threads.map(config_modules.debug_arp_cache, config_param_list)
    running_config_results = threads.map(config_modules.debug_running_config, config_param_list)
    threads.close()
    threads.join()

if __name__ == "__main__":
    main()

