from pylab import *
from fractions import Fraction     # Gjør at vi kan regne med brøker
#Terningkast med flere terninger

N = int(input("Hvor mange ganger skal vi kaste terningen? "))

G = Fraction(0)                     # Teller gunstige utfall

for i in range(N):                  # Kaster T terninger en gang
    if randint(1,7) == 6:           # Hvis antall øyne er lik S
        G = G + 1                   # Øker antall gunstige med en

N = Fraction(N)                     # Gjør N om til en brøk for å kunne regne ut svaret som brøk

print("Den relative frekvensen for å få seks når vi kaster", N, "ganger er", G/N, "=", round(float(G/N), 5))  # Regner gunstige delt på mulige