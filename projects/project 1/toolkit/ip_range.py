import sys
import time
from socket import *


if __name__ == '__main__':

    args = sys.argv[1:]
    ip = args[0]
    start = int(args[1])
    end = int(args[2])
    # ip = "82.115.20.167"
    # start = 160
    # end = 170

    startTime = time.time()
    for i in range(start, end + 1):

        # Create subnet address
        ip = ".".join(ip.split(".")[:3]) + "." + str(i)
        _socket = socket(AF_INET, SOCK_STREAM)

        conn = _socket.connect_ex((ip, 80))
        if conn == 0:
            print(f"{ip} --> Live")
        # else:
        #     print(f"{ip} --> Dead")
        _socket.close()

    print('scanning complete in ', time.time() - startTime)