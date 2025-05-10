# SAT Solver Comparison: Resolution, Davis–Putnam, and DPLL

This repository contains Python implementations of three SAT solving algorithms:

- **Resolution-based solver**
- **Davis–Putnam (DP) algorithm**
- **Davis–Putnam–Logemann–Loveland (DPLL) algorithm**

The project also includes test CNF data and scripts to run experiments and measure performance.

---

## Goal

This project was created for a comparative study of SAT solving algorithms, both theoretically and experimentally. The goal was to:

- Implement key SAT solving methods
- Run experiments on a variety of CNF inputs
- Compare results based on:
  - Satisfiability result (SAT / UNSAT)
  - Computation time
  - Memory consumption
  - Behavior with small, medium, and random formulas

---

## Folder Structure

MPI_Activity2_experiment/
│
├── Data/
│ ├── sat_small.cnf # A small satisfiable formula
│ ├── unsat_small.cnf # A small unsatisfiable formula
│ └── random_medium.cnf # Randomly generated formula (medium size)
│
├── experiment.py # Main script to run experiments
├── results.csv # Output of the experiments
├── solvers.py # Contains the three SAT solver implementations
├── test_solvers.py
└── README.md # This file


---

## Solvers Implemented

### 1. Resolution Solver

- Applies binary clause resolution iteratively
- If the empty clause is derived → UNSAT
- If no new clauses can be derived → SAT

### 2. Davis–Putnam (DP) Algorithm

- Eliminates variables by resolving all clauses that contain a variable and its negation
- Continues until all clauses are removed (SAT) or an empty clause appears (UNSAT)

### 3. DPLL Algorithm

- Recursive, backtracking search
- Includes **unit propagation**
- Can be extended to include heuristics (e.g., pure literal, variable ordering)

---

## Running the Experiments

Make sure you have Python 3 installed.

### Run the experiment:

```bash
python experiment.py
