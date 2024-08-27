import socket
import selectors


selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    # регистрация объекта для мониторинга готов ли он читать или писать
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accetp_connection) 

def accetp_connection(server_socket):
    client_socket, addr = server_socket.accept()  #Принимает входящее подключения
    print("Подключен", addr)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_messages)


def send_messages(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = "Hello world\n".encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:
        events = selector.select()  #(rey, events)
        # SelectorKey - NameTuple
        # fileobj
        # events
        # data

        for key, event in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == "__main__":
    server()
    event_loop()
