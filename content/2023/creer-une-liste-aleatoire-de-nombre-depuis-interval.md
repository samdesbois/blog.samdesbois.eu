Title: Créer une liste de nombre aléatoire de depuis un interval avec Python
Date: 2023-11-10
Category: Informatique
Tags: python, code

## Contexte et définition du problème
C'est la fin de la semaine. Il ne me reste que plus quelques heures avant 
de retourner à la maison pour le week-end. Je prends donc sur mon temps de 
pause pour coder un petit peu. PLus exactement je fais une série 
d'exercices issus d'un cours en ligne. Ce cours consiste en [une série de 
100 exercices](https://www.udemy.com/course/python-video-workbook/). Je 
prends un certain plaisir à effectuer ce cours et je le refais pour la 
deuxième fois pour consolider mes acquis et ainsi également par plaisir.

Il est composé de plusieurs parties et chaque partie contient plus d'une 
dizaine d'exercices. Pour varier un peu cette nouvelle étude, comme j'aime 
bien faire dans des situations similaires, je fais les exercices dans un 
ordre **aléatoire**. Dans ce cas précis, je vais aborder une nouvelle partie : 
la section 3 qui comporte les exercices 51 à 75.

Mon objectif est donc de générer une **liste aléatoire** de nombres entiers 
compris entre 51 et 75 avec l'aide de **python**.

## Ma solution

Il est très agréable de parvenir à une solution sans avoir recours à 
Google©. Et j'ai été agréablement surpris de parvenir à résoudre ce petit 
problème sans avoir recours à cette béquille diabolique.

La première étape est ce qu'on pourrait appeler le brouillon. Je tâtonne le 
problème dans la console Python©. On peut également appeler ça le bac à 
sable. Dans le logiciel que j'utilise pour coder (PyCharm), il y a un 
onglet quelque part en bas pour accéder à cette console avec l'entrée qui 
commence par `>>>`.

Je cherche donc une fonction que gère des listes aléatoires. Je me rappelle 
que les fonctions de bases ne le permettent pas et qu'il faut passer par 
une bibliothèque. Cette bibliothèque me revient à l'esprit facilement, car 
elle s'appelle `random`, qui veut dire *aléatoire* comme vous savez 
sûrement déjà. Je dois donc importer cette librairie :

```python
import random
```

J'utilise ensuite la fonction intégrée (*built-in function*) `dir` qui 
permet de lister toutes les méthodes de la classe `random`. Je parcours les 
différentes méthodes et mon choix se pose sur `sample`. Ensuite j'écris 
directement la ligne de commande et mon éditeur de code me montre les 
paramètres attendus, mais il est possible d'avoir la définition de la 
méthode avec cette commande : `help(random.sampl)`

En bidouillant avec les fonctions intégrées `range()` et `list()`, j'arrive 
à ce code fonctionnel pour mon problème.

````python
import random

my_list = list(range(51, 76))
my_list_randomized = random.sample(my_list, len(my_list))

print(my_list_randomized)
````

Et la *built-in* fonction `len()` permet de connaitre la longueur de notre 
liste, car la méthode `random.sample()` a besoin d'un deuxième paramètre 
obligatoire pour savoir la taille de la liste extraite. Dans notre cas, la 
taille de l'échantillon aléatoire est égale à la taille de notre liste 
initiale.

## Conclusion
Petit exercice très rapide et pas très compliqué pour moi. Je dois vous 
avouer que j'avais déjà fait cet exercice il y a quelques années avec une 
recherche sur Google@. Je pense que cette recherche était superflue et 
qu'il est possible de trouver la solution soi-même avec la satisfaction de 
trouver seul en bonus. J'imagine qu'il y a sûrement des solutions autres et 
probablement plus efficaces ou élégantes, néanmoins celle-ci me satisfait 
amplement.