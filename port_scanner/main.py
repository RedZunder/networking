import socket
import sys
from datetime import datetime
import argparse
from ipaddress import IPv4Network
from concurrent.futures import ThreadPoolExecutor
from scapy.all import sr1, IP, ICMP

# Input
parser = argparse.ArgumentParser()
parser=argparse.ArgumentParser(prog='Network scanner')
parser.add_argument('target', help="IP submask to scan, e.g. 192.168.1.0/24")
parser.add_argument('-p','--sport', type=int, help="Starting port")
parser.add_argument('-P','--fport', type=int, help="Finishing port")
parser.add_argument('-v','--verbose', action="store_true", help="Increase verbosity")

args = parser.parse_args()

'''
By finding first the active IPs, we reduce the number of scans done later in the 'scan_ports' function
Instead of 256 IPs * 5000 ports, we do around 3 IPs * 5000 ports
'''

def find_active_ips(network_cidr: str, timeout: float = 1.0, max_workers: int = 256) -> list[str]:
    net = IPv4Network(network_cidr)
    hosts = [str(ip) for ip in net.hosts()]
    active = []

    def ping(host: str) -> str | None:
        pkt = sr1(IP(dst=host)/ICMP(), timeout=timeout, verbose=False)
        return host if pkt is not None else None

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        for result in pool.map(ping, hosts):
            if result:
                active.append(result)

    return active

def scan_ports(port: int, ips: list[str]) -> None:
    for ip in ips:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                print(f"{ip}:{port} is open")
        except Exception as e:
            print(f"{ip}:{port}: {e}")
            pass
        finally:
            sock.close()

if __name__ == "__main__":
    start_time = datetime.now()

    # Discover which hosts are up
    active_ips = find_active_ips(args.target, timeout=0.5, max_workers=256)

    if args.verbose:        #extra info
        print("Reachable hosts:")
        for ip in active_ips:
            print(" -", ip)

    # Determine port range
    start_port = args.sport or 1
    end_port   = args.fport or 5000

    if args.sport:
        print(f"Starting port: {args.sport}")
    if args.fport:
        print(f"Ending port: {args.fport}")

    # Scan each port across all active IPs in parallel
    with ThreadPoolExecutor(max_workers=200) as pool:
        pool.map(lambda p: scan_ports(p, active_ips), range(start_port, end_port + 1))

    finish_time = datetime.now()
    print(f"Took: {finish_time - start_time}")
