cyfry = {
        0: 'zero', 1: 'jeden', 2: 'dwa',
        3: 'trzy', 4: 'cztery', 5: 'piec',
        6: 'szesc', 7: 'siedem', 8: 'osiem', 9: 'dziewiec'
}

liczba = 1337
wynik = []

while (liczba != 0):
    wynik = [(cyfry[liczba % 10])] + wynik
    liczba = liczba / 10
print wynik


def slownie3(liczba):
    cyfry = ['zero', 'jeden', 'dwa', 'trzy', 'cztery',
             'piec', 'szesc', 'siedem', 'osiem', 'dziewiec']
    return map(lambda x: cyfry[int(x)], str(liczba))

print slownie3(1234)
