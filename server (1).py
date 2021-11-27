import socket
import threading
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def server_con():
    global ip
    global port
    ip = "127.0.0.1"
    port = 1212
    servidor.bind((ip, port))
    servidor.listen()
    global clientAddress
    global clientConnected
    (clientConnected, clientAddress) = servidor.accept()
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
def send():
    while True:
        try:
            para_cliente = input("How you want to send?\n")
            clientConnected.send(para_cliente.encode())
        except KeyboardInterrupt:
            print("Cancelled")
            break
def recive():
    while True:
        try:
            mensaje_cliente = clientConnected.recv(1024)
            print("Client:",mensaje_cliente.decode())
        except KeyboardInterrupt:
            print("Cancelled")
            break
server_con()
thread_send = threading.Thread(target=send)
thread_recive = threading.Thread(target=recive)
thread_recive.start()
thread_send.start()