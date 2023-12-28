import socket, json, ast

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9191
client = None

def connect_to_node():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print ("Warning: Server {} not running on {}".format(HOST, PORT))
        return False
    return True

def main():
    if connect_to_node():
        client.send("get_metrics".encode('utf-8'))
        msg = client.recv(1024).decode('utf-8')
        # print ("msg = {}, type = {}".format(msg, type(msg)))
        metrics = ast.literal_eval(json.dumps(msg))
        print (metrics)
        # print ("Message sent successfully!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass