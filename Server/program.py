import socket
import threading

#keeps track of all connections
clients = []

#New instance is added to clients for each connection
def handle_cleint(conn, adr):
    print(f'New connectino from {adr}')
    clients.append(conn)
    try:
        while True:
            #Will wait for data to come through
            data=conn.recv(1024)
            if not data:
                break
            print(f'Saw: \'{data.decode()}\' || From: {adr}')
            broadcast(data)
    finally:
        #Runs after client disconnects
        clients.remove(conn)
        conn.close()
        print(f'Connection from {adr} closed')

#Sends message to all connected clients
def broadcast(message):
    for client in clients:
        client.sendall(message)

def main():
    #Socket Setup
    local_ip = socket.gethostbyname(socket.gethostname())
    print(f'Your local ip is: {local_ip}')
    port=34874
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((local_ip, port))
    sock.listen(5)

    #Set up thread when new connection is made
    try:
        while True:
            #This will wait until it sees a new connection
            conn, adr = sock.accept()
            thread = threading.Thread(target=handle_cleint, args=(conn, adr))
            thread.start()
    finally:
        sock.close()

if __name__ == "__main__":
    main()

'''



client_socket, client_address = sock.accpet()
sock.connect((host, portal))

sock.sendall(b'Hello, World!')

data = sock.recv(1024)

sock.close()

try:
    #socket exceptions
except socket.error as e:
    print(f'Socket Error: {e}')

    '''
