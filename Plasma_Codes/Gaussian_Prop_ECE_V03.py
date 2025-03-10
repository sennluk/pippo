#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:38:54 2025

@author: luca
"""
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

# Calcola la frequenza ciclotronica e la lunghezza d'onda per una data armonica n
def cyclotron_freq_wavelength(B,n):
    # Costanti
    ce = 1.602e-19      # carica elettrone in COulomb
    me = 9.11e-31       # massa elettrone in Kg
    c = 299792458       # Vel lunce in m/sec
    pi = np.pi          # pi greco
    ###
    f_ce = (2*ce*B)/(2*pi*me)   #  Hz - Calcolo seconda armonica frequenza ciclotornica 
    lambda_ce = c/f_ce*100          # m - Lunghezza d'onda seconda armonica - in centimetri
    
    return f_ce, lambda_ce
   
def gaussian_beam_profile(y, x, w0, lambda_):
    """
    Calcola l'intensità di un fascio gaussiano mentre si propaga nello spazio.
    """
    x_R = np.pi * w0**2 / lambda_  # Lunghezza di Rayleigh
    w_x = w0 * np.sqrt(1 + (x / x_R) ** 2)  # Larghezza del fascio
    intensity = np.exp(-2 * (y / w_x) ** 2).T  # Trasposizione per coerenza con gli assi
    return intensity, w_x
################################


# Parametri
B = 3.5        # Campo magnetico in Tesla
n = 2          # Armonica 
w0 = 2         # Waist in cm - Dimensione antenna/2

x_range = 200  # Estensione simulazione asse x in cm
percent = 70   # Percentuale dell'intensità du
############


f_ce,lambda_ce = cyclotron_freq_wavelength(B, n)
print(f"Frequenza ciclotronica (2ª armonica) per B = {B} T: {f_ce/1e9:.2f} GHz")
print(f"Lunghezza d'onda ({n}ª armonica) per B = {B} T: {lambda_ce:.2f} cm")


y = np.linspace(-15, 15, 400)  # Asse spaziale y in cm
x = np.linspace(0, x_range, 10*x_range)  # Propagazione lungo x in cm

# Creazione della matrice dell'intensità
Y, X = np.meshgrid(y, x)
intensity, w_x = gaussian_beam_profile(Y, X, w0, lambda_ce)

# Calcolo della larghezza a 60% dell'intensità massima
threshold = (1-percent/100)  # Soglia del 60%
w_x_thresh = w_x * np.sqrt(-np.log(threshold) / 2)  # Larghezza trasversale corrispondente

# Plot
f = round(f_ce/10**9,2)
lamb = round(lambda_ce*10,2)  # tolgo decimale  e metto in mm

fig, ax = plt.subplots(figsize=(8, 5))
img = ax.imshow(intensity, extent=[0, x_range, -15, 15], origin='lower', cmap='inferno', aspect='auto')
plt.colorbar(img, label='Relative intensity')
ax.set_xlabel("Distance from waist (cm)")
ax.set_ylabel("Vertical Position (cm)")
# ax.set_title(f"B = {B} T, f_ce (2nd harm) = {f} GHz, Lambda = {lamb} mm, Waist = {w0} cm")

off= 0
trat = 10
spaz1 = 5
linw1 = 0.5
spaz2 = 5
linw2 = 0.5
linw3 = 0.5

# Curve del bordo del fascio (waist)
ax.plot(x, w_x, 'w--', linestyle = (off,(trat,spaz1)), lw = linw1, label="Limite del fascio (1/e²)")
ax.plot(x, -w_x, 'w--', linestyle = (off,(trat,spaz1)), lw = linw1)
ax.axvline(x=100, color='green', ls = '-.', lw = linw3)
ax.hlines(y=2.5, xmin=100, xmax=200, color='white', ls = '-.', lw = linw3)
ax.hlines(y=-2.5, xmin=100, xmax=200, color='white', ls = '-.', lw = linw3)

# Curve di demarcazione al 60% dell'intensità massima
ax.plot(x, w_x_thresh, 'c', linestyle = (off,(trat,spaz2)), lw = linw2, label=f"Limite {percent}% Intensità") # linestyle: offset, puintyi di tratto, punti di spazio
ax.plot(x, -w_x_thresh, 'c', linestyle = (off,(trat,spaz2)), lw = linw2)

# Aggiunta dei tick su entrambi i lati dell'asse y
ax.yaxis.set_ticks(np.arange(-14, 16, 2))
ax.yaxis.set_tick_params(labelright=True, right=True)  # Attiva i tick e le etichette anche a destra

# ax.legend()

plt.show()
plt.savefig('Fig_03_Gaussian_Prop.pdf',bbox_inches="tight", dpi=300)
