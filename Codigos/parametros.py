"""
parametros:
    Se encarga de tomar los archivos y calcular
    diversos parametros como la Temperatura y demas
"""

import numpy as np

#%% Temperatura

def get_Temp(lamb,flux): #Saca temperatura con Ley Wien
    """
    Ley de Wien: 
        lamb_max*T= b
    """

    b= 2.8976e-7 #Angstrom

    index= np.where(np.max(flux))
    """
    Index toma la posicion del maximo del flujo y se la guarda para luego
    poder sacar la longitud de onda que tenga esa posicion en el array de longitudes
    de onda
    """

    lamb_max= lamb[index]

    T= b/lamb_max

    return T
