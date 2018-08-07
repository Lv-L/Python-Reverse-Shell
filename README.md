# Python Reverse Shell
A simple reverse shell written in python.

Make sure to set the 'host' variable in 'client.py' to the IP address of the machine running 'server.py'

If python is not installed on the machine to run the client, you can use [pyinstaller](https://www.pyinstaller.org/downloads.html) to package the script into a .exe file. Use 'pyinstaller --onefile client.py' to package it. To make the console not appear when running the .exe, add the --noconsole option.

The machine on which client.py is run is the machine that server.py can run commands on. Make sure to store the server's IP in the host variable in client.py before running it.

The client.py script is meant to be run with command prompt to allow simpler setup. 

TODOs:
1. Add option to add revshell to startup
2. combine scripts so that shell commands can be sent and recieved from the same script
