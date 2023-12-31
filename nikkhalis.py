import socket

def send_student_id(student_id):
    try:
        # Server address and port
        server_address = 'izani.synology.me'
        server_port = 8443

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect((server_address, server_port))

       
        client_socket.send(student_id.encode())

        
        response = client_socket.recv(1024).decode()
        print("Server response:", response)

        client_socket.close()
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    student_id = '2022943033'  
    send_student_id(student_id)
