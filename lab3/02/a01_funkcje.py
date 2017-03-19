# 01_funkcje
#
# Sprobuj wykonac w shellu:
# locals()
# globals()
# import a01_funkcje
# locals()
# globals()


a = 1
b = 2

def test1(arg1):
    """To jest pierwsza linia opisu
    
    A to sa kolejne
    I jeszcze
    I jeszcze
    """
    a = arg1
    print 'test1:LOCALS  :', locals()
    print 'test1:GLOBALS :', globals()
    

def test2(arg2):
    global a
    a = arg2    
    b = arg2 + 1
    test1(b)
    print 'test2:LOCALS  :', locals()
    print 'test2:GLOBALS :', globals()

 
# nastepnie sprawdzmy wyniki
# a01_funkcje.a
# a01_funkcje.b
# a01_funkcje.test1(3)
# a01_funkcje.test2(3)

# jakie wyniki otrzymamy wywolujac
# 01_funkcje.test1__doc__
# 01_funkcje.test2.__doc__
#
# Sprawdz
# locals.__doc__
# globals.__doc__