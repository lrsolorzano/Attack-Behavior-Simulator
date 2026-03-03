class DefenseMeasure:
    def __init__(self, name, effectiveness):
        self.name = name
        self.effectiveness = effectiveness

    def __str__(self):
        return f"{self.name} with effectiveness {self.effectiveness}"

class DefenseEvaluator:
    def __init__(self, defenses):
        self.defenses = defenses

    def evaluate(self):
        results = {}
        for defense in self.defenses:
            results[defense.name] = defense.effectiveness * 100  # Assume effectiveness is a fraction
        return results

    def generate_report(self):
        report = "Defense Evaluation Report\n"
        report += "=" * 30 + "\n"
        evaluations = self.evaluate()
        for defense, effectiveness in evaluations.items():
            report += f"Defense Measure: {defense}, Effectiveness: {effectiveness}%\n"
        return report

# Example Usage
if __name__ == "__main__":
    defenses = [
        DefenseMeasure("Firewall", 0.85),
        DefenseMeasure("Intrusion Detection System", 0.75),
        DefenseMeasure("Regular Updates", 0.90),
    ]
    
    evaluator = DefenseEvaluator(defenses)
    print(evaluator.generate_report())
