import socket
import threading

#allows for cleaner server disconnects
exit_flag = False

#wait for user to type message and send
#runs on its own thread
def sending(client):
     global exit_flag
     while not exit_flag:
            message = input('Please enter a message to send or Exit to quit:')
            if message.lower() == 'exit':
                exit_flag = True
                break
            #encodes message into bytes
            client.sendall(message.encode('utf-8'))

#listen for received messages
#runs on its own thread
def receiving(client):
    global exit_flag
    while not exit_flag:
        #will wait here until data comes through
        data = client.recv(1024)
        if not data:
            print("Connection closed by server.")
            exit_flag = True
            break
        print(f'Recieved: {data.decode()}')


def main():
    #setup of connection
    global exit_flag
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn_ip = input('Please enter the local IP to connect to:')
    client.connect((conn_ip, 34874))

    #two threads for send and receive
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