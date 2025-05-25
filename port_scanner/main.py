import socket
import sys
from datetime import datetime
import argparse
import threading
from concurrent.futures import ThreadPoolExecutor


#Input
parser = argparse.ArgumentParser()
parser.add_argument('target', help="IP submask to scan")
parser.add_argument('-p','--sport', type=int, help="Starting port")
parser.add_argument('-P', '--fport', type=int, help="Finishing port")
args = parser.parse_args()

def scan_ports(port:int) -> None:
    try:
            for ip in range(1,256):
                targetIP = socket.gethostbyname(args.target + '.{}'.format(ip))
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.2)
                if sock.connect_ex((targetIP, port))==0:
                    print(f" {targetIP}:{port} is open")
                sock.close()

    except KeyboardInterrupt:
        sys.exit()
    except socket.gaierror:
        print(f"Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()


start_time=datetime.now()
#for 1000 ports
with ThreadPoolExecutor(max_workers=1000) as pool:
    pool.map(scan_ports, range(1, 1000))
finish_time=datetime.now()


time_spent=finish_time-start_time
print("Took: {}".format(time_spent))

