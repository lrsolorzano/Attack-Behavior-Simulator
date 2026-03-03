class Asset:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Threat:
    def __init__(self, name, likelihood):
        self.name = name
        self.likelihood = likelihood

class Vulnerability:
    def __init__(self, name, impact):
        self.name = name
        self.impact = impact

class QuantitativeRiskModel:
    def __init__(self):
        self.assets = []
        self.threats = []
        self.vulnerabilities = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def add_threat(self, threat):
        self.threats.append(threat)

    def add_vulnerability(self, vulnerability):
        self.vulnerabilities.append(vulnerability)

    def calculate_risk_score(self, asset_name):
        asset = next((a for a in self.assets if a.name == asset_name), None)
        if not asset:
            return 0

        risk_score = 0
        for threat in self.threats:
            for vulnerability in self.vulnerabilities:
                risk_score += asset.value * threat.likelihood * vulnerability.impact
        return risk_score

# Example usage:
# asset = Asset('Server', 100000)
# threat = Threat('Hacker', 0.7)
# vulnerability = Vulnerability('SQL Injection', 0.8)
# qrm = QuantitativeRiskModel()
# qrm.add_asset(asset)
# qrm.add_threat(threat)
# qrm.add_vulnerability(vulnerability)
# score = qrm.calculate_risk_score('Server')
# print(f'Risk Score: {score}')