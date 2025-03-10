#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:44:33 2025

@author: luca
"""

import numpy as np
import matplotlib.pyplot as plt

def gaussian_beam_profile(x, z, w0, lambda_):
    """
    Calcola l'intensità di un fascio gaussiano mentre si propaga nello spazio.
    """
    z_R = np.pi * w0**2 / lambda_  # Lunghezza di Rayleigh
    w_z = w0 * np.sqrt(1 + (z / z_R) ** 2)  # Larghezza del fascio
    return np.exp(-2 * (x / w_z) ** 2)

# Parametri
w0 = 5  # Waist in cm
lambda_ = 0.5  # Lunghezza d'onda in cm
x = np.linspace(-15, 15, 400)  # Asse spaziale x in cm
z = np.linspace(0, 100, 200)  # Propagazione lungo z in cm

# Creazione della matrice dell'intensità
X, Z = np.meshgrid(x, z)
intensity = gaussian_beam_profile(X, Z, w0, lambda_)

# Plot
plt.figure(figsize=(8, 5))
plt.imshow(intensity, extent=[-15, 15, 0, 100], origin='lower', cmap='inferno', aspect='auto')
plt.colorbar(label='Intensità relativa')
plt.xlabel("Posizione x (cm)")
plt.ylabel("Distanza di propagazione z (cm)")
plt.title("Propagazione di un fascio gaussiano")
plt.show()


# Aggiunta dei limiti della waist
w_z_values = w0 * np.sqrt(1 + (z / (np.pi * w0**2 / lambda_)) ** 2)
plt.plot(w_z_values, z, 'w--', label="Limite del fascio")
plt.plot(-w_z_values, z, 'w--')
plt.legend()

plt.show()