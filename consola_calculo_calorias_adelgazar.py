import calculadora_indices as calc
peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en centimetros): "))
edad = int(input("Ingrese la edad de la persona: "))
valor_genero = float(input("Ingrese -161 (femenino) o 5 (masculino): "))
calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
