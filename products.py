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

def crear_detalle_pedido(codigo_producto, cantidad, precio_unitario, numero_linea):
     return{
            "codigo_producto" : codigo_producto,
            "cantidad" : cantidad,
            "precio_unitario" : precio_unitario,
            "numero_linea" : numero_linea
     }

def crear_pedido(codigo_pedido, codigo_cliente, fecha_pedido, detalles_pedido):
     return{
         "codigo_pedido": codigo_pedido,
         "codigo_cliente": codigo_cliente,
         "fecha_pedido": fecha_pedido,
         "detalles_pedido": detalles_pedido
         
     }

def guardar_en_json(nombre_archivo, datos):

    try:
        with open("data/pedidos.json", "r") as archivo:
            contenido_existente = json.load(archivo)
        if not isinstance(contenido_existente, list):
            contenido_existente = []
    except (FileNotFoundError, json.JSONDecodeError):
        contenido_existente = []

def cliente():
    try:
        with open("pedido.json", "r") as archivo:
            pedidos_existentes = json.load(archivo)
        if isinstance(pedidos_existentes, list) and pedidos_existentes:
            ultimo_codigo_pedido = int(pedidos_existentes[-1]["codigo_pedido"])
            ultima_linea = pedidos_existentes[-1]["detalles_pedido"]["numero_linea"]
        else:
            ultimo_codigo_pedido = 0
            ultima_linea = 0
    except (FileNotFoundError, json.JSONDecodeError):
        pedidos_existentes = []
        ultimo_codigo_pedido = 0
        ultima_linea = 0
    
    nuevo_codigo_pedido = ultimo_codigo_pedido +1 
    nuevo_codigo_cliente = f"Cl-{nuevo_codigo_pedido:03d}"
    nueva_fecha_pedido = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Ingrese los detalles del pedido")
    codigo_producto = input("Código del producto: ")
    cantidad = int(input("Cantidad: "))
    precio_unitario = float(input("Precio unitario: "))
    nueva_linea = ultima_linea + 1

    detalles_pedido = crear_detalle_pedido(codigo_producto, cantidad, precio_unitario, nueva_linea)

    nuevo_pedido = crear_pedido(
        codigo_pedido=str(nuevo_codigo_pedido),
        codigo_cliente=nuevo_codigo_cliente,
        fecha_pedido=nueva_fecha_pedido,
        detalles_pedido=detalles_pedido
    )

    pedidos_existentes.append(nuevo_pedido)

    with open("pedido.json", "w") as archivo:
        json.dump(pedidos_existentes, archivo, indent=4)

    print(f"Pedido {nuevo_codigo_pedido} guardado exitosamente en 'pedido.json'.")