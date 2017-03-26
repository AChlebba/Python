ceny = {
        'mleko': 'dwa zlote', 'ser': 'trzy zlote', 'chleb': 'jeden zloty'
}

ceny2 = {
        'mleko': 22, 'ser': 13, 'chleb': 7
}

towary = ['mleko', 'chleb']
wynik = {}

def ListaCen(ceny, towary):
    for i in range(len(towary)):
        wynik[towary[i]] = ceny[towary[i]]
    return wynik
print ListaCen(ceny2, towary)
