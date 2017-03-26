ceny = {
        'mleko': 'dwa zlote', 'ser': 'trzy zlote', 'chleb': 'jeden zloty'
}

ceny2 = {
        'mleko': 22, 'ser': 13, 'chleb': 7
}

towary = ['mleko', 'chleb', 'mleko', 'mleko', 'mleko', 'mleko']
wynik = {}

def ListaCen(ceny, towary):
    for i in range(len(towary)):
        wynik['Produkt %d '%i + towary[i]] = ceny[towary[i]]

    koszt = {}
    koszt = wynik.keys()
    cena = 0

    for j in range(len(koszt)):
        cena += koszt[j]

    return wynik
print ListaCen(ceny2, towary)
