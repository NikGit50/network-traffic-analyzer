# Import the libraries required
from scapy.all import Ether, DNS,TCP,IP,UDP,DNSQR,wrpcap

# Packet Directory
packet=[
  Ether() /IP(src="198.0.2.10" ,dst="198.51.100.20") /TCP(sport=51515, dport=443, flags="S"),
  Ether() /IP(src="198.0.2.11" ,dst="192.0.2.1") /UDP(sport=53000, dport=53) /DNS(rd=1, qd=DNSQR(qname="example.com")),
  Ether()/IP(src="198.0.2.12" ,dst="198.51.100.30")/TCP(sport=52000, dport=80, flags="S"),
  Ether() /IP(src="198.0.2.11" ,dst="192.0.2.1") /UDP(sport=53001, dport=53) /DNS(rd=1, qd=DNSQR(qname="google.com"))
]

# To store the data in sample traffic file
wrpcap("sample_traffic.pcap", packet)

print("Sythentic Data network traffic created successfully")
print("Total packets: ",len(packet))