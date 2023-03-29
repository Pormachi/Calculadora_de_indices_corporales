import calculadora_indices as calc
peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en metros): "))
edad = int(input("Ingrese la edad de la persona: "))
valor_genero = float(input("Ingrese 0 (femenino) o 10.8 (masculino): "))
print(str(round(calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero),2))+'%')