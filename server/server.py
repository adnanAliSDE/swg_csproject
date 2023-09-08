import socket

s = socket.socket()

print("Created a socket")
s.bind(("0.0.0.0", 9090))

s.listen(2)
print("Listening on 9090...")

while True:
    conn, addr = s.accept()
    print("Connected with ", addr)
    data = conn.recv(1024).decode()
    print(data)
    conn.send(b"Welcome to SWG")

s.close()