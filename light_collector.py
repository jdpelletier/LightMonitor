import time
import datetime

import util

def light_collector():
    # Read and record the data
    currentDay = datetime.date.today()
    path = util.FolderCreate(currentDay)
    if currentDay != datetime.date.today():
        currentDay = datetime.date.today()
        path = Util.FolderCreate(currentDay)
    l = util.servRead()
    string = f"{l}"
    Util.FileWrite(path, string)
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
