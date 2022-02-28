import socket

IP = socket.gethostbyname(socket.gethostname())
port = 8080
addr = (IP, port)
format = "utf-8"
size = 1024

print("[STARTING] Server is starting.")
"Starting a TCP socket."
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"Bind the IP and port to server"
server.bind(addr)

"Server is waitin for connection request."
server.listen()
print(f"[LISTENING] Server is waiting at {IP} : {port}.")

while True:
    "Connection between server and client is successful."
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected")

    "Receiving the filename"
    filename = conn.recv(size).decode(format)
    print(f"[RECV] Receiving file name")
    file = open("server_user_data/"+filename, "w")
    conn.send("Filename Received.".encode(format))

    "Receiving the data of the file"
    data = conn.recv(size).decode(format)
    print(f"[RECV] Receiving file data")
    file.write(data)
    conn.send("File data Received.".encode(format))

    "Closing file"
    file.close()

    "Severing Connection"
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected from server.")
    server.close(port)