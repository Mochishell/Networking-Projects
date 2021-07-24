#Description
This is a branch off *Network_Automation/NETMIKO_TXT_FILES* to showcase NETMIKO, password file encryption, and multi-threading to improve performance. This project primarily uses encryption.py and multi_threading.py for execution.

File names are hard-coded for simplicity, so if you'd like to tinker with some of the passwords/IP addresses of devices, you should edit *password.txt* and *devices.txt*

Currently only supports Cisco IOS. Testing was done in GNS3 using Cisco IOSv images hosted on the GNS3 VM.

Credits to David Bombal's 'Python for Network Engineers' course on Udemy for guiding me and introducing me to using Netmiko, Napalm, and multi-threading for network automation and programmability. 

NETMIKO documentation/supported device types can be found [here](https://github.com/ktbyers/netmiko)

#Assumptions
- Only Cisco IOS/IOSv devices are in the topology
- The password file is named *password.txt*
- The devices file is named *devices.txt*
- Script is ran in an environment with connection to IPs specified in *devices.txt* and *password.txt*


#Usage
1. Encrypt password.txt using encrypt_file.py. Example would be `$ python3 encrypt_file.py`. Input your encryption key. Creates an encrypted password file titled *password.txt-encrypted*

2. Run *multi_threading.py* `$ python3 multi_threading.py` and input your encryption key

3. If executed correctly, will write the running configs of switches defined in *devices.txt* to *.cfg* files.

#password.txt formatting
*password.txt* is formatted as a CSV with the following format per row:
`[IP ADDRESS OF DEVICE],[USERNAME],[PASSWORD]` without the brackets. 

#devices.txt formatting
*devices.txt* is formatted as a CSV with the following format per row:
`[IP ADDRESS OF DEVICE],[NETMIKO DEVICE TYPE],[HOSTNAME]`. Note that `HOSTNAME` is local to the script; All connection to devices is done through the IP address.

Supported `NETMIKO DEVICE TYPE` values can be found [here](https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md)





