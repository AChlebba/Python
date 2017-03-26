

def MaxLiczba(*x):
    max = 0
    for i in x:
        if (i > max):
            max = i
    return max

print MaxLiczba(1,2,3,4,5,6,3,3,3,12,0)
