import socket
import json

class AttackSurface:
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.open_ports = []

    def scan_ports(self, port_range=(1, 65535)):
        """Scan for open ports on the target IP."""
        for port in range(port_range[0], port_range[1]+1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  # Timeout for socket connection
                result = sock.connect_ex((self.target_ip, port))
                if result == 0:
                    self.open_ports.append(port)
        return self.open_ports

    def identify_vulnerabilities(self):
        """Identify potential vulnerabilities based on open ports."""
        vulnerabilities = []
        # Example vulnerability checks
        for port in self.open_ports:
            if port == 22:
                vulnerabilities.append({"port": port, "vulnerability": "SSH exposed"})
            elif port == 80:
                vulnerabilities.append({"port": port, "vulnerability": "HTTP exposed"})
            # Add more checks as necessary
        return vulnerabilities

    def generate_report(self):
        """Generate a report of the attack surface characterization."""
        report = {
            "target_ip": self.target_ip,
            "open_ports": self.open_ports,
            "vulnerabilities": self.identify_vulnerabilities()
        }
        return json.dumps(report, indent=4)

if __name__ == '__main__':
    target = input('Enter the target IP address: ')
    attack_surface = AttackSurface(target)
    attack_surface.scan_ports()
    report = attack_surface.generate_report()
    print(report)