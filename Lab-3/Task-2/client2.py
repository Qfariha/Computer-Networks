import socket
format="utf-8"
max_dataLength=16
server_hostname=socket.gethostname()
server_ip=socket.gethostbyname(server_hostname)

listening_port=5050
server_socket_addr=(server_ip,listening_port)


client_hostname=socket.gethostname()
client_ip=socket.gethostbyname(client_hostname)

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(server_socket_addr)

def send_message(data):
    dataEncoded= data.encode(format)
    dataLengthInt=len(data)
    dataLengthStr=str(dataLengthInt)

    additional_space_length= max_dataLength-len(dataLengthStr)

    dataLengthStr+=" "*additional_space_length

    dataLengthEncoded= dataLengthStr.encode(format)
    client.send(dataLengthEncoded)
    client.send(dataEncoded)

   
    received_from_server=client.recv(2048).decode(format)
    print(f"Received from server: {received_from_server}")

while True:
    inp=input("Enter a message: ")
    if inp=="End":
        send_message("disconnect")
        break
    else:
        send_message(inp)