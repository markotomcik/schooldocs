import random

pravdepodobnost_mutacie=30
povodnaDNA="AGCGTTGACCCATGTGGGCACGAGTGTACCCTTAGA"
novaDNA=""
zmena=0

for nukleotid in povodnaDNA:
    if random.randint(0, 100) < pravdepodobnost_mutacie:
        if nukleotid == "A":
            novaDNA = novaDNA + "T"
        elif nukleotid == "T":
            novaDNA = novaDNA + "A"
        elif nukleotid == "C":
            novaDNA = novaDNA + "G"
        elif nukleotid == "G":
            novaDNA = novaDNA + "C"
        zmena = zmena + 1
    else:
        novaDNA = novaDNA + nukleotid

print(f'Pôvodná DNA: {povodnaDNA}')
print(f'Nová DNA: {novaDNA}')
print(f'Mutácia prebehla na {zmena} nukleotidoch z celkového počtu {len(povodnaDNA)}')
            
