import math
def f11(x):
    a= math.sqrt(5*math.pow(x,4)+math.exp(x))
    b=-math.sqrt((math.sin(x)+94*x)/(math.log(x)+x**8))
    c=math.sqrt((math.pow(x,7)+95*x**8)/(x**7-math.log(x)))
    return a+b+c
def f12(x):
    if x<58:
        return 70*(59*x+94*x**6)+x**6
    elif x<117:
        return 3*x**7+math.tan(x)-91
    else:
        return (x**4-math.cos(x))**6-47*x**5
def f13(n, m):
    s1=0
    for i in range(1, n+1):
        s1=s1+22*i**5+83*i**7
    s2=0
    for i in range(1,n+1):
        for j in range(1, m+1):
            s2=s2+37*i**3+4j-9
    return 96*s1+s2
def f14(n)
    if n==0:
        return 3
    elif n==1
        return 6
    else
        return math.sin(f14(n-2))+math.sin(f14(n-2))+22
