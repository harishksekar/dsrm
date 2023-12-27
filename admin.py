import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9191
client = None

def setup_client():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print ("Warning: Server {} not running on {}".format(HOST, PORT))
        return False
    return True

def main():
    global server
    if setup_client():
        client.send("Hello from client boss!!".encode('utf-8'))
        print ("Message sent successfully!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass