import nmap

# Initialize the Nmap Port Scanner
nm = nmap.PortScanner()

def characterize_attack_surface(target):
    """Characterizes the attack surface of a given target using Nmap."""
    nm.scan(target)
    print(f"Scanning {target}...")
    
    # Print general information about the target
    print(f"Host: {nm[target].hostname()}")
    print(f"State: {nm[target].state()}")
    
    # Get all protocols
    for proto in nm[target].all_protocols():
        print(f"Protocol: {proto}")
        lport = list(nm[target][proto].keys())
        lport.sort()
        for port in lport:
            print(f"Port: {port}	State: {nm[target][proto][port]['state']}")

def identify_vulnerabilities(target):
    """Identifies vulnerabilities on a target using Nmap's scripting engine."""
    nm.scan(target, arguments='--script vuln')
    print(f"Identifying vulnerabilities on {target}...")
    for script in nm[target].scripts:
        print(f"Script: {script} | Output: {nm[target].scripts[script]}")

if __name__ == '__main__':
    target_ip = input('Enter target IP to scan: ')
    characterize_attack_surface(target_ip)
    identify_vulnerabilities(target_ip)