#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:42:50 2025

@author: luca
"""

import numpy as np
import matplotlib.pyplot as plt

def gaussian_beam(x, w0):
    """
    Calcola l'intensità di un fascio gaussiano con waist w0.
    """
    return np.exp(-2 * (x / w0) ** 2)

# Parametri
w0 = 5  # Waist in cm
x = np.linspace(-15, 15, 400)  # Asse spaziale in cm

# Calcola il profilo del fascio
intensity = gaussian_beam(x, w0)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, intensity, label=f'Waist = {w0} cm', color='b')
plt.xlabel("Posizione (cm)")
plt.ylabel("Intensità relativa")
plt.title("Profilo di un fascio gaussiano")
plt.legend()
plt.grid()
plt.show()
