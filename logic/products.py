from formula.products import updateQuantityInventory
from tabulate import tabulate
import json
from datetime import datetime

def findAll():
    with open ("data/products.json", "r", encoding="utf-8" ) as file:
        data = file.read()
        convertListOrDict= json.loads(data)
        return convertListOrDict
    
def saveAll(data):
    with open ("data/products.json", "w") as file:
        convertJSON = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJSON)
        return "se modifico el archivo products.json"


#actualizar inventario

def updateInventoryByCode(code_product):
    data = findAll()
    category_found = False
    for product in data:
        if (product.get("codigo_producto") == code_product):
            category_found = True
            quantity = int(input("Ingrese la cantidad de productos  que desea actualizar: "))
            stock = updateQuantityInventory(product.get("cantidad_en_stock"), quantity)
            product.update({"cantidad_en_stock": stock})
            print(f"Se actualizo el stock de {code_product} a {stock}")
            input("Presione enter para continuar... ")
    if category_found:
        print(tabulate(data, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    else:
                print("Codigo no encontrado")  
                input("Presione enter para ver los codigos")
                print("CODIGOS DISPONIBLES")
                print(" ")
                for product in data: 
                 print(product.get("codigo_producto"))
                print(" ")

