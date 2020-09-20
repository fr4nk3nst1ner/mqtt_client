This is a high-level MQTT client Python script that supports TLS. I didn't see many examples out there that included authentication so I wanted to share this in hopes it helps others test embedded implementations of MQTT to identify misconfigurations and identify vulns. 

You will need to hardcode the directory paths of your CA cerificate, client certificate, and private key within the script. These are notated within source to help guide where the changes need to be made. 
