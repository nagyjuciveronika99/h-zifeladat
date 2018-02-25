import datetime
def feladat_27():
    szam=int(input())
    pozitiv=szam>0
    pozitivdb=0
    negativdb=0
    if szam==0:
        return[0,0]
    if pozitiv:
        pozitivdb=pozitivdb+1
    else:
        negativdb=negativdb+1
    while True:
        szam=int(input())
        if szam==0:
            break
        if pozitiv:
            pozitivdb=pozitivdb+1
            if szam>0:
                break
        else:
            negativdb=negativdb+1
            if szam<0:
                break
        pozitiv=szam>0

    return[pozitivdb,negativdb]


def feladat_28(n):
    legnagyobb=0
    for i in range(2,n-1):
        negyzetszam=i*i
        if negyzetszam>=n:
            return legnagyobb
        else:
            legnagyobb=negyzetszam
def feladat_29(n):
    if n<0 or n>12:
        return


    eredmeny=1
    for i in range(1,n+1):
        eredmeny=eredmeny*i
    return eredmeny
def feladat_30():

    ev=int(input())
    honap=int(input())
    nap=int(input())
    datum=datetime.date(ev,honap,nap)
    return datum.timetuple().tm_yday

def feladat_31(n):
    osztok=[]
    for oszto in range(1,n):
        if n%oszto==0:
            osztok.append(oszto)
    return osztok
def feladatok_32(n1,n2,k):
    szamok = []
    for szam in range(n1, n2):
        if szam%k == 0:
            szamok.append(szam)
    return szamok

def main():
    print(feladat_27())
    print(feladat_28(17))
    print(feladat_29(5))
    print(feladat_30())
    print(feladat_31(100))
    print(feladatok_32(0,100,20))
if __name__ == '__main__':
     main()