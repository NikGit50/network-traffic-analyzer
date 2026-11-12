# To import essential libraries
import csv
from scapy.all import rdpcap, IP, TCP, UDP, DNS,DNSQR

# To extract data
packets = rdpcap("sample_traffic.pcap")

# Counters for detction of types of protocol in captured packets
protocol_counts = {
    "TCP": 0,
    "UDP": 0,
    "DNS": 0,
    "Other": 0
}
# To Detect type of service captured packet belongs
service_port = {
  22:"SSH",
  80:"HTTP",
  443:"HTTPS",
  53:"DNS"
}
Service="UNKNOWN"

# Directory to store the results
results = []

print("\n===== NETWORK TRAFFIC ANALYZER =====")

for packet in packets:
  if IP in packet:
    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    packet_size = len(packet)
    destination_port=packet[IP].dport
    source_port=packet[IP].sport
    domain=""
    
    if DNS in packet:
      protocol = "DNS"
      if DNSQR in packet and packet[DNS].qd:
        domain=packet[DNSQR].qname.decode(errors="replace")
        print("Domain name: ",domain)
    elif TCP in packet:
      protocol = "TCP"
    elif UDP in packet:
      protocol = "UDP"
    else:
      protocol = "Other"

# To indentify network services
    if destination_port in service_port:
      Service=service_port[destination_port]
    elif source_port in service_port:
      Service=service_port[source_port]
    protocol_counts[protocol] += 1

    print(f"Source: {source_ip}")
    print(f"Destination: {destination_ip}")
    print(f"Protocol: {protocol}")
    print(f"Packet Size: {packet_size} bytes")
    print("-" * 40)

# Packet Filtering 
    target_protocol="ALL"
    if target_protocol!="ALL" and protocol!=target_protocol:
      continue
    results.append([
      source_ip,
      destination_ip,
      protocol,
      packet_size,
      domain,
      destination_port,
      source_port,
      Service
    ])
    
print("\n===== PROTOCOL SUMMARY =====")

for protocol, count in protocol_counts.items():
  percentage=(count/len(packets)) * 100
  print(f"{protocol}: {count}, ({percentage:.2f} %)")

print(f"\nTotal Packets: {len(packets)}")
total_bytes=sum(row[3] for row in results)
print("Total bytes captured: ", total_bytes)

# To Generate data in csv file
with open("analysis_result.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Source IP",
        "Destination IP",
        "Protocol",
        "Packet Size (bytes)",
        "Domain Name",
        "Destination port",
        "Source Port",
        "Services"
    ])

    writer.writerows(results)

print("\nCSV file created successfully!")
print("================================")
