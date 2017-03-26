w1 = (1, 2, 3)
w2 = (4, 5, 6)

s = 0
for x in range(len(w1)):
    s = s + w1[x]*w2[x]
print s
