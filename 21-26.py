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