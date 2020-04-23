mesta = []

mesto = input('Zadaj mesto, ktoré si navštívil: ')
mesta.append(mesto)

while True:
    mesto = input("Zadaj ďalšie mesto, ktoré si navštívil: ")
    if mesto not in mesta:
        mesta.append(mesto)
    else:
        mesta.sort()
        break

print(mesta)