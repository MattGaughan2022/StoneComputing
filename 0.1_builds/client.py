import socket
import cv2
import os

from PIL import Image

BUFFER_SIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input(str("Please enter the host address of the sender : "))
port = 8080
client.connect((host,port))
print("Connected ... ")

#filename = input(str("Please enter a filename for the incoming file : "))
#file = open(filename, 'wb')
#file_data = s.recv(2048)
#file.write(file_data)
##filename = input(str("Please enter a filename for the incoming file : "))
#ile = open(filename, 'rb')
#image_data = file.read(4096)
##while image_data:
#    client.send(image_data)
#    image_data = file.read(4096)
##file.show()

with open('client_file.png', 'rb') as file:
    file_data = file.read(BUFFER_SIZE)

    while file_data:
        client.send(file_data)
        file_data = file.read(BUFFER_SIZE)

client.send(b"%IMAGE_COMPLETED%")

with open('client_file_edited.png', 'wb') as file:
    recv_data = client.recv(BUFFER_SIZE)

    while recv_data:
        file.write(recv_data)
        recv_data = client.recv(BUFFER_SIZE)

        if recv_data == b"%IMAGE_COMPLETED%":
                break

print("File has been received successfully.")
#img = cv2.imread(filename)
#cv2.imshow('Test', image_data)
#cv2.waikKey(0)
#cv2.destroyAllWindows
#file.close()
client.close()

