from design.products import *
from logic.products import updateInventoryByCode
from logic.newProduct import *
from design.order import *
import os

if __name__=='__main__':
        
    isActive = True

    while isActive:
            try:
                match lobby():
                    case 0:
                        print("Has salido del programa.")
                        isActive = False  
                    case 1:
                        isActive = True
                        while isActive:
                            try:
                                match menu_cliente():
                                    case 0:
                                        print("Has salido del programa.")
                                        isActive = False 
                                    case 1:
                                        tableProducts()
                                        input("Presiona enter para continuar...")
                                    case 2:
                                        tableProductsByCategory(input("Ingrese la categoría (panes, pastel, postres): "))
                                        input("Regresaras al menú principal...")
                                    case 3:
                                        cliente()
                                        input("Regresaras al menu principal")
                                    
                                    case _:    
                                        print("Esa opción no existe")
                            except Exception as e:
                                print(f"Error: {e}. Selecciona una opción correcta.")
                                input("Presiona Enter para continuar...")
                    case 2:
                        designActive = True  
                        while designActive:
                            try:
                                match design():
                                    case 0:
                                        print("Has salido del programa.")
                                        designActive = False  
                                    case 1:
                                        tableProducts()
                                        input("Presiona Enter para continuar...")
                                    case 2:
                                        tableProductsByCategory(input("Ingrese la categoría (panes, pastel, postres): "))
                                        input("Regresaras al menú principal...")
                                    case 3:
                                        updateInventoryByCode(input("Ingrese el código de producto ejemplo (PNN_001): "))
                                        input("Presiona Enter para regresar al menú principal...")
                                    case 4:
                                        createProduct()
                                        input("Presiona Enter para continuar...")
                                    case _:    
                                        print("Esa opción no existe")
                            except Exception as e:
                                print(f"Error: {e}. Selecciona una opción correcta.")
                                input("Presiona Enter para continuar...")
                    case _:    
                        print("Esa opción no existe")
            except Exception as e:        
                print(f"Error: {e}. Selecciona una opción correcta.")
                input("Presiona Enter para continuar...")

