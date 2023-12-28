import os
import socket
import json
import time
import argparse

from lib.byte_utils import size_in_human_readable

HOST = socket.gethostbyname(socket.gethostname())
# PORT = 9191

def get_client_node(port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, port))
    except ConnectionRefusedError:
        print ("Warning: Node Server {} not running on {}".format(HOST, port))
        return None
    return client

def print_all_metrics(all_metrics):
    os.system('clear')
    dash_cnt = 138
    main_fmt = "|{:^10}|{:^5}|{:^39}|{:^39}|{:^39}|"
    print ('-' * dash_cnt)
    print (main_fmt.format("Host", "Port", "Disk", "Memory", "CPU"))
    print ('-' * dash_cnt)

    each_metric_fmt="{:^12}|{:^12}|{:^7}|{:^5}"
    metrics_fmt="|{:^10}|{:^5}|"+each_metric_fmt+"|"+each_metric_fmt+"|"+each_metric_fmt+"|"
    print(metrics_fmt.format("", "",
                             "Total", "Used", "Free", "%",
                             "Total", "Used", "Free", "%",
                             "Total", "Load", "Ctx Sw", "INTR"))
    print ('-' * dash_cnt)

    for host_port, metrics in all_metrics.items():
        host, port = host_port.split("_")
        disk_metrics = metrics["disk"] 
        mem_metrics = metrics["memory"]
        cpu_metrics = metrics["cpu"]

        # disk metrics
        disk_total = size_in_human_readable(disk_metrics["total"])
        disk_used = size_in_human_readable(disk_metrics["used"])
        disk_free = size_in_human_readable(disk_metrics["free"])
        disk_percent = disk_metrics["percent"]

        # memory metrics
        mem_total = size_in_human_readable(mem_metrics["total"])
        mem_used = size_in_human_readable(mem_metrics["used"])
        mem_free = size_in_human_readable(mem_metrics["free"])
        mem_percent = mem_metrics["percent"]
        
        # cpu metrics
        cpu_total = cpu_metrics["total"]
        cpu_load = cpu_metrics["load"]
        cpu_ctx_sw = size_in_human_readable(cpu_metrics["ctx_sw"], suffix="")
        cpu_intr = size_in_human_readable(cpu_metrics["intr"], suffix="")
        print (metrics_fmt.format(host, port,
                disk_total, disk_used, disk_free, disk_percent,
                mem_total, mem_used, mem_free, mem_percent,
                cpu_total, cpu_load, cpu_ctx_sw, cpu_intr
                ))
    print ('-' * dash_cnt)
        
def main():
    parser = argparse.ArgumentParser(description="Admin Server")
    parser.add_argument('--nports', action="store", dest="nports",
                        type=int, nargs = '+',
                        help="Ports of node servers (for Demo purpose)")
    args = parser.parse_args()
    print ("Connecting to node server on {}".format(args.nports))
    while True:
        all_metrics = {}
        for node_port in args.nports:
            client_node = get_client_node(node_port)
            if not client_node:
                continue

            client_node.send("get_metrics".encode('utf-8'))
            msg = client_node.recv(1024).decode('utf-8')
            msg = msg.replace("'", '"')
            client_metrics = json.loads(msg)
            all_metrics[str(HOST)+"_"+str(node_port)] = client_metrics
            # print (json.dumps(metrics, indent=4))
        print_all_metrics(all_metrics)
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass