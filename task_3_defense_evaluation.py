# task_3_defense_evaluation.py

import json
from datetime import datetime
from typing import Dict, List, Tuple

class DefenseMeasure:
    """Represents a defense measure and its effectiveness metrics."""
    
    def __init__(self, name: str, cost: float, complexity: str):
        self.name = name
        self.cost = cost
        self.complexity = complexity
        self.effectiveness_scores = []
    
    def record_effectiveness(self, attack_scenario: str, effectiveness_percent: float):
        """Record the effectiveness of this defense against an attack scenario."""
        self.effectiveness_scores.append({
            'scenario': attack_scenario,
            'effectiveness': effectiveness_percent
        })
    
    def get_average_effectiveness(self) -> float:
        """Calculate average effectiveness across all scenarios."""
        if not self.effectiveness_scores:
            return 0.0
        total = sum(score['effectiveness'] for score in self.effectiveness_scores)
        return total / len(self.effectiveness_scores)


class DefenseEvaluator:
    """Evaluates the impact and effectiveness of defense measures."""
    
    def __init__(self):
        self.defense_measures: Dict[str, DefenseMeasure] = {}
        self.evaluation_results = []
    
    def add_defense_measure(self, name: str, cost: float, complexity: str) -> None:
        """Add a new defense measure to evaluate."""
        self.defense_measures[name] = DefenseMeasure(name, cost, complexity)
    
    def evaluate_defense_against_attack(self, defense_name: str, 
                                       attack_scenario: str, 
                                       effectiveness_percent: float) -> None:
        """Evaluate how effective a defense is against a specific attack."""
        if defense_name in self.defense_measures:
            self.defense_measures[defense_name].record_effectiveness(
                attack_scenario, effectiveness_percent
            )
    
    def calculate_roi(self, defense_name: str) -> float:
        """Calculate Return on Investment based on effectiveness vs cost."""
        if defense_name not in self.defense_measures:
            return 0.0
        
        defense = self.defense_measures[defense_name]
        avg_effectiveness = defense.get_average_effectiveness()
        
        # ROI = (Effectiveness / Cost) * 100
        if defense.cost == 0:
            return 0.0
        return (avg_effectiveness / defense.cost) * 100
    
    def rank_defenses(self) -> List[Tuple[str, float]]:
        """Rank defense measures by ROI."""
        rankings = []
        for name in self.defense_measures:
            roi = self.calculate_roi(name)
            rankings.append((name, roi))
        return sorted(rankings, key=lambda x: x[1], reverse=True)
    
    def generate_evaluation_report(self, filename: str = 'defense_evaluation_report.json') -> None:
        """Generate a comprehensive evaluation report."""
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        
        report = {
            'timestamp': timestamp,
            'evaluation_summary': {},
            'defense_rankings': [],
            'detailed_analysis': []
        }
        
        # Add detailed analysis for each defense
        for name, defense in self.defense_measures.items():
            analysis = {
                'name': name,
                'cost': defense.cost,
                'complexity': defense.complexity,
                'average_effectiveness': defense.get_average_effectiveness(),
                'roi': self.calculate_roi(name),
                'test_results': defense.effectiveness_scores
            }
            report['detailed_analysis'].append(analysis)
        
        # Add rankings
        rankings = self.rank_defenses()
        for rank, (name, roi) in enumerate(rankings, 1):
            report['defense_rankings'].append({
                'rank': rank,
                'defense': name,
                'roi_score': roi
            })
        
        # Write report to file
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)
        
        print(f"Defense evaluation report generated: {filename}")


if __name__ == '__main__':
    # Example usage
    evaluator = DefenseEvaluator()
    
    # Add various defense measures
    evaluator.add_defense_measure("Firewall", cost=500.0, complexity="low")
    evaluator.add_defense_measure("IDS/IPS", cost=2000.0, complexity="medium")
    evaluator.add_defense_measure("EDR Solution", cost=5000.0, complexity="high")
    evaluator.add_defense_measure("Network Segmentation", cost=3000.0, complexity="high")
    
    # Evaluate defenses against various attack scenarios
    evaluator.evaluate_defense_against_attack("Firewall", "Brute Force Attack", 75.0)
    evaluator.evaluate_defense_against_attack("Firewall", "Port Scanning", 85.0)
    
    evaluator.evaluate_defense_against_attack("IDS/IPS", "Brute Force Attack", 90.0)
    evaluator.evaluate_defense_against_attack("IDS/IPS", "Malware Detection", 80.0)
    
    evaluator.evaluate_defense_against_attack("EDR Solution", "Malware Execution", 95.0)
    evaluator.evaluate_defense_against_attack("EDR Solution", "Lateral Movement", 85.0)
    
    evaluator.evaluate_defense_against_attack("Network Segmentation", "Lateral Movement", 92.0)
    evaluator.evaluate_defense_against_attack("Network Segmentation", "Data Exfiltration", 80.0)
    
    # Generate evaluation report
    evaluator.generate_evaluation_report()
    
    # Display rankings
    print("\nDefense Measure Rankings by ROI:")
    for rank, (name, roi) in enumerate(evaluator.rank_defenses(), 1):
        print(f"{rank}. {name}: ROI Score = {roi:.2f}")