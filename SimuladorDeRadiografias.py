import os
os.system("cls")

VALOR_PLAN = 80000
VALOR_RADIOGRAFIA = 12000

banderaNum = False
banderaQuintil = False

try:
    nombre = input("Ingrese su Nombre\n").title()
    edad = int(input("Ingrese su Edad\n"))
    quintil = int(input("Ingrese su Quintil\n"))

    if edad >= 0:
        banderaNum = True

    if quintil >= 1 and quintil <= 5:
        banderaQuintil = True

    if banderaNum and banderaQuintil:
        descuento_plan = 0

        if edad > 45:
            descuento_plan = 0
        elif edad <= 25:
            if quintil == 1 or quintil == 2:
                descuento_plan = 0.18
            elif quintil == 3 or quintil == 4:
                descuento_plan = 0.12
        elif edad >= 26 and edad <= 45:
            if quintil == 1 or quintil == 2:
                descuento_plan = 0.12
            elif quintil == 3 or quintil == 4:
                descuento_plan = 0.08
            
        valor_dcto_plan = VALOR_PLAN * descuento_plan
        valor_finalP = VALOR_PLAN - valor_dcto_plan

        dcto_radiografia = 0

        if quintil == 1 or quintil == 2 or quintil == 3:
            dcto_radiografia = 0.10
            if edad >= 40:
                dcto_radiografia = 0.10 + 0.05
        
        valor_dcto_radiografia = VALOR_RADIOGRAFIA * dcto_radiografia
        valor_finalR = VALOR_RADIOGRAFIA - valor_dcto_radiografia

        valor_final = valor_finalP + valor_finalR

        valor_finalP_red = round(valor_finalP)
        valor_finalR_red = round(valor_finalR)
        valor_final_red = round(valor_final)

        os.system("cls")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Quintil: {quintil}")
        print(f"Valor Final Plan Dental: ${valor_finalP_red}")
        print(f"Valor Final Radiografia: ${valor_finalR_red}")
        print(f"Total Final a Pagar: ${valor_final_red}")
    else:
        os.system("cls")
        print("Algunos datos no son correctos.")
except:
    os.system("cls")
    print("El valor debe ser Numérico")
    