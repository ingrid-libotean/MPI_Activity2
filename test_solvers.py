from solvers import resolution_solver, dp_solver, dpll_solver

def run_tests():
    test_cases = [
        {
            "name": "SAT example 1",
            "clauses": [[1, 2], [-1], [-2]],
            "expected": True
        },
        {
            "name": "UNSAT example 1",
            "clauses": [[1], [-1]],
            "expected": False
        },
        {
            "name": "SAT example 2",
            "clauses": [[1, 2], [-1, 2], [1, -2]],
            "expected": True
        },
        {
            "name": "UNSAT example 2 (contradiction)",
            "clauses": [[1], [2], [-1, -2]],
            "expected": False
        }
    ]

    solvers = [
        ("Resolution", resolution_solver),
        ("DP", dp_solver),
        ("DPLL", dpll_solver)
    ]

    for case in test_cases:
        print(f"\n=== {case['name']} ===")
        for solver_name, solver in solvers:
            result = solver(case["clauses"])
            status = "PASS" if result == case["expected"] else "FAIL"
            print(f"{solver_name}: {'SAT' if result else 'UNSAT'} → {status}")

if __name__ == "__main__":
    run_tests()
