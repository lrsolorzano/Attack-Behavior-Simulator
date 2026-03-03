import json
from datetime import datetime

class FinalReportGenerator:
    def __init__(self, findings, recommendations):
        self.findings = findings
        self.recommendations = recommendations
        self.report_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    def generate_html_report(self):
        html_content = f"<html><head><title>Final Report</title></head><body>"
        html_content += f"<h1>Final Report</h1><h2>Date: {self.report_date}</h2>"
        html_content += "<h3>Findings</h3><ul>"
        for finding in self.findings:
            html_content += f"<li>{finding}</li>"
        html_content += "</ul><h3>Recommendations</h3><ul>"
        for recommendation in self.recommendations:
            html_content += f"<li>{recommendation}</li>"
        html_content += "</ul></body></html>"
        return html_content

    def generate_json_report(self):
        report = {
            "date": self.report_date,
            "findings": self.findings,
            "recommendations": self.recommendations
        }
        return json.dumps(report, indent=4)

# Example Usage
if __name__ == "__main__":
    findings = ["Finding 1", "Finding 2", "Finding 3"]
    recommendations = ["Recommendation 1", "Recommendation 2", "Recommendation 3"]
    report_generator = FinalReportGenerator(findings, recommendations)
    
    html_report = report_generator.generate_html_report()
    json_report = report_generator.generate_json_report()
    
    print("HTML Report:")
    print(html_report)
    print("\nJSON Report:")
    print(json_report)