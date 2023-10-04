def phelloworld():
    print('hello world ;)')
def sum2(a,b):
    print('sum of given numbers is ,',a+b)
def sqrt(a):
    print('sqrt of given number is ,',a**(1/2))
def areaoftriangle_bh(b,h):
    print('area of triangle is,', 1/2*b*h)
def quadrat(a,b,c):
    print('roots are ', (-b+(b**2 - 4*a*c)**1/2)/(2*a) ,'and',(-b+(b**2 - 4*a*c)**1/2)/(2*a))
def swap(a,b):
    print('a is ',a,' b is ',b)
    a,b=b,a
    print('a is ',a,' b is ',b)
def random():
    import random
    x=random.randint(4,10)
    print('random number between 4 and 10 is',x)
def kmtoml(a):
    print(' miles are ',a*0.6213711)
def ctof(a):
    print(' faranheights are ,', c*9/5+32)
def sign(a):
    if a>0: print('positive')
    else:print('negative')
