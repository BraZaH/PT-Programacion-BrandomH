"""
@Brandom Hormazábal

Sistema de peliculas y cartelera de CineMax

Prueba Transversal 005_D

"""

from os import system as sys
from funciones import *

""" Estructura
    "id" : ["titulo", "genero", "duracion_min", "clasificacion", "idioma", "es_3d"],
"""
peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español',
    False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles',
    False],
}
""" Estructura
    "id" : ["precio", "cupos"],
"""
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

while True:
    sys("cls")
    print("""
========== MENÚ PRINCIPAL ==========
1. Cupos por género
2. Búsqueda de películas por rango de precio
3. Actualizar precio de película
4. Agregar película
5. Eliminar película
6. Salir
=====================================
          """)
    
    op = leer_opcion()

    match op:
        case 1:
            sys("cls")
            genero = input("Ingrese el género a buscar: ")
            cupos_genero(genero, peliculas, cartelera)
        case 2:
            while True:
                try:
                    sys("cls")
                    print("\tBusqueda de peliculas por rango de precio")
                    p_min = int(input("Precio Minimo: "))
                    p_max = int(input("Precio Maximo: "))

                    if p_min > p_max or p_min < 0 or p_max < 0:
                        input("El precio minimo no puede ser mayor que el precio maximo y ambos deben ser mayor o igual que 0.")
                        continue

                    busqueda_precio(p_min, p_max, peliculas, cartelera)
                    break
                except:
                    input("Debe ingresar valores enteros...")
        case 3:
            while True:
                sys("cls")
                print("\t Actualizar precio de pelicula")
                codigo = input("Ingrese codigo: ")
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if actualizar_precio(codigo, nuevo_precio, cartelera):
                    print("Precio actualizado...")
                else:
                    print("El codigo no existe...")

                op = input("¿Desea actualizar otro precio? (s/n)").lower()
                if op == "s":
                    continue
                else:
                    break
        case 4:
            try:

                sys("cls")
                print("\tAgregar pelicula")

                codigo = input("Ingrese codigo: ")
                if validar_codigo(codigo, peliculas, cartelera) == False:
                    input("El codigo ingresado no es valido...")
                    continue
                
                titulo = input("Ingresar titulo: ")
                if validar_titulo(titulo) == False:
                    input("Titulo ingresado no es valido...")
                    continue

                genero = input("Ingresar genero: ")
                if validar_genero(genero) == False:
                    input("Genero ingresado no es valido...")
                    continue
                
                duracion = int(input("Ingresar duración (mins): "))
                if validar_duracion(duracion) == False:
                    input("Duración ingresada no es valida...")
                    continue

                clasificacion = input("Ingresar clasificación: ")
                if validar_clasificacion(clasificacion) == False:
                    input("Clasificación ingresada no es valida...")
                    continue

                idioma = input("Ingresar idioma: ")
                if validar_idioma(idioma) == False:
                    input("Idioma ingresadon no es valido...")
                    continue

                es_3d = input("Ingresar si es 3d (s/n): ")
                if validar_3d(es_3d) == False:
                    input("Formato no valido... ")
                    continue

                precio = int(input("Ingresar el precio: "))
                if validar_precio(precio) == False:
                    input("El precio no es valido...")
                    continue

                cupos = int(input("Ingresar cupos: "))
                if validar_cupos(cupos) == False:
                    input("Cupos ingresados no es valido...")
                    continue

                if agregar_pelicula(codigo,titulo,genero,duracion,clasificacion,idioma,es_3d,precio,cupos, cartelera, peliculas) == True:
                    input("Pelicula agregada...")
                else:
                    input("El codigo ya existe...")
                    continue
            except:
                input("Hubo un error en la validación de un dato, por favor revise correctamente...")

        case 5:
            sys("cls")
            print("\tEliminar Pelicula")
            codigo = input("Ingrese codigo: ")

            if eliminar_pelicula(codigo, peliculas, cartelera) == True:
                input("Pelicula eliminada...")
            else:
                input("El codigo no existe...")
        case 6:
            exit()