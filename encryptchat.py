import rsa
import socket
import threading
public_key, private_key = rsa.newkeys(1024)
DEFAULT_IP_PORT = ("127.0.0.1", 6969)
choice = input("Do you want to be server or client?")
if choice == "s":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(DEFAULT_IP_PORT)
    server.listen()
    print("Waiting for connection...")
    client, addr = server.accept()
    print("Connected to", addr)
    client.send(public_key.save_pkcs1())
    partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    print("Use ctrl + c to disconnect")
elif choice == "c":
    print("Connecting to server...", end='')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(DEFAULT_IP_PORT)
    print("Success! Connected to" , client.getpeername())
    partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1())
    print("Use ctrl + c to disconnect")
else: exit()
def send_msg(c):
    while True:
        try:
            msg = input()
            print('\033[A' + '\033[K', end='') #delete input line
            c.send(rsa.encrypt(msg.encode(), partner))
            print("\033[91mYou: \033[0m" + msg)
        except: exit()

def recv_msg(c):
    while True:
        try:
            msg = rsa.decrypt(c.recv(1024), private_key)
            print("\033[94mPartner: \033[0m" + msg.decode())
        except:
            print("Partner has disconnected. Exiting...")
            exit()
try:
    send_thread = threading.Thread(target= send_msg, args=(client,)).start()
    recv_thread = threading.Thread(target= recv_msg, args=(client,)).start()
except: pass

