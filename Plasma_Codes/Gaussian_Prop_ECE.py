#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:36:24 2025

@author: luca
"""

import numpy as np
import matplotlib.pyplot as plt

def gaussian_beam_profile(y, x, w0, lambda_):
    """
    Calcola l'intensità di un fascio gaussiano mentre si propaga nello spazio.
    """
    x_R = np.pi * w0**2 / lambda_  # Lunghezza di Rayleigh
    w_x = w0 * np.sqrt(1 + (x / x_R) ** 2)  # Larghezza del fascio
    return np.exp(-2 * (y / w_x) ** 2).T, w_x  # Trasposizione per coerenza con gli assi

# Parametri
w0 = 2.5  # Waist in cm
lambda_ = 0.5  # Lunghezza d'onda in cm
y = np.linspace(-15, 15, 400)  # Asse spaziale y in cm
x = np.linspace(0, 100, 200)  # Propagazione lungo x in cm

# Creazione della matrice dell'intensità
Y, X = np.meshgrid(y, x)
intensity, w_x = gaussian_beam_profile(Y, X, w0, lambda_)

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
img = ax.imshow(intensity, extent=[0, 100, -15, 15], origin='lower', cmap='inferno', aspect='auto')
plt.colorbar(img, label='Relative intensity')
ax.set_xlabel("Distance from waist (cm)")
ax.set_ylabel("Vertical Position (cm)")

# Aggiunta dei limiti della waist
w_x_values = w0 * np.sqrt(1 + (x / (np.pi * w0**2 / lambda_)) ** 2)
ax.plot(x, w_x_values, 'w--', label="Limite del fascio")
ax.plot(x, -w_x_values, 'w--')

# Aggiunta dei tick su entrambi i lati
ax.yaxis.set_ticks(np.arange(-15, 16, 2))
ax.yaxis.set_tick_params(labelright=True, right=True)  # Attiva i tick e le etichette anche a destra

plt.show()
