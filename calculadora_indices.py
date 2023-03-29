def calcular_IMC(peso: float, altura: float) -> float:
    '''Calcula el índice de masa corporal de una persona 
    a partir de la ecuación definida anteriormente.'''
    IMC = peso/(altura)**2
    return IMC

def calcular_porcentaje_grasa(peso: float, altura: float, edad: float, valor_genero: float) -> float:
    '''Calcula el porcentaje de grasa de una persona a partir de la ecuación
    definida anteriormente'''
    #valor_genero = 0 (femenino)
    #valor_genero = 10.8 (masculino)
    GC = 1.2*calcular_IMC(peso, altura) + 0.23*edad -5.4 - valor_genero
    return GC

def calcular_calorias_en_reposo(peso: float, altura: float,edad: int, valor_genero: int) -> float:
    '''Calcula la cantidad de calorías que una persona quema estando en reposo
    (esto es, su tasa metabólica basal), a partir de la ecuación definida
    anteriormente.'''
    #valor_genero = -161 (femenino)
    #valor_genero = 5 (masculino)
    TMB = 10*peso + 6.25*altura -5*edad + valor_genero
    return TMB

def calcular_calorias_en_actividad(peso: float, altura: float,edad: int, valor_genero: float, valor_actividad: float) -> float:
    '''Calcula la cantidad de calorías que una persona quema al realizar algún tipo
    de actividad física (esto es, su tasa metabólica basal según actividad física),
    a partir de la ecuación definida anteriormente.'''
    #1.2: poco o ningún ejercicio
    #1.375: ejercicio ligero (1 a 3 días a la semana)
    #1.55: ejercicio moderado (3 a 5 días a la semana)
    #1.72: deportista (6 -7 días a la semana)
    #1.9: atleta (entrenamientos mañana y tarde.
    TMB_actividad_fisica = calcular_calorias_en_reposo(peso, altura,edad, valor_genero)*valor_actividad
    return TMB_actividad_fisica

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: float) -> str:
    '''Calcula el rango de calorías recomendado, que debe consumir una persona
    diariamente en caso de que desee adelgazar, a partir de la ecuación
    definida anteriormente.'''
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print("Para adelgazar es recomendado que consumas entre: " + str(round(TMB*80/100,2)) + " y " + str(round(TMB*85/100,2)) + " calorias al día.")
    