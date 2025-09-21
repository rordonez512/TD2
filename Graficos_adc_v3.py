#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 17:09:16 2025

@author: roman
"""

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# --- Configuración ---
N_BITS = 12
VREF = 3.3
FILENAME = "datos.txt"

def main():
    # Cargar datos (ignorando las primeras líneas raras si las hubiera)
    data = np.loadtxt(FILENAME, delimiter=",",max_rows=1000) #, usecols=(0,1,2,3))


    tiempo = data[:, 0] - data[0, 0]   
    adc1 = data[:, 1]
    adc2 = data[:, 2]
    adc3 = data[:, 3]

    # Conversión a voltaje para adc1 y adc2 (adc3 parece otro tipo de dato, lo dejamos crudo)
    volt1 = adc1 * VREF / (2**N_BITS - 1)
    volt2 = adc2 * VREF / (2**N_BITS - 1)

    #Graficar
    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    axs[0].plot(tiempo, volt1, linewidth=1, label="Canal 1 [V]")
    axs[0].set_ylabel("Canal 1 [V]")
    axs[0].grid(True)
    axs[0].legend()

    axs[1].plot(tiempo, volt2, linewidth=1, label="Canal 2 [V]")
    axs[1].set_ylabel("Canal 2 [V]")
    axs[1].grid(True)
    axs[1].legend()

    axs[2].plot(tiempo, adc3, linewidth=1, label="Canal 3 [crudo]")
    axs[2].set_xlabel("Tiempo [ms]")
    axs[2].set_ylabel("Canal 3 [crudo]")
    axs[2].grid(True)
    axs[2].legend()

    fig.suptitle("Señales del potenciómetro")
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # deja espacio al título
    plt.show()

if __name__ == "__main__":
    main()
