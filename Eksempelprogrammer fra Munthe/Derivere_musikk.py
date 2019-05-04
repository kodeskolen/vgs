from scipy.io import wavfile
from pylab import *
import numpy as np

# Laste inn data og samplerate
samplerate, data = wavfile.read('Tristan_og_Isolde.wav') # Her bytter du navn på musikkfil

# På grunn av to lydkanaler må data splittes opp
data_k1 = data[:, 0]        # Kolonne 1
data_k2 = data[:, 1]        # Kolonne 2

# Antall målinger i filen og regner ut tiden mellom hver måling
lengde = len(data_k1)
times = np.arange(lengde)/float(samplerate)

# Startverdi for plotting av graf
start = 6500

def graf(data, times, tittel):  # Programkode som lager et plot av sangen
    y = data[start:start+500]   # Amplituden
    x = times[start:start+500]  # Tiden, plotter ca 0.01 sekund ved +500
    figure(figsize=(13, 4))     # Størrelse på grafikkfeltet
    scatter(x, y)               # Plotter et punktplot
    xlim(x[0], x[-1])           # Størrelse på x-aksen
    title(tittel)               # Tittel på graf
    xlabel('time (s)')          # Navn på x-akse
    ylabel('amplitude')         # Navn på y-akse

def gjør_klar_for_lagring(data1, data2):            # Programkode som setter sammen arrayer
    data1 = np.asarray(data1, dtype=np.int16)       # Konverterer dataene til en array 
    data2 = np.asarray(data2, dtype=np.int16)       # som vi kan lagre som en .wav fil
    ny_data = np.hstack((data1, data2))             # Slår sammen to arrayer til en
    return ny_data

graf(data_k1, times, 'Original')                # Kaller på graf-koden
savefig('Tristan_og_Isolde_original.png', dpi=100)    # Lagrer grafen som .png
show()                                          # Viser grafen på skjerm

lengde = lengde - 1                             # Reduserer lengde med 1

data1a = np.zeros([lengde])                     # Lager en array for dataene
data1b = np.zeros([lengde])

for i in range(lengde):
    data1a[i] = (data_k1[i+1] - data_k1[i]) * (samplerate / 10000)    # Deriverer .wav filen       
    data1b[i] = (data_k2[i+1] - data_k2[i]) * (samplerate / 10000)    
data1a = (max(data_k1)/max(data1a)) * data1a[:]                     # Normaliserer lydnivået
data1b = (max(data_k2)/max(data1b)) * data1b[:]

times = times[0:lengde]                                     # Reduserer tiden med ett element 

graf(data1a, times, 'Deriverte')                            # Lager grafen
savefig('Tristan_og_Isolde_derivert.png', dpi=100)                # Lagrer grafen i fil
show()                                                      # Viser grafen på skjerm

data_ny = gjør_klar_for_lagring(data1a, data1b)                 # Kaller på kode
wavfile.write('Tristan_og_Isolde_derivert.wav', samplerate, data_ny)  # Lagrer som .wav fil