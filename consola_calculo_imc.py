# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:31:00 2025

@author: Fernando
"""

import calculadora_indices as calc

def ejecutar_calculo_imc() -> None:
    print("******************************************")
    print("*CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)*")
    print("*******************************************")
    
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
    
    imc = calc.calcular_IMC(peso, altura)
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

ejecutar_calculo_imc()

