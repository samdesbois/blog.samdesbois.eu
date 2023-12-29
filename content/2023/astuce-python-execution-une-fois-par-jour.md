Title: Astuce Python : exécuter un code une seule fois par jour
Date: 2023-12-29
Category: Informatique
language: fr
Tags: python, code

Nous arrivons dans les derniers jours de 2023. Je continue à m'entrainer 
avec le langage de programmation **Python**. Je refais certains exercices 
déjà rélisés il y a quelques années sur un cours d'*udemy*. En passant, je 
ne vais pas pour l'instant utiliser chatGPT ou autre intelligence 
artificielle (IA) pour coder, car je code seulement pour mon plaisir 
intellectuel.
Une personne m'a informé qu'il était possible d'apprendre en utilisant cette 
IA pour expliquer le code. Cette parenthèse est terminée. Je reviens à 
l'objet de ce post.

En relisant mes notes, dans ma démarche de révision, je suis tombé sur une 
portion de code assez intéressante. Elle permet d'éxécuter une commande "une 
fois par jour" :

```python
import time
from datetime import datetime as dt


while True:
    if dt.now().hour == 11 and dt.now().minute == 55:
        # On exécute son programme
        print("Programme exécuté !")
        time.sleep(60)
```

Je ne sais pas du tout si cela est recommandé, voire dangereux, mais je 
trouve cette manière de faire assez élégante.

Passez de bonnes fêtes de fin d'année !