import random

slovo = input("Zadaj slovo: ")

if len(slovo) > 3:
    slovo = [
        slovo[0],
        slovo[1:-1],
        slovo[-1]
    ]
    slovo[1] = ''.join(random.sample(slovo[1], len(slovo[1])))

print(''.join([str(elem) for elem in slovo]))
