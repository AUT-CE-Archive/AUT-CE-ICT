import json
import socket

HOST = "127.0.0.1"  # Localhost
PORT = 62412        # A random non-priveleged port

def serialize(data: dict) -> bytes:
    """ Serializes a dictionary into a JSON string """
    return json.dumps(data).encode('utf-8')

def deserialize(data: bytes) -> dict:
    """ Deserializes a JSON string into a dictionary """
    return json.loads(data.decode('utf-8'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:

            # Request malware data
            conn.sendall(b"sysinfo")
            data = conn.recv(1024)
            sysinfo = deserialize(data)
            print(sysinfo)

            # Terminate malware connection
            conn.sendall(b"exit")
            break