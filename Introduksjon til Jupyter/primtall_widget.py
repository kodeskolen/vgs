"""
En enkel widget hvor man kan skrive inn et tall og
sjekke om det er et primtall eller ikke.
"""

from ipywidgets import interact

def er_primtall(n):
    if n == 1:
        return False
    
    for d in range(2, n-1):
        if n % d == 0:
            return False
    
    return True

def sjekk_primtall(n):
    n = int(n)

    if n < 1:
    	print("Kan ikke sjekke negative tall!")

    if er_primtall(n):
        print(f"{n} er et primtall")
    else:
        print(f"{n} er ikke et primtall")

interact(sjekk_primtall, n="1");