#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:39:22 2018

@author: lisandro
"""

#Librerias

import numpy as np
import matplotlib.pyplot as plt

#Funciones

def rectangular(N):
    
    wr = np.ones((N,1),dtype = float)
    
    return wr

def bartlett(N):
    
    n = np.linspace(0,N-1,N)
    
    wt = (1 - (np.abs(2*n - N + 1)/(N+1))).reshape(N,1)
    
    return wt

def hann(N):
    
    n = np.linspace(0,N-1,N)
    
    whn = (0.5 * (1 - np.cos( (2*np.pi*n)/(N-1) ))).reshape(N,1)
    
    return whn

def hamming(N):
    
    n = np.linspace(0,N-1,N)
    
    whm = (0.54 - 0.46*np.cos( (2*np.pi*n)/(N-1) )).reshape(N,1)
    
    return whm

def blackman(N):
    
    n = np.linspace(0,N-1,N)
    
    wb = (0.42 - 0.5*np.cos( (2*np.pi*n)/(N-1) ) + 0.08*np.cos( (4*np.pi*n)/(N-1) )).reshape(N,1)
    
    return wb

def flattop(N):
    
    n = np.linspace(0,N-1,N)
    
    wft = (1 - 1.93*np.cos( (2*np.pi*n)/(N-1) ) + 1.29*np.cos( (4*np.pi*n)/(N-1) ) - 0.388*np.cos( (6*np.pi*n)/(N-1) ) + 0.028*np.cos( (8*np.pi*n)/(N-1) )).reshape(N,1)
    
    wft = wft/np.max(wft)
    
    return wft

#Testbench
    
def testbench():
    
    #Cantidad de muestras
    N = 1024
    
    #Genera una ventana tipo bartlett(triangular)
    wt = bartlett(N)
    
    #Presentacion grafica de los resultados temporales
    plt.figure()
    plt.title('Ventana de Bartlett, N = ' + str(N))
    plt.plot(wt)
    plt.xlabel('n')
    plt.ylabel('wt[n]')
    plt.grid()
    
    #Genera ventana tipo hanning
    whn = hann(N)
    
    #Presentacion grafica de los resultados temporales
    plt.figure()
    plt.title('Ventana de Hann, N = ' + str(N))
    plt.plot(whn)
    plt.xlabel('n')
    plt.ylabel('whn[n]')
    plt.grid()
    
    #Genera ventana tipo hamming
    whm = hamming(N)
    
    #Presentacion grafica de los resultados temporales
    plt.figure()
    plt.title('Ventana de Hamming, N = ' + str(N))
    plt.plot(whm)
    plt.xlabel('n')
    plt.ylabel('whm[n]')
    plt.grid()

    #Genera ventana tipo blackman
    wb = blackman(N)
    
    #Presentacion grafica de los resultados temporales
    plt.figure()
    plt.title('Ventana de Blackman, N = ' + str(N))
    plt.plot(wb)
    plt.xlabel('n')
    plt.ylabel('wb[n]')
    plt.grid()

    #Genera ventana tipo flattop
    wft = flattop(N)
    
    #Presentacion grafica de los resultados temporales
    plt.figure()
    plt.title('Ventana FlatTop, N = ' + str(N))
    plt.plot(wft)
    plt.xlabel('n')
    plt.ylabel('wft[n]')
    plt.grid()
