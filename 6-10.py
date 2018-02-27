import math
def feladat_6(a,b,c):
    if max(a,b,c)<(a+b+c-(min(a,b,c)+max(a,b,c))+min(a,b,c)):
        s=(a+b+c)/2
        T=math.sqrt((s-a)*(s-b)*(s-c)*s)
        print("A beirt kor sugara",(T*2)/(a+b+c),end=".\n")
        print("A kore irt kor sugara",(a*b*c)/(4*T),end=".\n")
    else:
        print("A haromszog nem megszerkesztheto.")


def feladat_7(h,s,d):
    k=2*(h+s)
    if k==d:
        print("Pont eleg a drot.")
    elif k>d:
        print(k-d,"m drot kell meg.")
    else:
        print(d-k,"m drot maradt.")


def feladat_8(x,a,b,c,d):
    if x<5:
        f=3*x-5
    elif 5<=x and x<=10:
        f=10
    elif x>10:
        f=9*x+1
    else:
        f="Nem eleme az ertelmezesi tartomanynak."
    if a+c>2*d and b>0:
        E=d-3*b
    elif a+c<2*d and b<0:
        E=d+3*b
    else:
        E=4
    return f,E
def feladat_9(a,b,c):
    if b*b-4*a*c>=0:
        x1=(-1*b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-1*b-math.sqrt(b*b-4*a*c))/(2*a)
        return x1,x2
    else:
        return "Nincs valos megoldas"
def feladat_10(a,b):
    x=0
    for i in range(a,b+1):
        if (i%4==0 and i%100!=0) or i%400==0:
            x=x+1
    return x

def main():
    feladat_6(3,4,5)
    feladat_7(3,4,15)
    print (feladat_8(12,3,4,2,5))
    print(feladat_9(1,2,4))
    print(feladat_10(1998,2018))
if __name__ == '__main__':
     main()