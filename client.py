"""
Autonomous Agent Fictitious Play Learning Skill
Pure Python Standard Library implementation.
"""
from typing import List, Dict, Any

class FictitiousPlay:
    """
    Brown's Fictitious Play algorithm for learning mixed-strategy Nash equilibria.
    """
    def __init__(self, p1_payoffs: List[List[float]], p2_payoffs: List[List[float]]):
        self.A = [[float(v) for v in r] for r in p1_payoffs]
        self.B = [[float(v) for v in r] for r in p2_payoffs]
        self.m = len(p1_payoffs)
        self.n = len(p2_payoffs[0])
        self.p1_counts = [0] * self.m
        self.p2_counts = [0] * self.n

    def play(self, iterations: int = 500) -> Dict[str, Any]:
        p1_choice = 0
        p2_choice = 0
        self.p1_counts[p1_choice] += 1
        self.p2_counts[p2_choice] += 1

        for t in range(2, iterations + 1):
            p2_dist = [c / (t - 1) for c in self.p2_counts]
            p1_expected = [sum(self.A[i][j] * p2_dist[j] for j in range(self.n)) for i in range(self.m)]
            p1_choice = int(max(range(self.m), key=lambda i: p1_expected[i]))

            p1_dist = [c / (t - 1) for c in self.p1_counts]
            p2_expected = [sum(self.B[i][j] * p1_dist[i] for i in range(self.m)) for j in range(self.n)]
            p2_choice = int(max(range(self.n), key=lambda j: p2_expected[j]))

            self.p1_counts[p1_choice] += 1
            self.p2_counts[p2_choice] += 1

        total = iterations
        return {
            "p1_mixed_strategy": [round(c / total, 4) for c in self.p1_counts],
            "p2_mixed_strategy": [round(c / total, 4) for c in self.p2_counts],
            "iterations": total
        }
