# LAB SETUP GUIDE

## Overview
This document provides a comprehensive guide to configuring a test environment using three virtual machines (VMs). This setup aims to simulate an attack behavior simulator environment effectively.

## Requirements
- A hypervisor such as VMware, VirtualBox, or any other virtualization software.
- At least 16 GB of RAM.
- CPU with support for virtualization.

## Virtual Machines Configuration
### VM 1: Attacker VM
- **Operating System:** Kali Linux
- **Purpose:** This VM is used for launching attacks against the other VMs.
- **RAM:** 4 GB
- **CPUs:** 2
- **Network Configuration:** 
  - Adapter Type: Bridged
  - IP: Obtain automatically (DHCP)

### VM 2: Target VM 1
- **Operating System:** Windows Server 2019
- **Purpose:** This VM will serve as a target for attacks.
- **RAM:** 4 GB
- **CPUs:** 2
- **Network Configuration:** 
  - Adapter Type: Bridged
  - IP: Obtain automatically (DHCP)

### VM 3: Target VM 2
- **Operating System:** Ubuntu Server 20.04
- **Purpose:** This VM will also act as a target for attacks.
- **RAM:** 4 GB
- **CPUs:** 2
- **Network Configuration:** 
  - Adapter Type: Bridged
  - IP: Obtain automatically (DHCP)

## Step-by-Step Setup
1. **Create and Configure VMs:**
   - Using your virtualization software, create three virtual machines as per the specifications above.
2. **Install Operating Systems:**
   - Install the corresponding OS on each VM.
3. **Network Setup:**
   - Ensure all VMs are on the same network. Check the IP addresses assigned to each VM.
4. **Install Required Software:**
   - **Attacker VM:** Install penetration testing tools like Metasploit, Nmap, and Burp Suite.
   - **Target VMs:** Configure necessary services that can be exploited (e.g., web servers, databases).
5. **Testing the Setup:**
   - From the Attacker VM, try to ping the Target VMs to ensure connectivity.
   - Conduct basic tests to verify that the environment is functioning correctly.

## Conclusion
With this configuration, you should have a fully functional test environment set up with three virtual machines. This setup will simulate various attack scenarios effectively.