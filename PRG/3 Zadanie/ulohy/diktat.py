diktat=["syn","dym","bicykel","rizoto","ryža","písomka"]
pocet_spravnych=0

for slovo in diktat:
    hadane_slovo = ""
    hadane_iy = ""
    for pismeno in slovo:
        if pismeno in "iíyý":
            hadane_slovo = hadane_slovo + "_"
            hadane_iy = hadane_iy + pismeno
        else:
            hadane_slovo = hadane_slovo + pismeno
    print("Doplň i/í/y/ý:", hadane_slovo)
    pismena = input("> ")
    if pismena == hadane_iy:
        pocet_spravnych = pocet_spravnych + 1


print(f'Výsledok: {pocet_spravnych} správne z {len(diktat)}.')
        
    
    
    
