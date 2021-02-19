import socket
import threading
import time
import statistics

PORT = 6000
SERVER = "192.168.0.22"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client():
    l = []
    for i in range(10):
        conn, addr = server.accept()
        msg = conn.recv(1024).decode()
        print(f"{msg}")
        l.append(float(msg))
        conn.close()
        time.sleep(1)
        i += 1
    l_av = statistics.mean(l)
    print(f"{l_av}")


def start():
    server.listen()
    print(f"Server is listening on {SERVER} port {PORT}")
    while True:
        handle_client()
        # thread = threading.Thread(target=handle_client, args=(conn, addr))
        # thread.start()
        # print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print('Waiting for client connection...')
try:
    start()
except KeyboardInterrupt:
    print('stopping...')
