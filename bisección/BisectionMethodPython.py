import numpy as np
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import pandas as pd

# Análisis Inicial
weight = np.linspace(-25, 25)
h = weight**2 + 27*weight + 12753/16

h_header = {'Libras': weight, 'Momentum': h}
data_h =  pd.DataFrame(data=h_header)


h = lambda weight : weight**2 + 27*weight + 12753/16
h(.5)

def bisection(g_x, initial, final):
    # Guardar variables de uso continuo
    x_i = 0
    x_p = 0
    x_n = 0
    
    # Escoger los primeros límites
        # Limite inicial se procura que sea g(x) positivo.
    if h(initial) > 0:
        x_p = initial
        x_n = final
        print(f"g({x_p}) > 0.")
    elif h(final) > 0:
        x_p = final
        x_n = initial
        print(f"g({x_p}) > 0.")
    
    #Crear una tabla con los valores.
    xtab_val = []
    ytab_val = []
    
    xtab_val.append(x_p)
    xtab_val.append(x_n)
    
    ytab_val.append(g(x_p))
    ytab_val.append(g(x_n))
    
    d = {'x': xtab_val, 'f(x)': ytab_val}
    df = pd.DataFrame(data=d)
    
    # Comienza la iteración
    keep_iter = True
    while keep_iter == True:
        # Se calcula el punto medio entre el rango x_p y x_n
        x_i = (x_p + x_n)/2
        
        # Se observa si hay cambio de signo
        if h(x_i) > 0:
            x_p = x_i
            #print(f"g({x_p}) > 0.")
        elif h(x_i) < 0:
            x_n = x_i
            #print(f"g({x_p}) > 0.")
        val_x = x_p
        val_y = h(x_p)
        df2 = {'x': val_x, 'f(x)': val_y} 
        df = df.append(df2, ignore_index = True) 
        display(df)         
        keep_iter = bool(input("Do you want to keep iterating?\n Type True to continue, type False to stop: "))
