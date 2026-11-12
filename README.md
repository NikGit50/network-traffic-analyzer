# Network Traffic Analyzer Using Python and Scapy

## Overview

A Python-based cybersecurity project developed using Python and Scapy to analyze network packets from PCAP files. The tool extracts packet information, identifies network protocols, analyzes network ports, calculates traffic statistics, and exports results to CSV format.

The project was developed in two stages: offline PCAP analysis and separate live network traffic analysis in a Linux environment.

## Features

### 1. Offline PCAP Analysis

- Reads network packets from PCAP files.
- Extracts source and destination IP addresses.
- Identifies TCP, UDP, and DNS packets.
- Extracts DNS query domain names.
- Calculates individual packet sizes.
- Extracts source and destination ports.
- Performs basic service identification using port numbers.
- Supports protocol-based filtering.
- Calculates protocol counts and percentages.
- Calculates total packet count and data size.
- Exports analysis results to CSV format.

### 2. Live Network Traffic Analysis

Live traffic analysis was developed and tested separately in a Linux/Xubuntu virtual machine.

- Captures live network packets using Scapy's `sniff()` function.
- Uses network interface selection for packet capture.
- Supports packet-count and timeout-based capture.
- Analyzes captured TCP, UDP, and DNS traffic.
- Extracts source and destination IP addresses.
- Extracts DNS query domain names.
- Extracts source and destination ports.
- Performs basic service identification.
- Generates CSV reports containing captured traffic information.
- Calculates protocol statistics and total captured data size.

**Note:** The live traffic capture implementation is maintained separately and is not included in this public repository.

## Technologies and Libraries Used

- **Python:** Main programming language.
- **Scapy:** Packet manipulation, PCAP processing, protocol analysis, and live packet capture using `sniff()`.
- **CSV Module:** Exporting packet analysis results.
- **PCAP:** Packet capture file format used for offline analysis.

## Project Structure

```text
network-traffic-analyzer/
│
├── .gitignore
├── README.md
├── requirements.txt
├── create_sample.py
├── main.py
├── sample_traffic.pcap
└── sample_analysis_result.csv
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/NikGit50/network-traffic-analyzer.git
```

### 2. Navigate to the project directory

```bash
cd network-traffic-analyzer
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```cmd
.venv\Scripts\activate
```

**Linux:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Generate Synthetic Network Traffic

```bash
python create_sample.py
```

This generates a synthetic PCAP file named `sample_traffic.pcap`.

### Run the Offline Analyzer

```bash
python main.py
```

The analyzer processes the PCAP file and exports the analysis results to a CSV file.

## Live Traffic Analysis – Development Details

Live traffic analysis was implemented and tested separately in a Linux/Xubuntu virtual machine using the Scapy library.

The primary Scapy function used for live packet capture was:

```python
sniff(iface="enp0s3", count=20, timeout=50)
```

Where:

- `iface`: Specifies the network interface used for packet capture.
- `count`: Specifies the maximum number of packets to capture.
- `timeout`: Specifies the maximum capture duration in seconds.

The captured packets were subsequently analyzed to identify protocols, extract network information, calculate traffic statistics, and generate CSV reports.

The live-capture implementation is not distributed in this public repository.

## Sample Output

The offline analyzer generates a CSV report containing:

| Field | Description |
|---|---|
| Source IP | Packet source IP address |
| Destination IP | Packet destination IP address |
| Protocol | Identified network protocol |
| Packet Size | Size of the packet in bytes |
| Domain Name | Extracted DNS query domain |
| Destination Port | Destination port number |
| Source Port | Source port number |
| Services | Basic service identification |

## Learning Objectives

- Understanding network packet structures.
- Learning TCP, UDP, and DNS protocol identification.
- Working with PCAP files.
- Using Scapy for packet analysis.
- Understanding network ports and service identification.
- Implementing protocol-based filtering.
- Calculating network traffic statistics.
- Learning live packet capture concepts using Scapy's `sniff()` function.
- Exporting packet analysis data using Python.

## Project Status

**Offline PCAP Analysis:** Developed and tested.

**Live Traffic Analysis:** Developed and tested separately in a Linux/Xubuntu virtual machine.

**Public Repository:** Focuses on offline PCAP analysis using synthetic network traffic.

## Ethical Considerations

This project is intended for educational and defensive cybersecurity learning. Live traffic analysis was performed in a controlled virtual-machine environment. Packet capture should only be conducted on networks where proper authorization has been obtained.

## Disclaimer

This project is developed for educational and authorized cybersecurity analysis. The public repository does not include the live packet-capture implementation or real captured network traffic.

## Author

**Nikhil Kumar Gupta**

Computer Science and Engineering Student

GitHub: https://github.com/NikGit50
