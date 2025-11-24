# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:34:00 2025

@author: Fernando
"""

import calculadora_indices as calc

def ejecutar_calculo_calorias_actividad() -> None:
    print("********************************************")
    print("*CÁLCULO DE CALORÍAS SEGÚN ACTIVIDAD FÍSICA*")
    print("********************************************")
    
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en centimetros: "))
    edad = int(input("Ingresa tu edad en años: "))
    genero = input("Ingresa tu género (H/M): ").upper()
    
    valor_genero = 5 if genero == "H" else -161
    valor_actividad = float(input("Ingresa tu nivel de actividad (por ejemplo 1.2 para baja, 1.55 para moderada, 1.9 para intensa): "))
    
    calorias = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print(f"Tu gasto calórico diario según actividad es: {calorias:.2f} calorías.")

ejecutar_calculo_calorias_actividad()
