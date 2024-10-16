import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 61616

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(512)
            if not data:
                break
            expr = data.decode('utf-8')
            result = str(eval(expr))
            conn.sendall(result.encode('utf-8'))
