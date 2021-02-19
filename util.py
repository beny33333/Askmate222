import time

def conver_UNIX_to_datetime(UNIX_time):
    return time.strftime("%D %H:%M", time.localtime(int(UNIX_time)))