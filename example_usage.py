"""Example usage for Fictitious Play Skill."""
from client import FictitiousPlay

def main():
    print("Executing Fictitious Play Iterative Learning...")
    # Matching Pennies: unique Nash equilibrium is (0.5, 0.5)
    A = [[1.0, -1.0], [-1.0, 1.0]]
    B = [[-1.0, 1.0], [1.0, -1.0]]
    fp = FictitiousPlay(A, B)
    res = fp.play(iterations=1000)
    print("Learned Mixed Strategies:", res)
    assert abs(res["p1_mixed_strategy"][0] - 0.5) < 0.05
    assert abs(res["p2_mixed_strategy"][0] - 0.5) < 0.05
    print("Fictitious Play verified successfully!")

if __name__ == "__main__":
    main()
