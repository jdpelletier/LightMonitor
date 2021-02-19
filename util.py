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

    parent_directory = "/home/pi/Desktop/Apps/FireBeetleTesting/LightMonitor/TestData"
    path = os.path.join(parent_directory, todaystr)
    try:
        os.mkdir(path)
    except OSError:
        pass
    else:
        print ("Successfully created the directory %s " % path)
    return path


def servRead(server):
        l = []
        for i in range(10):
            conn, addr = server.accept()
            msg = conn.recv(1024).decode()
            l.append(float(msg))
            conn.close()
            time.sleep(1)
            i += 1
        l_av = statistics.mean(l)
        return l_av
