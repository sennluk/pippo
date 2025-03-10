#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:08:56 2025
@author: luca
Calcolo spessore ottico plasma-Tokamak
V00 : profili n,T, B lineari
"""

import numpy as np
from scipy.integrate import trapz

# Costanti fisiche
e = 1.602e-19  # Carica elettrone (C)
m_e = 9.109e-31  # Massa elettrone (kg)
c = 3.0e8  # Velocità della luce (m/s)

# Funzione per il coefficiente di assorbimento ciclotronico elettronico
def kappa_nu(n_e, B, nu):
    nu_c = e * B / (2 * np.pi * m_e)  # Frequenza ciclotronica
    return (e**2 / (m_e * c)) * (n_e / B) * (nu / nu_c)

# Dati simulati (da sostituire con i dati reali)
N = 100  # Numero di punti lungo la linea di integrazione
s = np.linspace(0, 1, N)  # Coordinate lungo la linea (m)
n_e = np.linspace(1e18, 5e18, N)  # Densità elettronica (m^-3)
B = np.linspace(1, 2, N)  # Campo magnetico (T)

# Frequenze ciclotroniche
nu_c = e * B / (2 * np.pi * m_e)  # Prima armonica
nu_2c = 2 * nu_c  # Seconda armonica

# Calcolo dello spessore ottico per prima e seconda armonica
tau_nu1 = trapz(kappa_nu(n_e, B, nu_c), s)
tau_nu2 = trapz(kappa_nu(n_e, B, nu_2c), s)

# Output
print(f"Spessore ottico alla prima armonica: {tau_nu1:.3f}")
print(f"Spessore ottico alla seconda armonica: {tau_nu2:.3f}")