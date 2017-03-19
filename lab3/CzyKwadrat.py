# n = input('Podaj liczbe do sprawdzenia ')
n = 16
i = 0
while i*i <= n:
    if i*i == n:
        print 'jest kwadratem'
        i=n+1
    else:
        i += 1
        if i*i > n:
            print 'nie jest kwadratem'
