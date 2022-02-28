import socket

IP = socket.gethostbyname(socket.gethostname())
port = 8080
addr = (IP, port)
format = "utf-8"
size = 1024


"Starting a TCP socket"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"Connecting to the server"
client.connect(addr)

"Opening and reading the file data"
file = open("test.txt", "r")
data = file.read()

"Sending the filename to the server"
client.send("test.txt".encode(format))
msg = client.recv(size).decode(format)
print(f"[server]: {msg}")

"Transmitting file data to server"
client.send(data.encode(format))
msg = client.recv(size).decode(format)
print(f"[server]: {msg}")

"Closing the file"
file.close()

"Severing connection"
client.close()
