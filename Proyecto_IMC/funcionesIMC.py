def esta_en_rango(valor_minimo, valor_maximo, valor):
    if valor >= valor_minimo and valor <= valor_maximo:
        return True
    else:
        return False
    #end if-else

def sistema_unidades():
    while True:
        sistema = int(input("1) Imperial (lb/in)\n2) Métrico (kg/m)\n¿Qué sistema vas a utilizar? "))
        if sistema > 2 or sistema < 1:
            print("Valor no válido. Escoge entre 1 o 2 nub")
        else:
            if sistema == 1: print("Sistema imperial seleccionado")
            else: print("Sistema métrico seleccionado")
            #end if-else
            break
        #end if-else
    return sistema


def solicitar_datos(sistema):
    if sistema == 1:
        u_peso = "lb"
        u_estatura = "ft"
    else:
        u_peso = "kg"
        u_estatura = "m"

    peso = float(input(f"Ingresa el peso en {u_peso}: "))
    estatura = float(input(f"Ingresa la estatura en {u_estatura}: "))
    if sistema == 1:
        if esta_en_rango(0,667,peso):
            return peso, estatura
        else:
            print("Error peso o estatura. Favor de volver a capturar")
    else:
        if esta_en_rango(0,300, peso) and esta_en_rango(0,3,estatura):
            return peso, estatura
        else:
            print("Error en peso o estatura. Vuelve a capturar")

def aplicar_formulas(peso, estatura, sistema):
    if sistema == 1:
        imc = (peso*0.453)/(estatura*0.3048)**2
    else:
        imc = (peso/estatura**2)
    return imc

def mostrar_inidcadores(imc, indice=None):
    if imc<18.5: 
        indice = "bajo peso"
    if imc >= 18.5 and 24.9>imc: 
        indice = "indice normal"
    if imc >= 25 and 29.9>imc: 
        indice = "Sobrepeso"
    if imc >= 30 and 39.9>imc: 
        indice = "Obesidad"
    elif imc > 40: 
        indice = "Obesidad mórbida" 
    return indice

