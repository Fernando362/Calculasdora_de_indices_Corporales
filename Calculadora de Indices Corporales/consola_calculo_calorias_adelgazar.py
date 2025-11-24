# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:35:00 2025

@author: Fernando
"""

import calculadora_indices as calc

def ejecutar_calculo_calorias_adelgazar() -> None:
    print("*******************************************")
    print("*CÁLCULO DE CALORÍAS DIARIAS PARA ADELGAZAR*")
    print("********************************************")
    
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en centimetros: "))
    edad = int(input("Ingresa tu edad en años: "))
    genero = input("Ingresa tu género (H/M): ").upper()
    
    valor_genero = 5 if genero == "H" else -161
    
    resultado = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(resultado)

ejecutar_calculo_calorias_adelgazar()

