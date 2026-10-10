import funcionesIMC

sistema = funcionesIMC.sistema_unidades()

peso, estatura = funcionesIMC.solicitar_datos(sistema)
print("Peso:",peso,"Estatura:", estatura)

imc = funcionesIMC.aplicar_formulas(peso, estatura, sistema)
print(f"Tu índice de masa corporal es: {imc:.2f}")
#resultado indice
resultado = funcionesIMC.mostrar_inidcadores(funcionesIMC.aplicar_formulas(peso, estatura, sistema))
print(resultado)