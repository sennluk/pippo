#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:38:54 2025

@author: luca
"""
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')


def cyclotron_freq_wavelength(B,n):
    fce = (2*ce*B)/(2*pi*me)#/10**9  # Calcolo seconda armonica frequenza ciclotornica 
    
def gaussian_beam_profile(y, x, w0, lambda_):
    """
    Calcola l'intensità di un fascio gaussiano mentre si propaga nello spazio.
    """
    x_R = np.pi * w0**2 / lambda_  # Lunghezza di Rayleigh
    w_x = w0 * np.sqrt(1 + (x / x_R) ** 2)  # Larghezza del fascio
    intensity = np.exp(-2 * (y / w_x) ** 2).T  # Trasposizione per coerenza con gli assi
    return intensity, w_x

# Costanti
ce = 1.602e-19 # carica elettrone in COulomb
me = 9.11e-31 # massa elettrone in Kg
c = 299792458 # Vel lunce in m/sec
pi = np.pi

# Parametri
B = 3.5 # Campo magnetico in Tesla
w0 = 4  # Waist in cm - Dimensione antenna/2
lambda_ = 0.6  # Lunghezza d'onda in cm
x_range = 100 # Estensione simulazione asse x in cm
percent = 60 # Percentuale dell'intensità du

y = np.linspace(-15, 15, 400)  # Asse spaziale y in cm
x = np.linspace(0, x_range, 2*x_range)  # Propagazione lungo x in cm

############


lam_est = c/fce # Lunghezza d'onda seconda armonica - in metri
sec_nd = lam_est*100 # Lunghezza d'onda seconda armonica in cm
 


# Creazione della matrice dell'intensità
Y, X = np.meshgrid(y, x)
# intensity, w_x = gaussian_beam_profile(Y, X, w0, lambda_)
intensity, w_x = gaussian_beam_profile(Y, X, w0, sec_nd)

# Calcolo della larghezza a 60% dell'intensità massima
threshold = 0.4  # Soglia del 60%
w_x_60 = w_x * np.sqrt(-np.log(threshold) / 2)  # Larghezza trasversale corrispondente

# Plot
lamb = round(sec_nd,2)
f = round(fce/10**9,2)

fig, ax = plt.subplots(figsize=(8, 5))
img = ax.imshow(intensity, extent=[0, x_range, -15, 15], origin='lower', cmap='inferno', aspect='auto')
plt.colorbar(img, label='Relative intensity')
ax.set_xlabel("Distance from waist (cm)")
ax.set_ylabel("Vertical Position (cm)")
ax.set_title(f"B = {B} T, fce = {f} GHz, L(2nd harm) = {lamb} cm, Waist = {w0} cm")

# Curve del bordo del fascio (waist)
ax.plot(x, w_x, 'w--', label="Limite del fascio (1/e²)")
ax.plot(x, -w_x, 'w--')

# Curve di demarcazione al 60% dell'intensità massima
ax.plot(x, w_x_60, 'c--', label="Limite 60% Intensità")
ax.plot(x, -w_x_60, 'c--')

# Aggiunta dei tick su entrambi i lati dell'asse y
ax.yaxis.set_ticks(np.arange(-15, 16, 2))
ax.yaxis.set_tick_params(labelright=True, right=True)  # Attiva i tick e le etichette anche a destra

# ax.legend()

plt.show()
