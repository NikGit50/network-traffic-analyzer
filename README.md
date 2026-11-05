# Network Traffic Analyzer Using Python and Scapy

## Overview
A beginner-friendly cybersecurity project developed using Python and Scapy to analyze network packets from PCAP files. The tool identifies network protocols, extracts packet information, displays protocol statistics, and exports analysis results to a CSV file.

## Features
- Reads network packets from PCAP files.
- Extracts source and destination IP addresses.
- Identifies TCP and DNS packets.
- Calculates packet sizes.
- Counts packets by protocol.
- Exports packet analysis results to CSV format.

## Technologies Used
- Python
- Scapy
- CSV Module
- PCAP (Packet Capture)

## Project Structure
```text
network-traffic-analyzer/
│
├── main.py
├── create_sample.py
├── sample_traffic.pcap
├── analysis_result.csv
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone (https://github.com/NikGit50/network-traffic-analyzer)
```

2. Navigate to the project directory:
```bash
cd network-traffic-analyzer
```

3. Create a virtual environment:
```bash
python -m venv .venv
```

4. Activate the virtual environment:

Windows:
```cmd
.venv\Scripts\activate
```

Linux:
```bash
source .venv/bin/activate
```

5. Install Scapy:
```bash
pip install scapy
```

## Usage

Generate synthetic network traffic:
```bash
python create_sample.py
```

Run the analyzer:
```bash
python main.py
```

The analyzer processes the generated PCAP file and creates `analysis_result.csv`.

## Sample Output

```text
===== PROTOCOL SUMMARY =====
TCP: 2
UDP: 0
DNS: 2
Other: 0

Total Packets: 4

CSV file created successfully!
```

## Learning Objectives
- Understanding network packet structures.
- Learning TCP and DNS protocol identification.
- Working with PCAP files.
- Using Scapy for packet analysis.
- Exporting network analysis data using Python.

## Project Status
**Ongoing Development**

Future improvements:
- DNS domain extraction.
- Live network traffic capture.
- Advanced protocol identification.
- Network traffic statistics and visualization.
- Suspicious traffic detection.

## Disclaimer
This project is developed for educational and cybersecurity learning purposes. Live packet capture and analysis should only be performed on networks where you have authorization.

## Author
Nikhil Gupta

Computer Science and Engineering Student

GitHub: Add your GitHub profile URL here
