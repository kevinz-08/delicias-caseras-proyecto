from logic.products import *
def createProduct():
    data = findAll()
    codigoProducto = input('Escribe el codigo del producto: ')
    name = input('Escribe el nombre del producto : ')
    catergoria = input('Escribe la categoria del producto: ')
    descripcion = input('Escribe una descripcion para tu producto: ')
    proveedor = input('Escribe el proveedor de tu producto: ')
    cantidadEnStock = int(input('Escribe la cantidad de tu stock: '))
    precioDeVenta = int(input('Escribe el precio de tu producto: '))
    precioDeProveedor = int(input('Escribe el precio que te da tu proveedor: '))
    
    gh = {
        "codigo_producto": codigoProducto,
        "nombre": name,
        "categoria": catergoria,
        "descripcion": descripcion,
        "proveedor": proveedor,
        "cantidad_en_stock": cantidadEnStock,
        "precio_venta": precioDeVenta,
        "precio_proveedor": precioDeProveedor
    }
    data.append(gh)
    saveAll(data)