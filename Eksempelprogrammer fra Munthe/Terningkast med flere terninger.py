from pylab import *
from fractions import Fraction         # Gjør at vi kan regne med brøker

#Terningkast med flere terninger

T = int(input("Hvor mange terninger skal kastes? "))
S = int(input("Hvilken sum av øyne er du på jakt etter? "))

N = 100000                              # Antall kast
G = Fraction(0)                         # Teller gunstige utfall

for i in range(N):                      # Kaster T terninger N ganger
    T_sum = 0                           # Setter summen av alle terningene lik 0
    for j in range(T):                  # Kaster T terninger en gang
        T_sum = T_sum + randint(1, 7)   # Summerer antall øyne
    if T_sum == S:                      # Hvis antall øyne er lik S
        G = G + 1                       # Øker antall gunstige med en

N = Fraction(N)                         # Gjør N om til en brøk for å kunne regne ut svaret som brøk

print(randint(1,2))
print("Sannsynligheten for å få", S, "øyne er", G/N, "=", round(float(G/N), 5))  # Regner gunstige delt på mulige