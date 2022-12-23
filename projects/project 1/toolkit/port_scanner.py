import sys
import time
from socket import *


if __name__ == '__main__':

    # Arguments
    args = sys.argv[1:]
    ip = args[0]
    starting_port = int(args[1])
    ending_port = int(args[2])

    startTime = time.time()
    # for port in [20, 22, 80, 81, 100]:
    for port in range(starting_port, ending_port):
        _socket = socket(AF_INET, SOCK_STREAM)

        conn = _socket.connect_ex((ip, port))
        if conn == 0:
            print(f"Port Open: --> {port}")
        # else:
        #     print(f"Port Closed: --> {port}")
        _socket.close()

    print('scanning complete in ', time.time() - startTime)