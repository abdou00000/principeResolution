from sympy import symbols, Or, Not, simplify_logic, to_cnf

# Fonction pour la négation d'une expression logique
def negation(expr):
    return Not(expr)

# Fonction pour mettre une expression sous forme de clauses
def mettre_sous_forme_clauses(expr):
    # Si l'expression est une disjonction, retourne ses arguments (clauses)
    # Sinon, retourne une liste contenant l'expression (comme une seule clause)
    return expr.args if isinstance(expr, Or) else [expr]

# Fonction pour chercher des clauses résolvantes
def chercher_clauses_resolvantes(clauses):
    # Parcours de toutes les paires de clauses
    for i, clause1 in enumerate(clauses):
        for j, clause2 in enumerate(clauses):
            if i != j:  # Ne pas comparer une clause avec elle-même
                # Applique la résolution entre clause1 et clause2
                resolvent = simplify_logic(clause1 | clause2)
                if resolvent:  # Si le resolvent n'est pas vide
                    return resolvent  # Renvoie le resolvent
    return False  # Aucun resolvent trouvé

# Fonction principale de l'algorithme de résolution
def algorithme_resolution(F):
    # Calcule la négation de F
    neg_F = negation(F)
    # Transforme la négation de F en forme normale conjonctive (CNF)
    cnf_F = to_cnf(neg_F)
    # Met la CNF de F sous forme de clauses
    clauses = mettre_sous_forme_clauses(cnf_F)
    # Cherche des clauses résolvantes
    resolvent = chercher_clauses_resolvantes(clauses)
    # Si aucun resolvent n'est trouvé, la formule est valide
    if not resolvent:
        return "F est valide"
    else:  # Sinon, la formule est invalide
        return "F est invalide"

# Variables symboliques
p, q, r = symbols('p q r')

# Exemple d'utilisation avec une formule valide
#F_input = 'p | ~p'

# Exemple d'utilisation avec une formule invalide
#F_input = 'p & ~p'

# Exemple d'utilisation avec une formule aléatoire
F_input = '(p | q) & (r | ~p)'

# Conversion de la chaîne en expression logique
F = eval(F_input)
# Appel de l'algorithme de résolution
print(algorithme_resolution(F))
