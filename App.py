from funciones import venta_laptops, venta_desktops, venta_impresoras, modificar_venta, ordenar_lista_precios, buscar_venta_num, mostrar_venta_alto,ordenar_ventas_quicksort,leer_ventas,ingresar_laptop
from funciones import ingresar_desktop, ingresar_impresora
import sys

def registrar_venta():
    while True:
        print("""
-------------------------------------------------------------------------------""")
        print("""
Opciones de Venta:
              1) Laptop
              2) Desktop
              3) Impresora
              0) Regresar
              """)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            a = venta_laptops()
            if a == 0:
                registrar_venta()
        elif opcion == 2:
            a = venta_desktops()
            if a == 0:
                registrar_venta()
        elif opcion == 3:
            a = venta_impresoras()
            if a == 0:
                registrar_venta()
        elif opcion == 0:
            break
    main()
    
def main():
    valid = True
    while valid:
        print("""
-------------------------------------------------------------------------------""")
        print("""
              1) Ingresar laptops
              2) Ingresar Desktops
              3) Ingresar impresoras
              4) Registrar venta
              5) Modificar la cantidad de una venta
              6) Ordenar ventas por precio
              7) Buscar venta por número de venta
              8) Mostrar venta con total más alto
              0) Salir
              """)
        x = int(input("Ingrese el número de la opción a realizar: "))
        if 0 <= x <= 8:
            if x == 0:
                sys.exit()
            elif x == 1:
                a = ingresar_laptop()
                if a == 0:
                    main()
            elif x == 2:
                a = ingresar_desktop()
                if a == 0:
                    main()
            elif x == 3:
                a = ingresar_impresora()
                if a == 0:
                    main()
            elif x == 4:
                registrar_venta()
            elif x == 5:
                a = leer_ventas()
                b = ordenar_ventas_quicksort(a)
                modificar_venta(b)
            elif x == 6:
                ordenar_lista_precios()
            elif x == 7:
                buscar_venta_num()
            elif x == 8:
                mostrar_venta_alto()
        else:
            print("""
              Por favor, ingrese un número valido.""")

main()