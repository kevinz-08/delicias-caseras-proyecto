from logic.products import findAll
from tabulate import tabulate

def lobby():
    print(""""
          
        ██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░
        ██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗
        ██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║
        ██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║
        ██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝
        ╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░
          
                        1. Entrar como Cliente 
                        2. Entrar como Admin
                        0. Salir del Programa
          
          
          """)
    opc = int(input('---)'))
    return opc



def design():
    print("""
    █████████████████████████████████████████████████████████████████████████████████████████
    █▄─▄▄▀█▄─▄▄─█▄─▄███▄─▄█─▄▄▄─█▄─▄██▀▄─██─▄▄▄▄███─▄▄▄─██▀▄─██─▄▄▄▄█▄─▄▄─█▄─▄▄▀██▀▄─██─▄▄▄▄█
    ██─██─██─▄█▀██─██▀██─██─███▀██─███─▀─██▄▄▄▄─███─███▀██─▀─██▄▄▄▄─██─▄█▀██─▄─▄██─▀─██▄▄▄▄─█
    ▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀                                        
                                                                   
                        1. Ver productos                                        
                        2. Ver productos por categoria                          
                        3. Actualizar el inventario de un producto              
                        4. Crear nuevo producto                                 
                        0. Salir                                                        
    """)
    opc = int(input('---)'))
    return opc

def menu_cliente():
    print("""
                                    
    █████████████████████████████████████████████████████████████████████████████████████████
    █▄─▄▄▀█▄─▄▄─█▄─▄███▄─▄█─▄▄▄─█▄─▄██▀▄─██─▄▄▄▄███─▄▄▄─██▀▄─██─▄▄▄▄█▄─▄▄─█▄─▄▄▀██▀▄─██─▄▄▄▄█
    ██─██─██─▄█▀██─██▀██─██─███▀██─███─▀─██▄▄▄▄─███─███▀██─▀─██▄▄▄▄─██─▄█▀██─▄─▄██─▀─██▄▄▄▄─█
    ▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀                                       
                            
                                                                                            
                                    1. Ver productos                                        
                                    2. Ver productos por categoria
                                    3. Comprar un producto                                    
                                    0. Salir                                                 
""")
    opc = int(input('---)'))
    return opc

def tableProducts():
    data = findAll()
    datamodify = []
    for diccionario in data:
        diccionario.pop("descripcion")
        diccionario.pop("proveedor")
        diccionario.pop("precio_proveedor")
        datamodify.append(diccionario)
    print(tabulate(datamodify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))

def tableProductsByCategory(category):
    data = findAll()
    datamodify = []
    category_found = False 
    for diccionario in data:
        if diccionario.get("categoria") == category:
            category_found = True  # Si encontramos productos con la categoría, cambiamos la variable a True
            diccionario.pop("descripcion")
            diccionario.pop("proveedor")
            diccionario.pop("precio_proveedor")
            datamodify.append(diccionario)
    
    if category_found:  # Si encontramos productos con la categoría, mostramos la tabla
        print(tabulate(datamodify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    else:  # Si no se encontró ninguna categoría, mostramos el mensaje de error
        print("Categoría no encontrada")
        input("Presione enter para ver las categorías disponibles")
        print("CATEGORIAS")
        print(" ")
        for diccionario in data:
            print(diccionario.get("categoria"))
        print(" ")