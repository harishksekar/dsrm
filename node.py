import socket
from lib.disk_utils import DiskUtilization
from lib.cpu_utils import CPU_Utilization
from lib.mem_utils import Memory_Utilization

server = None

class Node(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect_to_admin()
        self.disk_utils = DiskUtilization()
        self.cpu_utils = CPU_Utilization()
        self.mem_utils = Memory_Utilization()
        # print (self.mem_utils.get_memory_info())
        # print (self.cpu_utils.get_cpu_info())
        # print (self.disk_utils.get_disk_info())

    def connect_to_admin(self):
        self.admin = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 + TCP
        self.admin.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.admin.bind((self.host, self.port))
        self.admin.listen(5) # 5 = maximum number of clients it can talk to, at a time

    def communicate(self):
        while True:
            print ("Ready to accept...")
            comm_socket, address = self.admin.accept()
            msg = comm_socket.recv(1024).decode('utf-8')
            # print ("Received message from client {}: {}".format(address, msg))
            # comm_socket.send("Msg from server".encode('utf-8'))
            metrics = {}
            if msg == "get_metrics":
                metrics["disk"] = self.disk_utils.get_disk_info()
                metrics["memory"] = self.mem_utils.get_memory_info()
                metrics = str(metrics)

                comm_socket.send(metrics.encode('utf-8'))
            comm_socket.close()

def main():
    node = Node(host=socket.gethostbyname(socket.gethostname()), port=9191)
    return node.communicate()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass