def feladat_33():
    szam=int(input())
    legnagyobbszam=1
    legtobboszto=2
    for i in range(1,szam):
        osztok = []
        for oszto in range(1, i):

            if i % oszto == 0:
                osztok.append(oszto)
        osztokszama=osztok.__sizeof__()
        if osztokszama>=legtobboszto:
            legnagyobbszam=i
            osztokszama=legtobboszto
    return legnagyobbszam
def prime(n):
    kivetelek = [2, 4, 6, 8, 9]
    if n in kivetelek:
        return False
    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False
    return True

def feladat_34(n):
    if n<=6:
        return
    primek=[]

    for i in range(1,n):
        if prime(i):
            primek.append(i)
    return[primek[-1],n-primek[-1]]

def feladat_35(n):
    primiker=[]
    p=2
    q=p+2

    while len(primiker)<n:
        if (prime(p) and prime(q)):
            primiker.append([p,q])
        p=p+1
        q=q+1
    return primiker
def feladat_36(n):
    n=3
    lst=[1,1]
    if n==0 or n==1:
        print(0)
    else:
        while lst[len(lst)-1]<n:
            lst.append(lst[len(lst)-1]+lst[len(lst)-2])
    print(len(lst)-1)
def feladat_37(n):
    n=1998
    lst=[1,1]
    if n==0:
        print(1)
    elif n==1:
        print(2)
    else:
        while lst[len(lst)-1]<=n:
            lst.append(lst[len(lst)-1]+lst[len(lst)-2])
        print(len(lst) - 1)
def feladat_38():
    x=input("Szamjegy: ")
    y=input("Szam: ")
    z=0
    for i in range(len(y)):
        if x==y[i]:
            z=z+1
    print(z,end="* tartalmazza.")
def feladat_39():
    lst=[]
    auxlst=[]
    b=0
    for i in range(1000):
        b=0
        for j in range(len(str(i))):
            b=b+int(str(i)[j])*int(str(i)
    [j])*int(str(i[j])
            if int(i)==b:
                lst.append(i)
    print(lst)


def main():
   print(feladat_33())
   print(feladat_34(128))
   print(prime(4))
   print(feladat_35(5))
   print(feladat_36(1))
   print(feladat_37)
   print(feladat_38())
   print(feladat_39())
if __name__ == '__main__':
     main()