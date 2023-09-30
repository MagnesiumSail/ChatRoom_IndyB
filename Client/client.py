import socket
import threading

exit_flag = False

#wait for user to type message and send
def sending(client):
     global exit_flag
     while not exit_flag:
            message = input('Please enter a message to send or Exit to quit:')
            if message.lower() == 'exit':
                exit_flag = True
                break
            client.sendall(message.encode('utf-8'))

#listen for received messages
def receiving(client):
    global exit_flag
    while not exit_flag:
        data = client.recv(1024)
        if not data:
            print("Connection closed by server.")
            exit_flag = True
            break
        print(f'Recieved: {data.decode()}')


def main():
    global exit_flag
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn_ip = input('Please enter the local IP to connect to:')
    client.connect((conn_ip, 34874))

    send = threading.Thread(target=sending, args=(client,), daemon=True)
    receive = threading.Thread(target=receiving, args=(client,), daemon=True)

    try:
        send.start()
        receive.start()

        while not exit_flag:
            pass
    finally:
        print('Closing Client')
        client.close()


if __name__ == "__main__":
    main()