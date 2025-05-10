import time
import tracemalloc

def parse_dimacs(filename):
    with open(filename, 'r') as file:
        clauses = []
        for line in file:
            if line.startswith('p') or line.startswith('c'):
                continue
            clause = list(map(int, line.strip().split()))
            if clause and clause[-1] == 0:
                clause.pop()
            clauses.append(clause)
    return clauses

def run_with_profiling(solver, clauses):
    tracemalloc.start()
    start = time.time()
    result = solver(clauses)
    elapsed = time.time() - start
    _, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, elapsed, peak_mem / 1024  # in KB

# Solvers (from previous step)
def resolution_solver(clauses): ...  # Add code from previous reply
def dp_solver(clauses): ...
def dpll_solver(clauses, assignment=set()): ...

solvers = {
    "Resolution": resolution_solver,
    "DP": dp_solver,
    "DPLL": lambda cls: dpll_solver(cls, set()),
}

files = ["data/sat_small.cnf", "data/unsat_small.cnf", "data/random_medium.cnf"]

with open("results.csv", "w") as out:
    out.write("File,Algorithm,Result,Time(s),Memory(KB)\n")
    for file in files:
        clauses = parse_dimacs(file)
        for name, solver in solvers.items():
            result, t, mem = run_with_profiling(solver, clauses)
            out.write(f"{file},{name},{'SAT' if result else 'UNSAT'},{t:.4f},{mem:.2f}\n")
