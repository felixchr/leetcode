import time

def tail(filename, interval=1.0):
    #inteval
    f = open(filename)
    f.seek(2)
    while True:
        where = f.tell()
        line = f.readline()
        if not line:
            time.sleep(interval)
            f.seek(where)
        else:
            yield line