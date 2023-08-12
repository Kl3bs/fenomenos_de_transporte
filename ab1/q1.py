import numpy as np
import matplotlib.pyplot as plt



def d(x,a,b,c):
        return a*x**2 + b*x + c

radius = np.array([6377, 6378, 6379, 6380, 6381, 6382, 6383, 6385, 6387, 6392, 6397, 6402])
density = np.array([1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.5258, 0.4135, 0.1948, 0.08891, 0.04008])


#A) Obter a relacao da variacao da densidade com a altitude


coefficients = np.polyfit(density, radius,2)

a = coefficients[0]
b = coefficients[1]
c = coefficients[2]

print(d(7000,a,b,c))
 
        
        
  

#B) Calcular a massa  da atmosfera usado a correlacao obtida.

#6377 + 25
# p_atm = 0.04008

# v_planet = (4*np.pi*pow(6402,3))/3

# mass = v_planet*p_atm
# print("{:.2e}".format(mass), 'Kg')   
