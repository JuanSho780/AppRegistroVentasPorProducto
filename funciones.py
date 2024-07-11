import random
import ast

def ingresar_laptop():
    print("""
-------------------------------------------------------------------------------""")
    print("""
Ingrese los datos de la nueva Laptop (escriba SALIR para volver al inicio):
    """)
    descripcion = input("Descripción: ")
    if descripcion == "SALIR":
        return 0
    importado = input("Importado (SI o NO): ")
    if importado == "SI":
        importado = True
    else:
        importado = False
    codigo = generar_codigo()
    costoal = random.randint(20000, 45000)/100
    costofund = random.randint(8000, 15000)/100
    preciovent = costoal*1.25
    
    dicc = {
        "Tipo": "Laptop",
        "Descripción": descripcion,
        "Importado": importado,
        "Código": codigo,
        "Costo de almacenamiento": costoal,
        "Costo de funda": costofund,
        "Precio de venta": preciovent
        }
    
    with open("laptops.txt", "a") as file:
        file.write(str(dicc) + "\n")
    return None

def ingresar_desktop():
    print("""
-------------------------------------------------------------------------------""")
    print("""
Ingrese los datos de la nueva Desktop (escriba SALIR para volver al inicio):
    """)
    descripcion = input("Descripción: ")
    if descripcion == "SALIR":
        return 0
    importado = input("Importado (SI o NO): ")
    if importado == "SI":
        importado = True
    else:
        importado = False
    codigo = generar_codigo()
    
    while True:
        rnd = random.randint(18000, 25000)
        if rnd % 3 == 0:
            costoal = rnd/100
            break
   
    costofund = random.randint(15000, 25000)/100
    preciovent = costoal*1.25
    
    dicc = {
        "Tipo": "Desktop",
        "Descripción": descripcion,
        "Importado": importado,
        "Código": codigo,
        "Costo de almacenamiento": costoal,
        "Costo de funda": costofund,
        "Precio de venta": preciovent
        }
    
    with open("Desktops.txt", "a") as file:
        file.write(str(dicc) + "\n")
    return None

def ingresar_impresora():
    print("""
-------------------------------------------------------------------------------""")
    print("""
Ingrese los datos de la nueva Impresora (escriba SALIR para volver al inicio):
    """)
    descripcion = input("Descripción: ")
    if descripcion == "SALIR":
        return 0
    importado = input("Importado (SI o NO): ")
    
    if importado == "SI":
        importado = True
    else:
        importado = False
    codigo = generar_codigo()
    
    while True:
        rnd = random.randint(9000, 15000)
        if rnd % 2 == 0:
            costoal = rnd/100
            break

    preciovent = costoal*1.25
    
    dicc = {
        "Tipo": "Impresora",
        "Descripción": descripcion,
        "Importado": importado,
        "Código": codigo,
        "Costo de almacenamiento": costoal,
        "Precio de venta": preciovent
        }
    
    with open("Impresoras.txt", "a") as file:
        file.write(str(dicc) + "\n")
    return None

def generar_codigo():
    while True:
        rnd = random.randint(20000, 90000)
        if rnd % 7 == 0:
            codigo = rnd
            break
    return codigo

def leer_laptops():
    file = open("Laptops.txt", "r")
    lines = file.readlines()
    resp = []
    for line in lines:
        laptop_str = line.strip()
        laptop = ast.literal_eval(laptop_str)
        resp.append(laptop)
    return resp

def venta_laptops():
    laptops = leer_laptops() #laptops es una lista de diccionarios con las laptops ingresadas
    print("""
Tiene las siguientes opciones de venta:
    """)
    for laptop in laptops:
        print(str(laptop["Código"]) + ", " + str(laptop["Descripción"]))
    print("")
    valor = True
    while valor:
        codigo = input("Ingrese el código de la laptop a registrar (escriba SALIR para volver): ")
        i = -1
        no_valor = 0
        if codigo == "SALIR":
            return 0
        else:
            codigo = int(codigo)
            for j in range(0, len(laptops)):
                if laptops[j]["Código"] == codigo:
                    i = j
                    valor = False
                    break
                else:
                    no_valor += 1
            if no_valor == len(laptops):
                print("""
    -------------------Por favor, ingrese un código válido-------------------------
    """)      
    cantidad = int(input("Ingrese la cantidad de estas: "))
    laptops[i]["Cantidad de la venta"] = cantidad
    
    ventas = leer_ventas() #lista de diccionarios con las ventas registradas
    if len(ventas) == 0:
        laptops[i]["Número de la venta"] = 20000
    else:
        mayor_codigo = 0
        for venta in ventas:
            if venta["Número de la venta"] > mayor_codigo:
                mayor_codigo = venta["Número de la venta"]
                laptops[i]["Número de la venta"] = mayor_codigo + 1
                
    laptops[i]["Venta total"] = laptops[i]["Precio de venta"]*cantidad
    with open("VentaRegistrada.txt", "a") as file:
        file.write(str(laptops[i]) + "\n")
    
def leer_desktops():
    file = open("Desktops.txt", "r")
    lines = file.readlines()
    resp = []
    for line in lines:
        desktop_str = line.strip()
        desktop = ast.literal_eval(desktop_str)
        resp.append(desktop)
    return resp

def venta_desktops():
   desktops = leer_desktops() #desktops es una lista de diccionarios con las desktops ingresadas
   print("""
Tiene las siguientes opciones de venta:
    """)
   for desktop in desktops:
        print(str(desktop["Código"]) + ", " + str(desktop["Descripción"]))
   print("")
   valor = True
   while valor:
       codigo = input("Ingrese el código de la desktop a registrar (escriba SALIR para volver): ")
       if codigo == "SALIR":
           return 0
       else:
           codigo = int(codigo)
           i = -1
           no_valor = 0
           for j in range(0, len(desktops)):
               if desktops[j]["Código"] == codigo:
                   i = j
                   valor = False
                   break
               else:
                   no_valor += 1
                   if no_valor == len(desktops):        
                       print("""
            -------------------Por favor, ingrese un código válido-------------------------
            """)      
   cantidad = int(input("Ingrese la cantidad de estas: "))
   desktops[i]["Cantidad de la venta"] = cantidad
   
   ventas = leer_ventas() #lista de diccionarios con las ventas registradas
   if len(ventas) == 0:
       desktops[i]["Número de la venta"] = 20000
   else:
       mayor_codigo = 0
       for venta in ventas:
           if venta["Número de la venta"] > mayor_codigo:
               mayor_codigo = venta["Número de la venta"]
               desktops[i]["Número de la venta"] = mayor_codigo + 1
               
   desktops[i]["Venta total"] = desktops[i]["Precio de venta"]*cantidad
   with open("VentaRegistrada.txt", "a") as file:
       file.write(str(desktops[i]) + "\n")

def leer_impresoras():
    file = open("Impresoras.txt", "r")
    lines = file.readlines()
    resp = []
    for line in lines:
        impresora_str = line.strip()
        impresora = ast.literal_eval(impresora_str)
        resp.append(impresora)
    return resp

def venta_impresoras():
   impresoras = leer_impresoras() #impresoras es una lista de diccionarios con las impresoras ingresadas
   print("""
Tiene las siguientes opciones de venta:
    """)
   for impresora in impresoras:
        print(str(impresora["Código"]) + ", " + str(impresora["Descripción"]))
   print("")
   valor = True
   while valor:
       codigo = input("Ingrese el código de la impresora a registrar (escriba SALIR para volver): ")
       if codigo == "SALIR":
           return 0
       codigo = int(codigo)
       i = -1
       no_valor = 0
       for j in range(0, len(impresoras)):
           if impresoras[j]["Código"] == codigo:
               i = j
               valor = False
               break
           else:
               no_valor += 1
       if no_valor == len(impresoras):
           print("""
-------------------Por favor, ingrese un código válido-------------------------
""")      
   cantidad = int(input("Ingrese la cantidad de estas: "))
   impresoras[i]["Cantidad de la venta"] = cantidad
   
   ventas = leer_ventas() #lista de diccionarios con las ventas registradas
   if len(ventas) == 0:
       impresoras[i]["Número de la venta"] = 20000
   else:
       mayor_codigo = 0
       for venta in ventas:
           if venta["Número de la venta"] > mayor_codigo:
               mayor_codigo = venta["Número de la venta"]
               impresoras[i]["Número de la venta"] = mayor_codigo + 1
   
   impresoras[i]["Venta total"] = impresoras[i]["Precio de venta"]*cantidad
   with open("VentaRegistrada.txt", "a") as file:
       file.write(str(impresoras[i]) + "\n")

def leer_ventas():
    file = open("VentaRegistrada.txt", "r")
    lines = file.readlines()
    resp = []
    for line in lines:
        ventas_str = line.strip()
        ventas = ast.literal_eval(ventas_str)
        resp.append(ventas)
    return resp

def ordenar_ventas_quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores =[]
        mayores = []
        for i in range(1,len(lista)):
            if lista[i]["Número de la venta"] > pivot["Número de la venta"]:
                mayores.append(lista[i])
            else:
                menores.append(lista[i])
        mayores = ordenar_ventas_quicksort(mayores)
        menores = ordenar_ventas_quicksort(menores)
        return menores + [pivot] + mayores 
    
def modificar_venta(venta):
    print(""" 
        Elija el numero de venta que desee modificar:
          """)
    for unidad in venta:
        print(str(unidad["Número de la venta"]) + ', ' + str(unidad["Descripción"]))
    print("")
    valor = True
    while valor:
       numvent = input("Ingrese el numero de venta que desea modificar, escriba SALIR para volver: ")
       if numvent == "SALIR":
           return 0
       numvent = int(numvent)
       pos = -1
       izq = 0
       der = len(venta) - 1
       while izq <= der:
            medio = (izq + der) // 2
            if numvent == venta[medio]["Número de la venta"]:
                pos = medio
                valor = False
                break
            else:
                if numvent < venta[medio]["Número de la venta"]:
                    der = medio - 1
                else:
                    izq = medio + 1
       if pos == -1:
           print("""
-------------------Por favor, ingrese un numero de venta valida-------------------------
""")      
    nueva_cantidad = int(input("Ingrese la nueva cantidad de la venta: "))
    venta[pos]["Cantidad de la venta"] = nueva_cantidad
    venta[pos]["Venta total"] = nueva_cantidad*venta[pos]["Precio de venta"]
    archivo = open("VentaRegistrada.txt","w")
    for unidad in venta:
        archivo.write(str(unidad) + "\n")
    archivo.close
    return None

def ordenar_lista_precios():
    dic_ventas = leer_ventas()
    for i in range(len(dic_ventas)-1):
        for j in range(len(dic_ventas)-1-i):
            if dic_ventas[j]["Venta total"] > dic_ventas[j+1]["Venta total"]:
                aux = dic_ventas[j+1]
                dic_ventas[j+1] = dic_ventas[j]
                dic_ventas[j] = aux
    archivo = open("VentaRegistrada.txt","w")
    for unidad in dic_ventas:
        archivo.write(str(unidad) + "\n")
    archivo.close
    print("""          ----------------------------------------
          Se ha actualizado el orden de las ventas
          ----------------------------------------""")
    return None

def buscar_venta_num():
    dic_ventas = leer_ventas()
    print("")
    for ventas in dic_ventas:
        print(str(ventas["Descripción"]) + ", " + str(ventas["Número de la venta"]))
    print("")
    
    valor = True
    while valor:
       codigo = int(input("Ingrese el numero de venta a buscar (escriba SALIR para volver): "))
       if codigo == "SALIR":
           return 0
       i = -1
       no_valor = 0
       for j in range(0, len(dic_ventas)):
           if dic_ventas[j]["Número de la venta"] == codigo:
               i = j
               valor = False
               break
           else:
               no_valor += 1
       if no_valor == len(dic_ventas):
           print("""
----------------No se encontro la venta, ingrese un numero de venta valido--------------""")
    print(f"""
Los datos de la venta {codigo} son:
{dic_ventas[i]}""")
    return None

def mostrar_venta_alto():
    dic_ventas = leer_ventas()
    i = 0
    mayor = 0
    while i < len(dic_ventas):
        tmp = dic_ventas[i]["Venta total"]
        if tmp > mayor:
            mayor = tmp
        i+=1
    for x in dic_ventas:
        if x["Venta total"] == mayor:
            resp = x
    print(f"""
---------La venta con la venta total más alta es:----------
---------{resp}""")
    return None
