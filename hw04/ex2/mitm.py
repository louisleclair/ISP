from netfilterqueue import NetfilterQueue
import scapy.all as scapy
from scapy.layers.inet import IP, TCP


def print_and_accept(packet):
    packet.accept()
    ip = scapy.IP(packet.get_payload())
    if ip.haslayer(scapy.TCP):
        print(ip.show())

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
    