Title: Programme pour deviner un nombre
Date: 2024-10-13
Category: perso
language: fr
Tags: programmation 
Status: Published

Ce programme ultra simple n'en est pas moins un jeu vidéo.

```python
from sys import exit
from random import randint

TRIES_NUMBRER = 5

pseudo = input("Hello, put your name: ")
print("So your name is " + pseudo + "!")
print("Nice to meet you!")

number_to_guess = randint(1,20)

print("{}, You have {} tries to guess the number between 1 and 20 before "
      "loosing.".format(pseudo, TRIES_NUMBRER))

i = 1
while i < TRIES_NUMBRER + 1:
    guess = int(input("Enter your guess: "))

    if guess == number_to_guess:
        print("Well done {}! You found the number with only {} tries!"
              .format(pseudo, i))
        exit(0)
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")
    i += 1

print("Game over! :(")
exit(0)
```

Il y a de l'interactivité, car je demande le nom du joueur. Épatant !