import random

veta = input("Zadaj vetu: ")

def prehadzuj_slovo(slovo):
    if len(slovo) > 3:
        slovo = [
            slovo[0],
            slovo[1:-1],
            slovo[-1]
        ]
        slovo[1] = ''.join(random.sample(slovo[1], len(slovo[1])))
        slovo = ''.join([str(elem) for elem in slovo])
    return slovo

def prehadzuj(veta):
    znak = ""
    if veta[-1] in ".?!":
        znak = veta[-1]
        veta = veta[:-1]

    veta = veta.split()
    nova_veta = []
    
    for slovo in veta:
        nova_veta.append(prehadzuj_slovo(slovo))
    return " ".join([str(elem) for elem in nova_veta]) + znak
    

print(prehadzuj(veta))