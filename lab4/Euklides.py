b = int(raw_input('Podaj b: '))
a = int(raw_input('Podaj wieksze a: '))
c = int
while (b != 0):
    c = a
    a = b
    b = c % b
print a
