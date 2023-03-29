import calculadora_indices as calc
peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en metros): "))
print(round(calc.calcular_IMC(peso, altura),2))