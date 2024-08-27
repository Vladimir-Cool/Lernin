import socket
from select import select

# .fileno()

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

def accetp_connection(server_socket):
    client_socket, addr = server_socket.accept()  #Принимает входящее подключения
    print("Подключен", addr)

    to_monitor.append(client_socket)    #Мониторим 2 сокета

def send_messages(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = "Hello world\n".encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
        redy_to_read, redy_to_write, odj_have_error = select(to_monitor, [], [])   # read, write, errors

        for sock in redy_to_read:
            if sock is server_socket:
                accetp_connection(server_socket)
            else:
                send_messages(sock)

if __name__ == "__main__":
    to_monitor.append(server_socket)
    event_loop()
