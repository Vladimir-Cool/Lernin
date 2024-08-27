import socket

#AF_INET адрес фамили ipv4
#SOCK_STREAM - поддержка протаколом TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#SOL_SOCKET  - указывает что изменения уровня сокета
#SO_REUSEADDR  - переиспользование адреса, 1 TRUE
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accetp_connection(server_socket):
    while True:
        print("Перед .accept")
        client_socket, addr = server_socket.accept()  #Принимает входящее подключения
        print("Подключен", addr)
        send_messages(client_socket)


def send_messages(client_socket):
    while True:
        print("Перед .recv")
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = "Hello world\n".encode()
            client_socket.send(response)

    print("выход из внутреннего цикла")
    client_socket.close()

if __name__ == "__main__":
    accetp_connection(server_socket)
