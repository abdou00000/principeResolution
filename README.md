# Documentation de l'algorithme de résolution de formules logiques
Cette documentation fournit des instructions sur la façon d'utiliser l'algorithme de résolution de formules logiques implémenté en Python à l'aide de la bibliothèque SymPy.

# Fonctionnement
L'algorithme de résolution est basé sur la logique de résolution, une méthode de preuve en logique propositionnelle. L'idée principale est de transformer une formule logique en forme normale conjonctive (CNF), puis d'appliquer la résolution entre les clauses CNF pour déterminer la validité de la formule.

# L'algorithme comprend les étapes suivantes :

1) Négation de la formule : La formule logique en entrée est négativée pour obtenir sa forme négative.

2) Conversion en CNF : La forme négative de la formule est convertie en forme normale conjonctive (CNF) en utilisant la fonction to_cnf de la bibliothèque SymPy.

3) Mise sous forme de clauses : La CNF obtenue est ensuite mise sous forme de clauses, qui sont des disjonctions de littéraux.

4) Recherche de clauses résolvantes : Des paires de clauses sont comparées, et si une résolvante est trouvée, l'algorithme s'arrête et indique que la formule est invalide.

5) Validation de la formule : Si aucune résolvante n'est trouvée, la formule est considérée comme valide.
