# Usage

To use this script in your own environment, modify devices.txt, interface.txt and password.txt to fit your local environment. Make sure SSH is already pre enabled on your devices.
Note that the `devices.txt` and `password.txt` are symlinks pointing to their respective files in `Network_Automation`
Make sure there are no spaces after commas in devices.txt and password.txt

# Disclaimer
Currently only configured to work with Cisco IOS switches and routers

# Functionality
    - debug.py
        - Saves arp cache to file per device
        - Saves running config to file per device
    - interface.py
        - Uses `interface.txt` to configure interfaces per device. See `interface.txt` for formatting

# Potential functionality
-Incorporate multithreading for increased performance
