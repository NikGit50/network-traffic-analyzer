# To import libraries
import csv
from scapy.all import rdpcap, IP, TCP, UDP, DNS

# To extract data
packets = rdpcap("sample_traffic.pcap")

# Counters
protocol_counts = {
    "TCP": 0,
    "UDP": 0,
    "DNS": 0,
    "Other": 0
}

# Directory to store the results
results = []

print("\n===== NETWORK TRAFFIC ANALYZER =====")

for packet in packets:
  if IP in packet:
    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    packet_size = len(packet)

    if DNS in packet:
      protocol = "DNS"
    elif TCP in packet:
      protocol = "TCP"
    elif UDP in packet:
      protocol = "UDP"
    else:
      protocol = "Other"

    protocol_counts[protocol] += 1

    print(f"Source: {source_ip}")
    print(f"Destination: {destination_ip}")
    print(f"Protocol: {protocol}")
    print(f"Packet Size: {packet_size} bytes")
    print("-" * 40)

    results.append([
      source_ip,
      destination_ip,
      protocol,
      packet_size
    ])

print("\n===== PROTOCOL SUMMARY =====")

for protocol, count in protocol_counts.items():
  print(f"{protocol}: {count}")

print(f"\nTotal Packets: {len(packets)}")

with open("analysis_result.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Source IP",
        "Destination IP",
        "Protocol",
        "Packet Size (bytes)"
    ])

    writer.writerows(results)

print("\nCSV file created successfully!")