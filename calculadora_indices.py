# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 22:05:48 2025

@author: Fernando
"""
# Calcula el índice de masa corporal de una persona a partir de la ecuación definida anteriormente.    
def calcular_IMC(peso: float, altura: float) -> float:
    return (peso / (altura) ** 2)

# Calcula el porcentaje de grasa de una persona a partir de la ecuación definida anteriormente. 
def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    IMC = peso / (altura ** 2)
    return (1.2 * IMC +  0.23 * edad - 5.4 - valor_genero)

# Calcula la cantidad de calorías que una persona quema estando en reposo (esto es, su tasa metabólica basal), 
# a partir de la ecuación definida anteriormente.   
def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    return (10 * peso + (6.25 * altura) - (5 * edad) + valor_genero)

# Calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad física 
# (esto es, su tasa metabólica basal según actividad física), a partir de la ecuación definida anteriormente.        
def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float) -> float:
    return ((10 * peso + (6.25 * altura) - (5 * edad) + valor_genero) * valor_actividad)

# Calcula el rango de calorías recomendado que debe consumir una persona diariamente en caso de que desee adelgazar, 
# a partir de la ecuación definida anteriormente.
def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int) -> str:
    TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero

    rango_inferior = TMB * 0.80
    rango_superior = TMB * 0.85

    # Retorno de la cadena formateada
    return f"Para adelgazar es recomendado que consumas entre: {rango_inferior:.2f} y {rango_superior:.2f} calorías al día."
