import socket
import threading

clients = []

def handle_cleint(conn, adr):
    print(f'New connectino from {adr}')
    clients.append(conn)
    try:
        while True:
            data=conn.recv(1024)
            if not data:
                break
            print(f'Saw: \'{data.decode()}\' || From: {adr}')
            broadcast(data)
    finally:
        clients.remove(conn)
        conn.close()
        print(f'Connection from {adr} closed')

def broadcast(message):
    for client in clients:
        client.sendall(message)

def main():
    local_ip = socket.gethostbyname(socket.gethostname())
    print(f'Your local ip is: {local_ip}')
    port=34874
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((local_ip, port))
    sock.listen(5)
    try:
        while True:
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
