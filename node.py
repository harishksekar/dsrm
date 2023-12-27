import socket
# from lib.cpu_utils import CPUUtils
from lib.disk_utils import DiskUtilization
from lib.cpu_utils import CPU_Utilization
from lib.mem_utils import Memory_Utilization

server = None

class Node(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_setup()
        self.disk_utils = DiskUtilization()
        self.cpu_utils = CPU_Utilization()
        self.mem_utils = Memory_Utilization()
        # print (self.mem_utils.get_memory_info())
        # print (self.cpu_utils.get_cpu_info())
        # print (self.disk_utils.get_disk_info())

    def server_setup(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 + TCP
        self.server.bind((self.host, self.port))
        self.server.listen(5) # 5 = maximum number of clients it can talk to, at a time

    def communicate(self):
        # return self.cpu_utils.get_cpu_info()

        while True:
            comm_socket, address = self.server.accept()
            msg = comm_socket.recv(1024).decode('utf-8')
            print ("Received message from client {}: {}".format(address, msg))
            comm_socket.send("Msg from server".encode('utf-8'))
            comm_socket.close()

def main():
    server = Node(host=socket.gethostbyname(socket.gethostname()), port=9191)
    return server.communicate()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass