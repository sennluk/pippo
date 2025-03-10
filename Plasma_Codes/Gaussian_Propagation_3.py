#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:48:20 2025

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
plt.figure(figsize=(8, 5))
plt.imshow(intensity, extent=[0, 100, -15, 15], origin='lower', cmap='inferno', aspect='auto')
plt.colorbar(label='Relative intensity')
plt.xlabel("Distance from waist (cm)")
plt.ylabel("Vertical Position (cm)")
# plt.title("Propagazione di un fascio gaussiano")

# Aggiunta dei limiti della waist
w_x_values = w0 * np.sqrt(1 + (x / (np.pi * w0**2 / lambda_)) ** 2)
plt.plot(x, w_x_values, 'w--', label="Limite del fascio")
plt.plot(x, -w_x_values, 'w--')
# plt.legend()

# Aggiunta dei tick su entrambi i lati
ax.yaxis.set_ticks(np.arange(-15, 16, 2))
ax.yaxis.set_tick_params(labelright=True, right=True)  # Attiva i tick e le etichette anche a destra

# Impostazione della scala verticale ogni centimetro
plt.yticks(np.arange(-15, 16, 2))


plt.show()
