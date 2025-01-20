import socket
import threading
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

def handle_clients(connection, client_addr):
    #connection,client_addr=server.accept() 
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
                data1=int(data)
                if data1<=40:
                    salary=(data1)*200
                    connection.send(f'{salary}'.encode(format))
                elif data1>40:
                    salary=8000+ ((data1-40)*300)
                    connection.send(f'{salary}'.encode(format))


#Different clients in different threads
while True:
    connection,client_addr=server.accept()
    thread= threading.Thread(target= handle_clients, args= (connection, client_addr)) 
    thread.start()