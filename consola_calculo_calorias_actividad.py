import calculadora_indices as calc
peso = float(input("Ingrese el peso de la persona (en kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en centimetros): "))
edad = int(input("Ingrese la edad de la persona: "))
valor_genero = float(input("Ingrese -161 (femenino) o 5 (masculino): "))
valor_actividad = float(input("Ingrese valor actividad: "))
print(str(round(calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero,valor_actividad),2))+' cal')