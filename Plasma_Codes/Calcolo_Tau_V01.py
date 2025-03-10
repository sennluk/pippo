#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:21:59 2025
@author: luca
Calcolo spessore ottico con profilo di temperatura
V01: profilo Te gaussiano
"""
import numpy as np
from scipy.integrate import trapz

# Costanti fisiche
e = 1.602e-19  # Carica elettrone (C)
m_e = 9.109e-31  # Massa elettrone (kg)
c = 3.0e8  # Velocità della luce (m/s)
k_B = 1.381e-23  # Costante di Boltzmann (J/K)

# Funzione per il profilo gaussiano della temperatura elettronica
def gaussian_profile(s, T0, s0, sigma):
    return T0 * np.exp(-((s - s0) ** 2) / (2 * sigma ** 2))

# Parametri scelti
t_max = 5000 # Max temperature electron in eV
n_max = 5e19 # Ma ne 

# Funzione per il coefficiente di assorbimento ciclotronico elettronico
def kappa_nu(n_e, B, T_e, nu):
    nu_c = e * B / (2 * np.pi * m_e)  # Frequenza ciclotronica
    return (e**2 / (m_e * c)) * (n_e / B) * (nu / nu_c) * np.exp(-e * nu / (k_B * T_e))

# Dati simulati (da sostituire con i dati reali)
N = 100  # Numero di punti lungo la linea di integrazione
s = np.linspace(0, 1, N)  # Coordinate lungo la linea (m)
n_e = np.linspace(1e18, 5e18, N)  # Densità elettronica (m^-3)
B = np.linspace(1, 2, N)  # Campo magnetico (T)
T_e = gaussian_profile(s, T0=t_max, s0=0.5, sigma=0.2)  # Temperatura elettronica (eV)

# Frequenze ciclotroniche
nu_c = e * B / (2 * np.pi * m_e)  # Prima armonica
nu_2c = 2 * nu_c  # Seconda armonica

# Calcolo dello spessore ottico per prima e seconda armonica
tau_nu1 = trapz(kappa_nu(n_e, B, T_e, nu_c), s)
tau_nu2 = trapz(kappa_nu(n_e, B, T_e, nu_2c), s)

# Output
print(f"Spessore ottico alla prima armonica: {tau_nu1:.3f}")
print(f"Spessore ottico alla seconda armonica: {tau_nu2:.3f}")