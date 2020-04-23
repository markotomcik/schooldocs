cislo = int(input("Zadaj číslo: "))

def delitele(n):
    i = 1
    delitele = []
    while i <= n ** 0.5: 
        if (n % i == 0): 
            if i not in delitele:
                delitele.append(i)
            if n/i not in delitele:
                delitele.append(int(n/i))
        i = i + 1
    delitele.sort()
    return delitele

delitele = delitele(cislo)
if len(delitele) == 2:
    print(f"Číslo {cislo} je prvočíslo.")
else:
    print(f"Číslo {cislo} má delitele {', '.join([str(cislo) for cislo in delitele])}.")
