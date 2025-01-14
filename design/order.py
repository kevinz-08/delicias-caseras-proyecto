import json
from datetime import datetime

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