import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
C_m  =   1.0 # membrane capacitance, in uF/cm^2
g_Na = 120.0 # maximum conducances, in mS/cm^2
g_K  =  36.0
g_L  =   0.3
E_Na =  50.0 # Nernst reversal potentials, in mV
E_K  = -77.0
E_L  = -54.387

def alpha_m(V):
    return 0.1*(V+40.0)/(1.0 - np.exp(-(V+40.0) / 10.0))

def beta_m(V):  
    return 4.0*np.exp(-(V+65.0) / 18.0)

def alpha_h(V): 
    return 0.07*np.exp(-(V+65.0) / 20.0)

def beta_h(V):  
    return 1.0/(1.0 + np.exp(-(V+35.0) / 10.0))

def alpha_n(V): 
    return 0.01*(V+55.0)/(1.0 - np.exp(-(V+55.0) / 10.0))

def beta_n(V):  
    return 0.125*np.exp(-(V+65) / 80.0)

def dy_dt(y, t):
    V, m, h, n = y

    I_Na = g_Na*m**3*h*(V - E_Na)
    I_K = g_K*n**4*(V-E_K)
    I_L = g_L*(V-E_L)
    dV_dt = -(I_Na + I_K + I_L)/C_m + I_inj(t)/C_m

    dm_dt = alpha_m(V)*(1-m) - beta_m(V)*m
    dh_dt = alpha_h(V)*(1-h) - beta_h(V)*h
    dn_dt = alpha_n(V)*(1-n) - beta_n(V)*n
    return [dV_dt, dm_dt, dh_dt, dn_dt]

def I_inj(t):
    return 200*(2 < t < 2.2)

def run():
    t = np.linspace(0, 10, 1001)

    y = odeint(dy_dt, [-80, 0.05, 0.6, 0.32], t)
    V, m, h, n = np.hsplit(y, 4)

    plt.plot(t, V, linewidth=2)
    plt.xlabel('Tid (ms)')
    plt.ylabel('Membranpotensiale (mV)')
    plt.annotate('Stimuli', xy=(2, -70), xytext=(0, -50), fontsize=12,
                 arrowprops=dict(facecolor='darkred', width=2, shrink=0.1))    
    plt.title('Aksjonspotensialet som modellert av Hodgkin-Huxley modellen')
    plt.show()


if __name__ == '__main__':
    run()