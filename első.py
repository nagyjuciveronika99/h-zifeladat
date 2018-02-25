def feladat_1(a,b):
    a=a+b
    b=a-b
    a=a-b
    print("a=",a)
    print("b=",b)
    
def feladat_2(a,b,c):
    if a<b and a<c
        print(a)
        if b>c:
            print(c)
            print(b)
        else:
            print(b)
            print(c)
    elif b<c and b<a:
        print(b)
        if a<c:
            print(a)
            print(c)
        else:
            print(c)
            print(a)
    else:
        print(c)
        if a<b:
            print(a)
            print(b)
        else:
            print(b)
            print(a)
            
def feladat_3(x):
    if x>-2 and x<0:
        return 2*x
    elif x>=0 and x<2:
        return x*x
    elif x>2:
        return 10
    else:
        print("Nem eleme az ertelmezesi tartomanynak!")
        return

def feladat_5(a,b,c,d):
    print(a,b,c,d)
    if d>=0:
        print(a,b,c,d)
    else:
        print(a,b,c,d)
def feladat_4(a,b,c):
    return min(a,b,c),(max(abs(a), abs(b), abs(c)))
def feladat_15(a,b,hanyados=0):
    while a>=b:
        a=a-b
    return (a)
def feladat_16(a,b):
    r=1
    while r!=0:
        r=a%b
        a=b
        b=r
    return (a)
def feladat_17(a):
    masolat=a
    ujszam=0
    while a>0:
        szamjegy=a%10
        ujszam=ujszam*10+szamjegy
        a=int(a/10)
    return masolat==ujszam
def feladat_18(a,b):
    x=a
    y=b
    p=0
    while x>0:
        if x%2>0:
            p=p+y
        x=int(x/2)
        y=y+y
    return p
def feladat_19(n):
    kivetelek=[2,4,6,8,9]
    if n in kivetelek:
        return False
    for i in range(2, int(n / 2)):
         if n%i==0:
            return False
    return True
def feladat_20(n):
    szamok=[]
    a=0
    b=1
    c=0
    if n==1:
        szamok.append (a)
    else:
        if n==2:
            szamok.append(a)
            szamok.append(b)
        else:

            c=a+b
            szamok.append(a)
            szamok.append(b)
            szamok.append(c)
            k=3
            while k<n:
                a=b
                b=c
                c=a+b
                szamok.append(c)
                k=k+1
    return szamok



def main():
    print(feladat_15(15,10))
    print(feladat_16(13,17))
    print(feladat_17(15))
    print(feladat_18(15,10))
    print(feladat_19(15))
    print(feladat_20(8))
if __name__ == '__main__':
     main()


def feladat_21(a):
    ujszam = 0
    while a > 0:
        szamjegy = a % 10
        ujszam = ujszam * 10 + szamjegy
        a = int(a / 10)
    return  ujszam
def feladat_22(alap,kitevo):
    eredmeny=1
    while kitevo>0:
        if kitevo%2>0:
            eredmeny=eredmeny*alap
            kitevo=kitevo-1
        alap=alap*alap
        kitevo=kitevo/2
    return eredmeny
def feladat_23(n):
    osszeg=0
    for i in range(1,n):
        if n%i==0:
            osszeg=osszeg+i
    if osszeg==n:
        return True
    else:
        return False
def feladat_24():
    szam=int(input())
    maradek5db=0
    maradek7db=0
    while szam!=0:
        if szam%7==5:
            maradek5db=maradek5db+1
        if szam%13==7:
            maradek7db=maradek7db+1
        szam = int(input())
    return[maradek5db,maradek7db]
def feladat_25():
    nepesseg=int(input())
    terulet=int(input())
    nepsuruseg=nepesseg/terulet
    print (nepsuruseg)
    if nepsuruseg<=50:
        print("Ritkan.")
    elif nepsuruseg<=300:
        print("Atlagos.")
    else:
        print("Surun lakott.")
def feladat_26():
    osszeg=0
    szam = int(input())
    pozitivdb = 0
    negativdb = 0
    while szam != 0:
        if szam>0:
            pozitivdb = pozitivdb + 1
        else:
            negativdb = negativdb + 1
        osszeg=osszeg+szam
        print (osszeg)
        szam = int(input())
    return [pozitivdb,negativdb]
def main():
    print (feladat_21(321))
    print(feladat_22(3,3))
    print(feladat_23(6))
    print(feladat_24())
    feladat_25()
    print(feladat_26())
if __name__ == '__main__':
     main()    
