nombreVendedor=None
productos=[]
producto={}

opcion=100

print("Mercado")
print("****************")
print("1.Crear lista mercado")
print("2. Ver lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("5. Salir")
while opcion != 5:
    opcion=int(input("Digita una opción: "))
    if opcion == 1:
        print("Bienvenido a la creación de tu mercado")
        
        #Creando claves y valores de un diccionario
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["precio"]=int(input("Digita el precio del producto: "))
        producto["cantidad"]=int(input("Cuantos elementos de este producto vas a llevar: "))
        producto["presentacion"]=input("Cual presentación llevaras?: ")

        #Mostrando mi diccionario
        #print(producto)

        #Poblando una lista(Agregando elementos a una lista)
        productos.append(producto)
        print(productos)

    elif opcion == 2:
        print("Estoy en la 2")
    elif opcion == 3:
        print("Estoy en la 3")
    elif opcion == 4:
        print("Estoy en la 4")
    else:
        print("Opción no valida")