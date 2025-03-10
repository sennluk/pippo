#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 13:12:01 2025

@author: luca
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz

plt.close('all')

# Costanti fisiche
e = 1.602e-19    # Carica elettrone (C)
m_e = 9.109e-31  # Massa elettrone (kg)
c = 3.0e8        # Velocità della luce (m/s)
k_B = 8.617e-5   # Costante di Boltzmann (eV/K) # k_B = 1.381e-23  # Costante di Boltzmann (J/K)

# Funzione per il profilo gaussiano della temperatura elettronica
def gaussian_profile(s, T0, s0, sigma):
    return T0 * np.exp(-((s - s0) ** 2) / (2 * sigma ** 2))

# Funzione per il profilo gaussiano della densità elettronica
def gaussian_density_profile(s, n_e0, s0, sigma_n):
    return n_e0 * np.exp(-((s - s0) ** 2) / (2 * sigma_n ** 2))

# Funzione per il profilo gaussiano del campo magnetico
def gaussian_magnetic_profile(s, B0, s0, sigma_B):
    return B0 * np.exp(-((s - s0) ** 2) / (2 * sigma_B ** 2))

# Funzione per il coefficiente di assorbimento ciclotronico elettronico
def kappa_nu(n_e, B, T_e, nu):
    nu_c = e * B / (2 * np.pi * m_e)  # Frequenza ciclotronica
    return (e**2 / (m_e * c)) * (n_e / B) * (nu / nu_c) * np.exp(-e * nu / (k_B * T_e))

# Dati simulati (da sostituire con i dati reali)
N = 100        # Numero di punti lungo la linea di integrazione
s = np.linspace(0, 1, N)  # Coordinate lungo la linea (m)

# Parametri del profilo gaussiano
n_e0 = 1e19    # Densità centrale (m^-3)
sigma_n = 0.2  # Larghezza del profilo gaussiano della densità (m)
B0 = 3.5       # Campo magnetico centrale (T)
sigma_B = 0.2  # Larghezza del profilo gaussiano del campo magnetico (m)
s0 = 0.5       # Posizione centrale dei profili (m)
T0 = 10000     # Temperatura centrale (eV)
sigma_T = 0.2  # Larghezza del profilo gaussiano della temperatura (m)

# Profili
n_e = gaussian_density_profile(s, n_e0, s0, sigma_n)  # Densità elettronica (m^-3)
B = gaussian_magnetic_profile(s, B0, s0, sigma_B)     # Campo magnetico (T)
T_e = gaussian_profile(s, T0, s0, sigma_T)            # Temperatura elettronica (eV)

# Frequenze ciclotroniche
nu_c = e * B / (2 * np.pi * m_e)  # Prima armonica
nu_2c = 2 * nu_c  # Seconda armonica

# Calcolo dello spessore ottico per prima e seconda armonica
tau_nu1 = trapz(kappa_nu(n_e, B, T_e, nu_c), s)
tau_nu2 = trapz(kappa_nu(n_e, B, T_e, nu_2c), s)

# Output
print(f"Spessore ottico alla prima armonica: {tau_nu1:.3f}")
print(f"Spessore ottico alla seconda armonica: {tau_nu2:.3f}")
nu_c = np.max(e * B / (2 * np.pi * m_e))/10**9
print(f"max frequenza ciclotronica: {nu_c} GHz")

#%%
# Plot dei profili
plt.figure(figsize=(10, 6))

# Densità elettronica
plt.subplot(3, 1, 1)
plt.plot(s, n_e, label=r'$n_e(s)$', color='b')
plt.xlabel('Posizione $s$ (m)')
plt.ylabel('Densità $n_e$ (m⁻³)')
plt.title('Profilo della Densità Elettronica')
plt.legend()
plt.grid()

# Campo magnetico
plt.subplot(3, 1, 2)
plt.plot(s, B, label=r'$B(s)$', color='r')
plt.xlabel('Posizione $s$ (m)')
plt.ylabel('Campo Magnetico $B$ (T)')
plt.title('Profilo del Campo Magnetico')
plt.legend()
plt.grid()

# Temperatura elettronica
plt.subplot(3, 1, 3)
plt.plot(s, T_e, label=r'$T_e(s)$', color='g')
plt.xlabel('Posizione $s$ (m)')
plt.ylabel('Temperatura $T_e$ (eV)')
plt.title('Profilo della Temperatura Elettronica')
plt.legend()
plt.grid()

# Mostra i plot
plt.tight_layout()
plt.show()
