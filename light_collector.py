import socket
import time
import datetime

import util

PORT = 6000
SERVER = "192.168.0.22"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def light_collector():
    # Read and record the data
    currentDay = datetime.date.today()
    path = util.FolderCreate(currentDay)
    if currentDay != datetime.date.today():
        currentDay = datetime.date.today()
        path = util.FolderCreate(currentDay)
    l = util.servRead(server)
    string = f"{l}"
    util.FileWrite(path, string)
    time.sleep(288)            # wait 5 minutes
    return

def start():
    server.listen()
    print(f"Server is listening on {SERVER} port {PORT}")
    while True:
        light_collector()

print('Waiting for client connection...')

try:
    start()
except KeyboardInterrupt:
    print('stopping...')
