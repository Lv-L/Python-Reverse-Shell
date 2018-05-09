# Python Reverse Shell
A simple reverse shell created in python.


Make sure to set the 'host' variable in 'client.py' to the IP address of the machine running 'server.py'


If python is not installed on the machine to run the client, you can use [pyinstaller](https://www.pyinstaller.org/downloads.html) to package the script into a .exe file. Use 'pyinstaller --onefile client.py' to package it. To make the console not appear when running the .exe, add the --noconsole option.
