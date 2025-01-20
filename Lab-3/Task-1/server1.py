import socket
max_dataLength=16 #buffer
format="utf-8"
server_hostname=socket.gethostname()
server_ip=socket.gethostbyname(server_hostname)

listening_port=5050
server_socket_addr=(server_ip,listening_port)

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Obj creation

server.bind(server_socket_addr)

server.listen()
print("Server is listening")

while True:
    connection,client_addr=server.accept() #connection=socket obj
    print(f"Connected to {client_addr}")

    is_connected=True

    while is_connected:
        upcoming_data_length=connection.recv(max_dataLength).decode(format)
        print(f"Upcoming datalength is {upcoming_data_length}")
        if upcoming_data_length:
            data_length=int(upcoming_data_length)
            data=connection.recv(data_length).decode(format)
            
           
            if data=="disconnect":
                connection.send("Goodbye".encode(format))
                print(f"Disconnected with {client_addr}")
                is_connected=False
            else:

                print(data)
                connection.send("Message Received".encode(format))
    connection.close()


