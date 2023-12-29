import sys
import socket
import argparse

from lib.disk_utils import DiskUtilization
from lib.cpu_utils import CPU_Utilization
from lib.mem_utils import Memory_Utilization

server = None

class NodeServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect_to_admin()
        self.disk_utilz = DiskUtilization()
        self.cpu_utilz = CPU_Utilization()
        self.mem_utilz = Memory_Utilization()
        self.request_id = 0
        # print (self.mem_utilz.get_memory_info())
        # print (self.cpu_utilz.get_cpu_info())
        # print (self.disk_utilz.get_disk_info())

    def connect_to_admin(self):
        self.admin = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 + TCP
        self.admin.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.admin.bind((self.host, self.port))
        except socket.error as e:
            print (str(e))
            sys.exit(-1)
        self.admin.listen(5) # 5 = maximum number of clients it can talk to, at a time

    def communicate(self):
        print ("Node server ready to communicate...")
        while True:
            comm_socket, address = self.admin.accept()
            print ("[Request ID: {:3} - Connection from {}".format(self.request_id, address))
            self.request_id += 1
            msg = comm_socket.recv(1024).decode('utf-8')
            # print ("Received message from client {}: {}".format(address, msg))
            # comm_socket.send("Msg from server".encode('utf-8'))
            metrics = {}
            if msg == "get_metrics":
                metrics["disk"] = self.disk_utilz.get_disk_info()
                metrics["memory"] = self.mem_utilz.get_memory_info()
                metrics["cpu"] = self.cpu_utilz.get_cpu_info()
                metrics = str(metrics)

                comm_socket.send(metrics.encode('utf-8'))
            comm_socket.close()

def main():
    parser = argparse.ArgumentParser(description="Node Server")
    parser.add_argument('--port', action="store", dest="port", type=int, default=9191,
                        help="Port to run node server on")
    args = parser.parse_args()
    node = NodeServer(host=socket.gethostbyname(socket.gethostname()),
                port=args.port)
    return node.communicate()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
