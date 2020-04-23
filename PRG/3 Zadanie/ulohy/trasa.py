import tkinter

# empirické konštanty
KONSTANTA_VYSKY=200
KONSTANTA_SIRKY=200
KOEFICIENT_SIRKY_OKNA=750

# zadané výšky
vysky=[8120, 1506, 869, 132, 1175]

# výpočet koeficientov veľkosti okna
koeficient_vysky=(max(vysky)-min(vysky))/KONSTANTA_VYSKY
koeficient_sirky=KOEFICIENT_SIRKY_OKNA/(len(vysky)+2)

# výpočet veľkosti okna
vyska_okna=(max(vysky)-min(vysky))/koeficient_vysky+100
dlzka_okna=koeficient_sirky*(len(vysky)+1)

# vytvorenie objektu okna
okno=tkinter.Tk()
platno=tkinter.Canvas(okno, height=vyska_okna, width=dlzka_okna, bg="white")
platno.pack()

# prepočet a zmena mierky
suradnice = vysky.copy()
minimum = min(suradnice)

for i in range(len(suradnice)):
    suradnice[i] = suradnice[i] - minimum

maximum = max(suradnice)

for i in range(len(suradnice)):
    suradnice[i] = (maximum - suradnice[i])/koeficient_vysky
    suradnice[i] = suradnice[i] +50

# vykreslenie trasy
for i in range(len(suradnice)):
    if i+1 < len(suradnice):
        platno.create_line((i+1)*koeficient_sirky, suradnice[i], (i+2)*koeficient_sirky, suradnice[i+1])
    platno.create_text((i+1)*koeficient_sirky, suradnice[i], text=str(vysky[i])+" m")

# zistenie najväčšieho prevýšenia
prevysenie = 0
useky = []

# zistenie najväčšieho prevýšenia
for i in range(len(vysky)-1):
    prevysenie_na_useku = abs(vysky[i] - vysky[i+1])
    if prevysenie_na_useku > prevysenie:
        prevysenie = prevysenie_na_useku
        usek = i

# zisťovanie úsekov s najväčším prevýšením
for i in range(usek, len(vysky)-1):
    prevysenie_na_useku = abs(vysky[i] - vysky[i+1])
    if prevysenie_na_useku == prevysenie:
        useky.append(i+1)

# výpis prevýšenia
if len(useky) > 1:
    platno.create_text(dlzka_okna-200, vyska_okna-15, text=f"Najväčšie prevýšenie ({prevysenie} m) je prvýkrát na {useky[0]}. úseku.")
    print(f"Úseky s prevýšením {prevysenie} m: {useky}")
else:
    platno.create_text(dlzka_okna-150, vyska_okna-15, text=f"Najväčšie prevýšenie ({prevysenie} m) je na {useky[0]}. úseku.")
okno.mainloop()