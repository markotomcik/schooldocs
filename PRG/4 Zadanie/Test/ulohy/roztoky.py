vzorky=[3,7,5,6,8,4]
vysledky=[]

for vzorka in vzorky:
    if vzorka < 7:
        vysledky.append("kyslý")
    elif vzorka > 7:
        vysledky.append("zásaditý")
    elif vzorka == 7:
        vysledky.append("neutrálny")

print('pH analyzovaných vzoriek a výsledky analýzy:')
for i in range(len(vzorky)):
    print(f'{vzorky[i]} {vysledky[i]}')