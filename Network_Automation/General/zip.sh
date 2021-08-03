#!/bin/bash

#will overwrite any existing tarballs created from this script

#will tar the arp files created from debug.py
printf "\nAttempting to tar arp files\n"
tar -czvf arp.tar.gz ./*arp.txt --remove-files 2> errors.txt 

if [ "$?" = "0" ]; then
    printf "arp.txt files tarred and removed\n"
else
    printf "arp.txt files already tarred or don't exist\n" 
fi
    
#will tar the running_config files created from debug.py
printf "\nAttempting to tar running_config files\n"
tar -czvf running_config.tar.gz ./*running_config.txt --remove-files 2>> errors.txt

if [ "$?" = "0" ]; then
    printf "running_config.txt files tarred and removed\n"
else
    printf "running_config.txt files already tarred or don't exist\n" 
fi
