import os
from tabulate import tabulate
import requests

def iniciar():
    os.system('cls')
    while True:
        print('Selecione una opcion')
        print('\t1. Registrar movimiento')
        print('\t2. Ver todos los  movimiento')
        print('\t3. Buscar un movimiento')
        print('\t4. Modificar un  movimiento')
        print('\t5. Eliminar un movimiento')
        print('\t6. Salir del programa')
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            nuevo_movimiento()
        if opcion == '2':
            mostrar_movimientos()  
        if opcion == '3':
            buscar_movimiento()
        if opcion =='4':
            modificar_movimiento()    
        if opcion == '5':
            eliminar_movimiento()          
        elif opcion == '6':
            break
        else: 
            print('Escoja una opcion correcta')  

def nuevo_movimiento():
    tipo = input('Ingrese el tipo de movimiento \n-Ingreso\n-Gasto\n')
    cantidad = input('Ingrese la cantidad: ')
    fecha = input('Ingrese la fecha: ')
    data ={'tipo': tipo, 'cantidad': cantidad, 'fecha': fecha}
    respuesta = requests.post(url='http://localhost:3000/movimientos/registrar', data=data)
    print(respuesta.text)

def mostrar_movimientos():
    response = requests.get(url='http://localhost:3000/movimientos/todos')
    datos = []
    for dato in response.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)    
    header = ['ID', 'TIPO DE MOVIMIENTO', 'CANTIDAD', 'FECHA']
    tabla = tabulate(datos, header, tablefmt='fancy_grid')
    print(tabla)


def buscar_movimiento():
    id = input('Ingrese el id del movimiento a buscar: ')
    response = requests.get(url=f'http://localhost:3000/movimientos/buscar/{id}')
    if response.status_code == 200:
        try:
            datos = response.json()
            if datos:
                # Asegúrate de que datos es una lista de diccionarios
                if isinstance(datos, list):
                    datos = [list(dato.values()) for dato in datos]
                else:
                    datos = [list(datos.values())]
                header = ['ID', 'TIPO DE MOVIMIENTO', 'CANTIDAD', 'FECHA']
                tabla = tabulate(datos, header, tablefmt='fancy_grid')
                print(tabla)
            else:
                print('Movimiento no encontrado')
        except requests.exceptions.JSONDecodeError:
            print('Error decodificando la respuesta JSON')
    else:
        print('Error al buscar el movimiento:', response.text)


def modificar_movimiento():
    id = input('Ingrese el id que desea modificar: ')
    campo = input('Ingrese el campo a modificar\n1. Tipo\n2. Cantidad\n3. Fecha\n')
    nuevo_valor = ''
    if campo == '1':
        campo = 'tipo'
        nuevo_valor = input('Ingrese el tipo de movimiento: ')
    elif campo == '2':
        campo = 'cantidad' 
        nuevo_valor = input('Ingrese nueva cantidad:')   
    elif campo == '3':
        campo = 'fecha' 
        nuevo_valor = input('Ingrese nueva fecha: ')
    
    data = {'campo': campo, 'nuevo_valor': nuevo_valor} 
    respuesta = requests.post(url=f'http://localhost:3000/movimientos/modificar/{id}', data=data)
    print(respuesta.text)  
  
def eliminar_movimiento():
    id = input('Ingrese el id del movimiento a eliminar: ')
    respuesta = requests.post(url='http://localhost:3000/movimientos/eliminar/'+id)
    print(respuesta.text)

iniciar()                   