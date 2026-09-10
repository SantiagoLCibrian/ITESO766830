#Santiago López Cibrián | O2026_ESI3890E | Sesión 7 | 8 de septiembre de 2026

print("------------Ejercicio I ------------")
nombre_2 = None

nombre_1 = str(input("-Proporciona tu primer nombre \n"))
nombre_2 = str(input("-En caso de tener. Proporciona tu segundo nombre \n (De lo contrario presione ENTER) \n" ))
apellido_1 = str(input("-Proporciona tu primer apellido \n"))
apellido_2 = str(input("-Proporciona tu segundo apellido \n"))

nombre_completo = (f"{nombre_1} {nombre_2} {apellido_1} {apellido_2}").upper()

print("------------Ejercicio II------------") 

if nombre_2 == None :
    nombre_completo.replace(nombre_2, "")
else:
    print (f"-Su nombre completo es: {nombre_completo}")

print("------------Ejercicio III------------")
nombrecompleto = nombre_completo.replace(" ", "")
print(f"Primer caracter:  {nombrecompleto[0]}\nQuinto caracter:  {nombrecompleto[5]}\nSéptimo caracter: {nombrecompleto[7]}\nÚltimo caracter:  {nombrecompleto[-1]}") 

print("------------Ejercicio IV------------")
if nombre_2 is "" :
    acronimo = (f"{nombre_1[0]}.{apellido_1[0]}.{apellido_2[0]}")  
else:
    acronimo = (f"{nombre_1[0]}.{nombre_2[0]}.{apellido_1[0]}.{apellido_2[0]}")   

print(acronimo)

print("------------Ejercicio V------------")
s = input("Proporcionar letra o frase ").upper()
s in nombre_completo
vnombre_completo = nombre_completo.count(s)

print(s in nombre_completo)
print(f"La letra o frase {s} se encuentra {vnombre_completo} cantidad de veces en su nombre completo.")

print("------------Ejercicio VI------------")
completo_nombre = ''.join(reversed(nombre_completo))
print(f"{nombre_completo} \n{completo_nombre}")

print("------------Ejercicio VII------------")
print(f"Su nombre completo cuenta con {len(nombrecompleto)} letras\n")

print("------------Ejercicio VIII------------")
correo = input("Introducir correo electrónico: ").lower()

usuario = correo[0:correo.index("@")]
dominio = correo[correo.index("@"):correo.index(".")]
tdl = correo[correo.index("."): ]

print(f"Usuario: {usuario}\nDominio: {dominio}\nTDL: {tdl}")

print("------------Ejercicio IX------------")
codigo_1 = 120
producto_1 = "capuccino 250ml(2)" 
precio_2 = int(950)/100

codigo_2 = 100
producto_2 = "botella con agua 600ml(1)"
precio_1 = int(120)/100

codigo_3 = 132
producto_3 = "pay de manzana 115gr(1)"
precio_3 = int(525)/100

print(f"codigo") 
print(f"{codigo_1:06d} | {producto_1:<15} | ${precio_1}")
print(f"{codigo_2:06d} | {producto_2:<15} | ${precio_2}")
print(f"{codigo_3:06d} | {producto_3:<15} | ${precio_3}")

"""
[LOG]
+ Aprendí: Más formas de manipular las strings y los índices. 
! Me confundí en: Implementar el segundo nombre opcional y el problema IX 
> Próximo paso: Repasar y checar el hipervínculo de w3 schools con más ejercios de python. 
"""
