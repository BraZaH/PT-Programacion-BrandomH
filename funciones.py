# -------------------------------------------
# (LEER OPCIÓN)
# -------------------------------------------
def leer_opcion() -> int:
    try:
        op = int(input(">> "))

        if 1 > op > 6:
            input("[ERROR] Las opciones son entre 1 y 6 (incluyendolos)...")
            return -1

        return op
    except:
        input("[ERROR] Opción ingresada no es valida...")
        return -1
    

# -------------------------------------------
# (CUPOS GENERO)
# -------------------------------------------
def cupos_genero(genero: str, peliculas : dict, cartelera: dict) -> None:
    print("\tCupos por genero")
    contador = 0
    genero = genero.lower()
    for i in peliculas:
        if peliculas[i][1].lower() == genero:
            
            # Se encontró pelicula, ahora se debe buscar sus cupos
            for j in cartelera:
                if i == j:
                    contador += cartelera[j][1]
    
    input(f"Para el genero {genero.capitalize()} se ha encontardo un total de {contador} cupos.")


# -------------------------------------------
# (BUSCAR PRECIO)
# -------------------------------------------
def busqueda_precio(p_min : int, p_max :int, peliculas : dict, cartelera : dict) -> None:
    # ["titulo--codigo", ...]
    p = []

    for id_cartelera in cartelera:
        if p_min <= cartelera[id_cartelera][0] <= p_max and cartelera[id_cartelera][1] > 0:
            p.append(f"{peliculas[id_cartelera][0]} -- {id_cartelera}")

    p.sort()

    if len(p) == 0:
        input("No hay peliculsa en este rango de precios...")
    else:
        print("Las peliculas encontradas fueron: ")
        for i in p:
            print(i)
        input("...")


# -------------------------------------------
# (BUSCAR CODIGO)
# -------------------------------------------
def buscar_codigo(codigo: int, cartelera: dict) -> bool:
    for id in cartelera:
        if id == codigo:
            return True
    return False    


# -------------------------------------------
# (ACTUALIZAR PRECIO)
# -------------------------------------------
def actualizar_precio(codigo: int, nuevo_precio: int, cartelera: dict) -> bool:
    
    if buscar_codigo(codigo, cartelera) == False:
        return False
    
    for id in cartelera:
        if id == codigo:
            cartelera[id][0] = nuevo_precio
            return True
        
    
# -------------------------------------------
# (AGREGAR PELICULA VALIDADORES)
# -------------------------------------------

# (HELPERS)
def validar_espacios(texto: str) -> bool:
    texto = texto.strip()
    if texto == "":
        return False
    return True

def validar_entero_mayor0(numero: str) -> bool:
    if type(numero) != int: # Si no es entero
        return False
    if numero > 0: # Check duración
        return True
    
    return False

# -------------------------------------------
# (VALIDACIONES)
# -------------------------------------------

def validar_codigo(codigo: str, peliculas: dict, cartelera: dict) -> bool:
    if validar_espacios(codigo) == False:
        return False

    for i in peliculas:
        if i == codigo:
            return False
    for i in cartelera:
        if i == codigo:
            return False
        
    return True

def validar_titulo(titulo: str) -> bool:
    return validar_espacios(titulo)

def validar_genero(genero: str) -> bool:
    return validar_espacios(genero)

def validar_duracion(duracion: int) -> bool:
    return validar_entero_mayor0(duracion)
    
def validar_clasificacion(clasificacion: str) -> bool:
    if len(clasificacion) != 1:
        return False
    
    clasificaciones = ["A","B","C"]

    if clasificacion not in clasificaciones:
        print("Cago segunda ver")
        return False
    
    return True # En caso que no se cumpla nada

def validar_idioma(idioma: str) -> bool:
    return validar_espacios(idioma)

def validar_3d(es_3d: str) -> bool:
    es_3d = es_3d.lower()
    if es_3d == "s" or es_3d == "n":
        return True
    return False # En caso que no se cumpla 

def validar_precio(precio: int) -> bool:
    return validar_entero_mayor0(precio)

def validar_cupos(cupos: int) -> bool:
    if type(cupos) != int:
        return False
    
    if cupos >= 0:
        return True
    
    return False

# -------------------------------------------
# (AGREGAR PELICULA)

def agregar_pelicula(codigo: str, titulo: str, genero: str, duracion: int, clasificacion: str, idioma: str, es_3d: str, precio: int, cupos: int, cartelera: dict, peliculas: dict) -> bool:
    # Check de codigos

    for id in cartelera:
        if id == codigo:
            return False

    for id in peliculas:
        if id == codigo:
            return False

    # Agregar pelicula

    peliculas[id] = [
        titulo, genero, duracion, clasificacion, idioma, es_3d
    ] 

    cartelera[id] = [
        precio, cupos
    ]

    return True

# -------------------------------------------
# (ELIMINAR PELICULA)
# -------------------------------------------

def eliminar_pelicula(codigo: str, peliculas: dict, cartelera: dict) -> bool:
    if buscar_codigo(codigo, cartelera) == False:
        return False
    
    codigo_nuevo = ""

    for i in peliculas:
        if i.lower() == codigo.lower():
            codigo_nuevo = i
    

    cartelera.pop(codigo_nuevo)  
    peliculas.pop(codigo_nuevo)

    return True

