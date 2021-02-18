import os
import time
import datetime
import statistics

def NowString():
    today = datetime.datetime.now()
    time = today.time().strftime('%H:%M:%S ')
    return time

def FileWrite(filepath, data):
    filename = os.path.join(str(filepath), "dataFile.txt")
    with open(filename, 'a') as f:
        f.write(NowString())
        f.write(data)
        f.write("\n")
        f.close()

def FolderCreate(today):
    todaystr = today.isoformat()

    parent_directory = "/home/pi/Desktop/Hatchery/TestData"
    path = os.path.join(parent_directory, todaystr)
    try:
        os.mkdir(path)
    except OSError:
        print ("The folder %s is already created" % path)
    else:
        print ("Successfully created the directory %s " % path)
    return path

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

def servRead():
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
        return l_av
