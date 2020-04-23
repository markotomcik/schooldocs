import random

august = [random.randint(0, 50) for i in range(31)]
print(f'Spadnuté zrážky počas jednotlivých dní v auguste: {august}')

august.sort()
print(f'Najväčšie denné úhrny zrážok: {"mm, ".join([str(august[-(i+1)]) for i in range(3)])}mm.')

print(f'V auguste bol počet dní {august.count(0)}.')