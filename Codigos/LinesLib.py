# -*- coding: utf-8 -*-
"""
LinesScript:
    Script que prepara las lineas
"""
# Diccionario de lineas que vamos a marcar
"""
Nota: Lineas mas destacables

    Balmer(partes segundo nivel) https://es.wikipedia.org/wiki/Líneas_de_Balmer
        - Halpha (salto 2 --> 3): 6563 A
        -Hbeta (salto 2 --> 4): 4861 
        -HY (2--> 5): 4340 A
        -Hdelta (2-->6): 4107
        -Hepsi (2--> 7): 3970
        -Hchi (2-->8): 3889
        -Heta (2--> 9): 3835
        
    Lymann(partes del primer nivel) no las vemos en el optico, por eso no las tenemos en cuenta 
    (son de 1000 A)
    
    Calcio H y K 
    
    Helio I y He II
    
    Otros metales (Fe,Mg,Si)
"""

lineas_metalicas= {
    "Ca I 4227": 4227,
    "Ca II (K)": 3934,
    "Ca II (H)": 3968,
    "Mg II 4481": 4481,
    "Si IV (4089)": 4089,
    "Si III (4552)": 4552,
    "Si II (4128)": 4128,
    "Ti II 4179":4179,
    "Na (D2)": 5890
    }
lineas_fe= {
    "Fe I 4383": 4383,
    "Fe I 4271": 4271,
    "Fe II 4233": 4233,
    "Fe II 4172": 4172
    }

lineas_balmer= {
    r'$H_{\alpha}$': 6563,
    r'$H_{\beta}$': 4861,
    r'$H_{\gamma}$': 4340,
    r'$H_{\delta}$': 4102,
    r'$H_{\epsilon}$': 3970,   
    r'$H_{\delta}$ (h)': 4100 # Es de las lineas de Fraunhofer. https://arxiv.org/pdf/2410.07301 pg 4
    }

lineas_helio= {
    "He I 5875": 5875,
    "He I 4922": 4922,
    "He I 4713": 4713,
    "He I 4471": 4471,
    "He I 4388": 4388,
    "He I 4144": 4144,
    "He I 4120": 4120,
    "He II 4686": 4686,
    "He II 4542": 4542,
    "He II 4200": 4200,
    "He I + II 4026": 4026  
    }

lines= {}
lines.update(lineas_metalicas)
lines.update(lineas_balmer)
lines.update(lineas_helio)
lines.update(lineas_fe)

