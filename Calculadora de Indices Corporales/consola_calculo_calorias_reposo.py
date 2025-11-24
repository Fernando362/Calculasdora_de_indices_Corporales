# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:33:00 2025

@author: Fernando
"""

import calculadora_indices as calc

def ejecutar_calculo_calorias_reposo() -> None:
    print("*************************************")
    print("*CÁLCULO DE CALORÍAS EN REPOSO (TMB)*")
    print("*************************************")
    
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en centimetros: "))
    edad = int(input("Ingresa tu edad en años: "))
    genero = input("Ingresa tu género (H/M): ").upper()
    
    valor_genero = 5 if genero == "H" else -161
    
    tmb = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print(f"Tu Tasa Metabólica Basal (TMB) es: {tmb:.2f} calorías al día.")

ejecutar_calculo_calorias_reposo()
