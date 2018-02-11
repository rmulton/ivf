# Projet d'Introduction à la vérification formelle
## Objectif
L'objectif de ce projet est de réaliser un outil d'analyse de couverture de tests pour le langage While.

## Utilisation
### Essai de l'outil
Lancer la commande ```python test_prog.py```
Le résultat attendu est le suivant :
```
=== Tests for First program ===
1. Test TA passed.
2. Test TD passed.
3. Test 4-TC didn't pass. Some 4-paths are not visited: [[(1, 3), (3, 4), (4, 5), (5, '_')]]
4. Test I_TB for i=1 passed
5. Test TDef passed
6. Test TU passed
7. Test TDU passed
8. Test TC passed
=== End of the tests for First program ===

=== Tests for Program while ===
1. Test TA passed.
2. Test TD passed.
3. Test 5-TC didn't pass. Some 5-paths are not visited: [[(1, 2), (2, 4), (4, 6), (6, 4), (4, 6)], [(1, 3), (3, 4), (4, 6), (6, 4), (4, 5)], [(1, 3), (3, 4), (4, 6), (6, 4), (4, 6)]]
4. Test I_TB for i=1 didn't pass. Some paths are not visited: [[(1, 3), (3, 4), (4, 6), (6, 4), (4, 5), (5, '_')]]
5. Test TDef passed
6. Test TU passed
7. Test TDU passed
8. Test TC passed
=== End of the tests for Program while ===

=== Tests for Program 3 variables v1 ===
1. Test TA didn't pass. Some assign edges are not visited: {(3, 4)}
2. Test TD passed.
3. Test 5-TC didn't pass. Some 5-paths are not visited: [[(1, 2), (2, 4), (4, 6), (6, '_')], [(1, 3), (3, 4), (4, 5), (5, '_')], [(1, 3), (3, 4), (4, 6), (6, '_')], [(1, 3), (3, 4), (4, 6), (6, 7), (7, 6)]]
4. Test I_TB for i=1 didn't pass. Some paths are not visited: [[(1, 2), (2, 4), (4, 6), (6, 7), (7, 6), (6, '_')], [(1, 3), (3, 4), (4, 6), (6, 7), (7, 6), (6, '_')]]
5. Test TDef didn't pass. Some variables dict_keys([<cover_analyser.Var.Var object at 0x0000022A0702BBE0>]) are not used on edges: {<cover_analyser.Var.Var object at 0x0000022A0702BBE0>: (3, 4)}
6. Test TU passed
7. Test TDU passed
8. Test TC didn't pass. Some conditions are not satisfied by any test provided: [<cover_analyser.expressions.boolean.InfOrEqual object at 0x0000022A0702BD68>]
=== End of the tests for Program 3 variables v1 ===

=== Tests for Program 3 variables v2 ===
1. Test TA passed.
2. Test TD passed.
3. Test 5-TC passed.
4. Test I_TB for i=1 passed
5. Test TDef passed
6. Test TU passed
7. Test TDU passed
8. Test TC passed
=== End of the tests for Program 3 variables v2 ===
```
### Utilisation sur un nouveau programme
- Écrire la fonction de création d'un objet de la classe Program (exemples disponibles dans ./program/examples.py)
- Créer un jeu de test pour le programme (exemples disponibles dans ./test_prog.py)
- Passer le jeu de test et le programme aux fonctions d'analyse de couverture désirées
### Créer de nouveaux tests
- Écrire la classe représentant le test dans ./cover\_analyser.py/test\_criteria.py. Elle doit présenter une méthode test(test_set, program).
- Écrire une fonction enveloppe qui instancie la classe représentant le test et effectue le test. (exemples disponibles dans ./cover\_analyser/test\_criteria.py)
## Réalisation
### Principe
1. L'utilisateur écrit le graphe d'un programme, puis crée un objet Program à partir de celui-ci, de la liste des variables utilisées par le programme, du noeud initial et de la liste des noeuds finaux.
2. L'utilisateur propose un jeu de test pour ce programme.
3. L'utilisateur passe ce programme et ce jeu de test à une fonction de test.
4. L'outil parcours le graphe selon l'algorithme décrit dans le test pour déterminé si le critère est valide pour le programme avec le jeu de test.
### Structure
Le code source est découpé en deux parties :
- ./program contient les éléments représentant le programme
- ./cover_analyser contient les éléments nécessaires à la validation ou à l'infirmation des tests
La racine contient également test_prog.py, qui permet d'essayer rapidement l'outil.
#### ./cover_analyser
- ./cover\_analyser/instructions.py contient les classes représentant les instructions que le programme peut utiliser
- ./cover\_analyser/test_criteria.py contient les classes et fonctions enveloppes implémentant la mécanique de validation des test
- ./cover\_analyser/expressions/arithmetic.py contient les classes représentant les expressions artihmétiques
- ./cover\_analyser/expressions/arithmetic.py contient les classes représentant les expressions booléennes et décisions
#### ./program
Ce dossier utilise les éléments du dossier ./cover_analyser
- ./program/node.py contient les classes représentant les différents types de noeuds que le graphe du programme peut comporter
- ./program/Program.py contient la classe représentant un programme. Elle comporte notamment les méthodes de parcours et d'extraction d'information du graphe du programme permettant de réaliser l'analyse de couverture
- ./program/examples.py contient des examples de programmes créés à partir de leur graphes de contrôle.