import socket
import cv2
import os
import io

from PIL import Image
from PIL import ImageFilter

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
server.bind((host,port))
server.listen()
print(host)
print("Waiting for incoming connections...")

client_socket, client_address = server.accept()
print(client_address, "Has connected to the server")
BUFFER_SIZE = 4096

while True:
    client_socket, _ = server.accept()
    filename = input(str("Please enter the file name of the file : "))

    file_stream = io.BytesIO()
    recv_data = client_socket.recv(BUFFER_SIZE)

    while recv_data:
        file_stream.write(recv_data)
        recv_data = client_socket.recv(BUFFER_SIZE)

        if recv_data == b"%IMAGE_COMPLETED%":
            break
    
    image = Image.open(file_stream)
    image = image.filter(ImageFilter.GaussianBlur(radius=10))

    image.tobytes()
    image.save('server_file.png', format='PNG')

    with open('server_file.png', 'rb') as file:
        file_data = file.read(BUFFER_SIZE)

        while file_data:
            client_socket.send(file_data)
            file_data = file.read(BUFFER_SIZE)

    client_socket.send(b"%IMAGE_COMPLETED")



#conn.send(file_chunk)
file.close()
print("Data has been transmitted successfully")