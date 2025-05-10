from copy import deepcopy

# =========================
# Resolution-based Solver
# =========================
def resolution_solver(clauses):
    clauses = [set(c) for c in clauses]
    new = set()

    while True:
        n = len(clauses)
        for i in range(n):
            for j in range(i + 1, n):
                ci, cj = clauses[i], clauses[j]
                for lit in ci:
                    if -lit in cj:
                        resolvent = (ci - {lit}) | (cj - {-lit})
                        if not resolvent:
                            return False  # Empty clause => UNSAT
                        new_clause = frozenset(resolvent)
                        if new_clause not in map(frozenset, clauses):
                            new.add(new_clause)

        if new.issubset(map(frozenset, clauses)):
            return True  # No new clauses added => SAT

        for c in new:
            clauses.append(set(c))
        new.clear()


# =========================
# Davis–Putnam (DP) Solver
# =========================
def dp_solver(clauses):
    def eliminate_var(var, clauses):
        pos = [c for c in clauses if var in c]
        neg = [c for c in clauses if -var in c]
        new_clauses = []

        for c in clauses:
            if var in c or -var in c:
                continue
            new_clauses.append(c)

        for p in pos:
            for n in neg:
                resolvent = list(set(p) - {var}) + list(set(n) - {-var})
                resolvent = list(set(resolvent))
                if not has_complementary_literals(resolvent):
                    new_clauses.append(resolvent)
        return new_clauses

    def has_complementary_literals(clause):
        return any(-lit in clause for lit in clause)

    variables = {abs(lit) for clause in clauses for lit in clause}

    for var in variables:
        clauses = eliminate_var(var, clauses)
        if [] in clauses:
            return False  # UNSAT

    return True  # SAT


# =========================
# DPLL Solver
# =========================
def dpll_solver(clauses, assignment=set()):
    clauses = simplify(clauses, assignment)
    if [] in clauses:
        return False
    if not clauses:
        return True

    unit_clauses = [c[0] for c in clauses if len(c) == 1]
    if unit_clauses:
        return dpll_solver(clauses, assignment | set(unit_clauses))

    var = abs(clauses[0][0])
    return (dpll_solver(clauses, assignment | {var}) or
            dpll_solver(clauses, assignment | {-var}))


def simplify(clauses, assignment):
    simplified = []
    for clause in clauses:
        if any(lit in assignment for lit in clause):
            continue  # clause already satisfied
        new_clause = [lit for lit in clause if -lit not in assignment]
        simplified.append(new_clause)
    return simplified
