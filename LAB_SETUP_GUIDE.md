# LAB SETUP GUIDE

## Overview
This guide provides comprehensive instructions for setting up a 3-VM testing environment for the Attack Behavior Simulator. The environment includes three virtual machines (VMs) configured to work together for testing purposes.

## VM Architecture
- **VM1**: Attack Simulator
- **VM2**: Target Machine
- **VM3**: Monitoring and Logging

### Resources Needed
- Hypervisor (e.g., VMware, VirtualBox)
- Minimum of 8GB RAM for each VM
- Network connectivity between VMs

## Installation Steps
1. **Create VMs**
   - Allocate resources as per the specifications above.
   - Install the OS (e.g., Ubuntu 20.04 LTS) on each VM.

2. **Install Required Packages**
   - For Ubuntu, run:
     ```bash
     sudo apt update
     sudo apt install -y package-name
     ```
   - Ensure that the necessary packages for the Attack Behavior Simulator are installed on VM1, and any software needed on other VMs is set up accordingly.

## Network Configuration
1. **Ensure Internal Network**
   - Configure all VMs to be on the same internal network for communication.

2. **Assign Static IPs**
   - For example:
     - VM1: 192.168.1.2
     - VM2: 192.168.1.3
     - VM3: 192.168.1.4

3. **Set up Hostnames**
   - Assign hostnames for easier access:
     - VM1: attack-simulator
     - VM2: target-machine
     - VM3: monitor-logger

## Service Setup
1. **Configure VMs for the Necessary Services**
   - Install and configure any services needed for the attack simulations and monitoring.
   - For example, you may want to install `nmap`, `tcpdump` on VM1 and set up specific services on VM2 as the target machine.

## Monitoring
1. **Install Monitoring Tools**
   - On VM3, install tools like Grafana or Prometheus if needed.
   - Configure these tools to monitor network traffic and service health across VMs.

## Troubleshooting
1. **Network Issues**
   - Check IP assignments and ensure VMs are on the same subnet.
   - Use commands like `ping` to test connectivity.

2. **Service Failures**
   - Monitor service logs on each VM for errors.
   - Restart services as needed and verify configurations.

## Conclusion
Following this guide will set up a robust testing environment for simulating attacks and monitoring responses. Ensure each step is followed carefully for a successful setup.