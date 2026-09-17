nombre = input("Nombre completo: ").strip().upper()
domicilio = input("Domicilio: ").strip().upper()
correo = input("correo electrónico: ").strip().upper()
rfc = input("RFC: ").strip().upper().replace(" ","").replace( "-", "")

requisitos = True

#Validcaiónde nombre y domicilio
if len(nombre) < 3 or len(domicilio) < 3:
    print ("Eror en el largo de nombre o domicilio, deben ser de al menos 3 letras.")
    requisitos = False
else:
    print("El correo y domicilio cumplen con los requisitos")

#Validación de correo electrónico

if '@' in correo:

    ind_desp_arroba = correo.index("@")+1
    sub_cadena_delante = correo[ind_desp_arroba:len(correo)]
    if "." in sub_cadena_delante:
        print("El correo cumple los requisitos")
    else:
        print("El correo NO cumple los requisitos (no tiene TLD).")
    #end if-else
else:
    print("El correo no cumple los requisitos (no tiene arroba).")

if len(rfc) == 12 or len(rfc) == 13:
    print("RFC inválido")
    requisitos = False

if requisitos == TRUE
  print("Todos los requisitos son válidos")
if requisitos == FALSE
  print("Falta uno o más de los requisitos") 
    print("RFC
