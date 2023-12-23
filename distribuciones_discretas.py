# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:21:43 2023

@author: marti
"""

import random
import matplotlib.pyplot as plt

#%%

#################################3

#SIMULACIÓN DE LA GENERACIÓN DE VARIABLES ALEATORIAS DISCRETAS QUE SIGUEN

###################################


#%%

def generar_n_variables_aleatorias(n, p, distribucion):
    
    variables = []
    
    for i in range(0, n):
        y = distribucion(p)
        variables.append(y)
        
    return variables

#%%


#Distribución de Bernoulli

def distribucion_bernoulli(p):
    
    #genero el valor de éxito de la variable aleatoria
    r = random.random()
    
    if r <= p:
        return 1 #éxito
    else:
        return 0 #fracaso
    

p = 0.7
y = distribucion_bernoulli(p)
print(f'Variable aleatoria que sigue una distribución de Bernoulli: {y}')

#%%

#Gráfico

valores = generar_n_variables_aleatorias(100, 0.7, distribucion_bernoulli)

plt.figure()
plt.hist(x=valores)
plt.xlabel("Valor de la variable aleatoria discreta")
plt.ylabel("Frecuencia")
plt.title("Distribución de Bernoulli")


del valores
#%%

#Distribución Binomial

#dadas n variables y p la probabilidad de éxito
def distribucion_binomial(n, p):
    
    #podemos expresar a y como suma de variables aleatorias de bernoulli
    
    y = 0 #cantidad de éxitos
    
    for i in range(0, n):
       y += distribucion_bernoulli(p)
        
    return y 

p = 0.7
n = 3
y = distribucion_binomial(n, p)
print(f'Variable aleatoria que sigue una distribución Binomial: {y}')


#%%

#Gráfico

valores = []

n = 1000
p = 0.4

for i in range(0, n):
    y = distribucion_binomial(n, p)
    valores.append(y)

plt.figure()
plt.hist(x=valores, range=(0, n), bins=n)
plt.xlabel("Valor de la variable aleatoria discreta")
plt.ylabel("Frecuencia")
plt.title("Distribución Binomial")


del valores

#%%

#Distribución geométrica

def distribucion_geometrica(p):
    
    #número de intentos hasta que se cumpla que R_i <= p
    m = 1
    
    while True:
        
        r = random.random()
        
        if r <= p:
            break
        else:
            m += 1
            
    y = m
    
    return y


p = 0.1
y = distribucion_geometrica(p)
print(f'Variable aleatoria que sigue una distribución Geométrica: {y}')

#%%

#Gráfico

p = 0.01
n = 1000
valores = generar_n_variables_aleatorias(n, p, distribucion_geometrica)
rango = (min(valores), max(valores))

plt.figure()
plt.hist(x=valores, range=rango)
plt.xlabel("Valor de la variable aleatoria discreta")
plt.ylabel("Frecuencia")
plt.title("Distribución Geométrica")


del valores

#%%

#Distribución Binomial 

#r = résimo éxito
def distribucion_binomial_negativa(p, r):
    
    #cantidad de intentos hasta obtener el résimo éxito
    y = 0
    
    for i in range(0, r):
        y += distribucion_geometrica(p)
        
    return y

p = 0.1
r = 2
y = distribucion_binomial_negativa(p, r)
print(f'Variable aleatoria que sigue una distribución Binomial Negativa: {y}')


#%%

#Gráfico


n = 1000
p = 0.2
r = 16
valores = []

for i in range(0, n):
    y = distribucion_binomial_negativa(p, r)
    valores.append(y)

plt.figure()
plt.hist(x=valores, range=(0, n), bins=n)
plt.xlabel("Valor de la variable aleatoria discreta")
plt.ylabel("Frecuencia")
plt.title("Distribución Binomial Negativa")


del valores