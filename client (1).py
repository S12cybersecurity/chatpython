import socket
import threading

def client_con_send():
    global cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("127.0.0.1", 1212))

def send():
    while True:
        try:
            mensaje = input("How you want to send?\n")
            cliente.send(mensaje.encode())
        except KeyboardInterrupt:
            print("Cancelled")
            break
def recive():
    while True:
        try:
            mensaje_del_server = cliente.recv(1024)
            print("Server:",mensaje_del_server.decode())
        except KeyboardInterrupt:
            print("Cancelled")
            break


thread_send = threading.Thread(target=send)
thread_recive = threading.Thread(target=recive)
client_con_send()
thread_recive.start()
thread_send.start()
