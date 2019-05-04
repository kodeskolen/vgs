from pylab import *

print()
print("Husk å ordne likningen slik at vi har y-leddet på venstre side,") 
print("og x-leddet og konstantleddet på høyre side.")

a = float(input("Skriv inn tallet foran y i første likning "))
b = float(input("Skriv inn tallet foran x i første likning "))
c = float(input("Skriv inn konstantleddet i første likning "))
d = float(input("Skriv inn tallet foran y i andre likning "))
e = float(input("Skriv inn tallet foran x i andre likning "))
f = float(input("Skriv inn konstantleddet i andre likning "))
print()

if b*d - e*a != 0:
    x = (f*a - c*d) / (b*d - e*a)
    y = (b*x + c) / a
    print("Løsningen er x =", x, "og y =", y)
elif a/d != c/f:
    print("Det er ingen mulige løsninger for x og y,") 
    print("siden dette er to parallelle linjer med ulik skjæring med y-aksen.")
else:
    print("Det er uendelig mange muligheter for verdiene til x og y") 
    print("fordi linjene er parallelle og sammenfallende.")
