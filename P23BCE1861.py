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
if __name__=="__main__":
    main()
