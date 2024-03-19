import numpy as np
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import pandas as pd

#Programa de Jacobi
x_1 = lambda x_2_p=0, x_3_p=0 : (610-(x_2_p+ 3*x_3_p))/2
x_2 = lambda x_1_p, x_3_p=0 : (510-(x_1_p+ 3*x_3_p))/3
x_3 = lambda x_1_p, x_2_p : (960-(4*x_1_p+ 3*x_2_p))/2

def Jacobi():
    #First Operation
    v_x_1 = x_1()
    v_x_2 = x_2(v_x_1)
    v_x_3 = x_3(v_x_1, v_x_2)
    
    #Initial Iteration done:
    repetitions = 0
    print(f"Initial values: {repetitions}\n")
    
    #Save variables in table:
    re_v_x_1 = v_x_1
    re_v_x_2 = v_x_2
    re_v_x_3 = v_x_3

    x1_tab_val = []
    x2_tab_val = []
    x3_tab_val = []
    
    x1_tab_val.append(re_v_x_1)
    x2_tab_val.append(re_v_x_2)
    x3_tab_val.append(re_v_x_3)
    
    d = {'x_1': x1_tab_val, 'x_2': x2_tab_val, 'x_3': x3_tab_val}
    df = pd.DataFrame(data=d)
    display(df) 
    
    #Recursive Operation calculation
    keep_iter = True
    while keep_iter == True:
        
        #Number of Repetitions
        print("______________________________________\n")
        repetitions += 1
        print(f"Repetition number: {repetitions}\n")
        
        #Operations to declare variables
        re_v_x_1 = x_1(re_v_x_2, re_v_x_3)
        re_v_x_2 = x_2(re_v_x_1, re_v_x_3)
        re_v_x_3 = x_3(re_v_x_1, re_v_x_2)
        
        #Update table
        d2 = {'x_1': re_v_x_1, 'x_2': re_v_x_2, 'x_3': re_v_x_3}
        df = df.append(d2, ignore_index = True) 
        display(df)
        
        
        #Save Variables with new values
        v_x_1 = re_v_x_1
        v_x_2 = re_v_x_2
        v_x_3 = re_v_x_3
        
        #Continue yes or no?
        keep_iter = bool(input("\nDo you want to keep iterating?\n Type True to continue, type False to stop: "))

    
    return v_x_1, v_x_2, v_x_3

if __name__ == "__main__":
    Jacobi()