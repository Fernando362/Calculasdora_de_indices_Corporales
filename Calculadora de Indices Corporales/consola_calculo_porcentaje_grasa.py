# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:32:00 2025

@author: Fernando
"""

import calculadora_indices as calc

def ejecutar_calculo_porcentaje_grasa() -> None:
    print("*****************************************")
    print("*CÁLCULO DEL PORCENTAJE DE GRASA CORPORAL*")
    print("******************************************")
    
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
    edad = int(input("Ingresa tu edad en años: "))
    genero = input("Ingresa tu género (H/M): ").upper()
    
    valor_genero = 10.8 if genero == "H" else 0
    
    grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print(f"Tu porcentaje de grasa corporal es: {grasa:.2f}%")

ejecutar_calculo_porcentaje_grasa()

