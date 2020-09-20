Performing an IoT pen test? Discovered that the device is communicating over the MQTT protocol and encrypting traffic / using crypto for auth? Use this script to connect to your broker and identify misconfigurations and identify vulns! 

Bonus: after authenticating, the script will subscribe to many common topics used by default, un-hardened MQTT implementations in addition to a wildcard subscription to all topics. 

You will need to hardcode the directory paths of your CA cerificate, client certificate, and private key within the script. These are notated within source to help guide where the changes need to be made. 

Please let me know if there are any improvements that could be made upon the script. 
