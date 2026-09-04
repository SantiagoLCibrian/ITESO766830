import math

def area_circulo(): 
    #entrada
    r = int(input("Medida del radio (cm)"))
    a = math.pi * r**2
    #salida
    print("Esta es la medida del círculo", a)
    #format string :.4f establece la cant de decimales impresos
    print(f"Esta es el área del círculo {a:.4f}")
    print("-----------------------------------------------------------------")
#SECCIÓN DE INVOCACIÓN DE FUNCIONES
area_circulo()

def distancia_eucllidiana():
    #Entarda
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    #Proceso
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    #Salida
    print(f"La distancia de p1({x1},{y2}) a  p2({x2},{y2}) es {d:.2f} unidades. " )
    print("-----------------------------------------------------------------")

#area_circulo()
distancia_eucllidiana()

#Algoritmo diferencia_temperatura
#Inicio
#
#1. Escribir: "Proporcionar temperaturas en grados Celsius: "
#2. Leer 
#3. t1 = float(leer)
#4. t2 = float(leer)
#5. dif_t = |t1-t2|
#6. escribir "La diferencia es de", dif_t "grados" 
#
#Fin

def diferencia_temperatura():
    t1 = float(input("Proporcionar temperatura 1 en grados Celsius: "))
    t2 = float(input("Proporcionar temperatura 2 en grados Celsius: "))

    dif_t = math.fabs(t1 - t2)
    print(f"La diferencia es de {dif_t:.1f} grados")
    print("-----------------------------------------------------------------")

diferencia_temperatura()

#Algoritmo puntos de un círculo
#Inicio
#1. Escribir "Proporsionar valor del radio"
#2. Escribir "Proporsionar valor del ángulo"
#3. Leer 
#4. r = radio
#5. gr = grados
#6. radianes = (grados * pi)/180
#7. x_c = radio * coseno(radian)
#8. y_c = radio * seno(radian)
#9. Escribir "Coordenadas (x, y) desde el punto de origen son:" 
#10. Escribir (x_c, y_c)
#
#Fin

def puntos_circ():
    r = float(input("Proporsionar valor del radio: "))
    gr = float(input("Proporsionar valor del ángulo: "))

    #convertor grad a rad
    rad = (gr * math.pi)/180

    # x & Y
    x_c = r*math.cos(rad)
    y_c = r*math.sin(rad)

    print ("Coordenadas (x, y) desde el punto de origen son:")
    print (f"({x_c:.2f}, {y_c:.2f})")

puntos_circ()
