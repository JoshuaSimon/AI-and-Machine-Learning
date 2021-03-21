# Implementation of a simple propositional calculus proofer.


def parse_propositon(input_proposition):
    clauses = input_proposition.split(" and ")
    return clauses

def parse_clause(input_clause):
    input_clause = input_clause.replace("(", "")
    input_clause = input_clause.replace(")", "")
    literals = input_clause.split(" or ")
    return literals

def calculate_clause(input_clause, knowledge_base):
    realizations = []
    for literal in input_clause:
        realizations.append(knowledge_base[literal])

    return any(realizations)



if __name__ == "__main__":
    knowledge_base = {
        "A": False, "B": False,
        "C": False, "D": True
        }
    input_proposition = "(A or B) and (B or C or D)"
    
    clauses = parse_propositon(input_proposition)
    clause_result = []

    for clause in clauses:
        literals = parse_clause(clause)
        clause_result.append(calculate_clause(literals, knowledge_base))
    
    result = all(clause_result)

    print("This proposition is", result)