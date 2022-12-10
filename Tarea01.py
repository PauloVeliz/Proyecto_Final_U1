import os
import csv
from time import sleep
from random import randint
from colorama import Fore,init

# Inicializa colorama
init()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Define la clase Libro con sus atributos
class Libro:
    def __init__(self,id:str,titulo:str,genero:str,ISBN:str,editorial:str,autor:str):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autor = autor

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Función valida que el número ingresado sea entero
def valida_int(texto_input:str) -> int:
    while True:
        print(Fore.CYAN + texto_input + Fore.RESET,end='')
        numero = input().strip()
        if numero.isdigit():
            return int(numero)
        print(Fore.RED + 'El valor ingresado no es un número.' + Fore.RESET)
        sleep(1)
        os.system(so)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Función valida que el valor ingresado no sea vacío
def valida_vacios(texto_input:str) -> str:
    while True:
        print(Fore.CYAN + texto_input + Fore.RESET,end='')
        texto = input().strip()
        if texto != '':
            return texto
        print(Fore.RED + 'El valor ingresado no debe ser vacío.' + Fore.RESET)
        sleep(1)
        os.system(so)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Función decoradora mostrar_libros
def mostrar_libros(funcion):
    def funcion_auxiliar(data_libros:list[object]) -> None:
        lista = funcion(data_libros)
        if lista != []:
            print (Fore.CYAN + '{:<3} {:<27} {:<17} {:<15} {:<12} {:<25}'.format( 'ID','Titulo','Genero','ISBN','Editorial','Autor(es)') + Fore.RESET)        
            for libro in lista:
                print (Fore.GREEN + '{:<3} {:<27} {:<17} {:<15} {:<12} {:<25}'.format( libro.id,libro.titulo,libro.genero,libro.ISBN,libro.editorial,libro.autor) + Fore.RESET)
    return funcion_auxiliar

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Lee los libros de un archivo libros.csv y los guarda en data_libros
def leer_libros() -> list[object]:
    file_csv = 'libros.csv'
    with open (file_csv,encoding='utf-8') as f_libros:
        doc_libros = csv.DictReader(f_libros)
        data_libros = [Libro(libro['ID'],libro['Titulo'],libro['Genero'],libro['ISBN'],libro['Editorial'],libro['Autor(es)']) for libro in doc_libros]
    return data_libros

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# OPCIÓN 1: Carga 3 libros y muestra según la función decoradora mostrar_libros
@mostrar_libros
def carga_3libros(data_libros:list[object]) -> list[object]:
    n_libros = len(data_libros)
    ind_libros_mostrar = set([])
    
    while len(ind_libros_mostrar) < 3:
        random = randint(0,n_libros-1)
        ind_libros_mostrar.add(random)
    
    carga_libros = [data_libros[ind] for ind in ind_libros_mostrar]
    return carga_libros

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# OPCIÓN 2: Lista los libros de acuerdo y muestra según la función decoradora mostrar_libros
@mostrar_libros
def listar_libros(data_libros:list[object]) -> list[object]:
    libros_listar = data_libros[:]
    return libros_listar

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# OPCIÓN 3: Agrega un libro.
@mostrar_libros
def agregar_libro(data_libros:list[object]) -> list[object]:
    libro = {'ID':'','Titulo':'','Genero':'','ISBN':'','Editorial':'','Autor(es)':''}
    for key in libro:
        texto_input = f'Ingrese el {key} del libro: '
        if key == 'ID':
            valor = str(valida_int(texto_input))
        else:
            if key ==  'Autor(es)':
                texto_nautor = 'Ingrese número de Autor(es): '
                n_autores = valida_int(texto_nautor)
                if n_autores == 1:
                    valor = valida_vacios(texto_input).lower().title()
                else:
                    autores = []
                    for i in range(n_autores):
                        cada_autor = f'Ingrese el Autor {i+1}: '
                        valor_cada_autor = valida_vacios(cada_autor)
                        autores.append(valor_cada_autor)
                    valor = ' & '.join(autores).lower().title()
            else:
                valor = valida_vacios(texto_input).lower().title()

        libro[key] = valor
    libro_agregar = Libro(libro['ID'],libro['Titulo'],libro['Genero'],libro['ISBN'],libro['Editorial'],libro['Autor(es)'])
    data_libros.append(libro_agregar)
    print(Fore.YELLOW + '------------------------------------------------------------' + Fore.RESET)
    print (Fore.GREEN + '!Se guardó el libro exitosamente!' + Fore.RESET)
    sleep(1.5)
    os.system(so)
    return data_libros

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# OPCIÓN 4: Eliminar libro por ID.
@mostrar_libros
def eliminar_libro(data_libros:list[object]) -> list[object]:
    texto_input = 'Ingrese el ID del libro a eliminar: '
    id_libro = valida_int(texto_input)

    for libro in data_libros:
        if int(libro.id) == id_libro:
            pos = data_libros.index(libro)
            del data_libros[pos]
            print(Fore.YELLOW + '------------------------------------------------------------' + Fore.RESET)
            print(Fore.GREEN + '¡Libro eliminado exitosamente!' + Fore.RESET)
            sleep(1.5)
            os.system(so)
            return data_libros
    print(Fore.YELLOW + '------------------------------------------------------------' + Fore.RESET)
    print(Fore.RED + 'El libro que desea eliminar no existe.' + Fore.RESET)
    sleep(1.5)
    os.system(so)
    return data_libros

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# OPCIÓN 5: Buscar libro por ISBN o por título.
@mostrar_libros
def buscar_libro(data_libros:list[object]) -> list:
    while True:
        texto_input = 'Desea buscar por Título (1) o ISBN (2): '
        opc_buscar = valida_int(texto_input)
        if opc_buscar in [1,2]:
            break
    os.system(so)
    if opc_buscar == 1:
        texto_input = 'Ingrese Título del libro: '
        libro_buscar = valida_vacios(texto_input).lower()
        for libro in data_libros:
            if libro.titulo.lower() == libro_buscar:
                return [libro]
    else:
        texto_input = 'Ingrese ISBN del libro: '
        libro_buscar = valida_vacios(texto_input).lower()
        for libro in data_libros:
            if libro.ISBN.lower() == libro_buscar:
                return [libro]
    print(Fore.YELLOW + '------------------------------------------------------------' + Fore.RESET)
    print(Fore.RED + 'El libro buscado no existe.' + Fore.RESET)
    sleep(1.5)
    os.system(so)
    return []

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# OPCIÓN 6: Ordenar libros por Títulos.
@mostrar_libros
def ordenar_libro(data_libros:list[object]) -> list[object]:
    Titulos_libros = [libro.titulo for libro in data_libros]
    Titulos_Ordenados = sorted(Titulos_libros)
    data_libros_orden = []

    for ind in range(len(data_libros)):
        pos = Titulos_libros.index(Titulos_Ordenados[ind])
        data_libros_orden.append(data_libros[pos])
    return data_libros_orden

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# OPCIÓN 7: Buscar libros por autor, editorial o género. Sugerir opciones y listar resultados.
@mostrar_libros
def buscar_libro_op7(data_libros:list[object]) -> list:
    while True:
        texto_input = 'Desea buscar por Autor(es) (1), Editorial (2) o Género (3): '
        opc_buscar = valida_int(texto_input)
        if opc_buscar in [1,2,3]:
            break
    os.system(so)
    sugerir_libros = []
    if opc_buscar == 1:
        texto_nautor = 'Ingrese número de Autor(es): '
        n_autores = valida_int(texto_nautor)
        if n_autores == 1:
            texto_input = 'Ingrese el Autor del libro: '
            autor = valida_vacios(texto_input).lower()
        else:
            autores = []
            for i in range(n_autores):
                cada_autor = f'Ingrese el Autor {i+1}: '
                valor_cada_autor = valida_vacios(cada_autor)
                autores.append(valor_cada_autor)
            autor = ' & '.join(autores).lower()

        for libro in data_libros:
            if libro.autor.lower() == autor:
                sugerir_libros.append(libro)
    elif opc_buscar == 2:
        texto_input = 'Ingrese Editorial del libro: '
        edito = valida_vacios(texto_input).lower()
        for libro in data_libros:
            if libro.editorial.lower() == edito:
                sugerir_libros.append(libro)
    else:
        texto_input = 'Ingrese Género del libro: '
        genero = valida_vacios(texto_input).lower()
        for libro in data_libros:
            if libro.genero.lower() == genero:
                sugerir_libros.append(libro)
    if sugerir_libros == []:
        print(Fore.YELLOW + '------------------------------------------------------------' + Fore.RESET)
        print(Fore.RED + 'El libro buscado no existe.' + Fore.RESET)
    sleep(1.5)
    os.system(so)
    return sugerir_libros

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# OPCIÓN 8: Buscar libro por número de autores. Ingresar número, por ejemplo 2(hace referencia a dos autores)
# y se deben listar todos los libros que contengan 2 autores.
@mostrar_libros
def buscar_libro_autores(data_libros:list[object]) -> list:
    texto_nautor = 'Ingrese número de Autor(es): '
    n_autores = valida_int(texto_nautor)
    data_libros_autores = []
    for libro in data_libros:
        if len(libro.autor.split(" & ")) == n_autores:
            data_libros_autores.append(libro)

    if  data_libros_autores == []:
        print(Fore.YELLOW + '------------------------------------------------------------' + Fore.RESET)
        print (Fore.RED + f'No hay libros con {n_autores} autores.' + Fore.RESET)
    sleep(1.5)
    os.system(so)
    return data_libros_autores

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# OPCIÓN 9: Editar o actualizar datos de un libro (título,género,ISBN,editorial y autores).
@mostrar_libros
def editar_libro(data_libros:list[object]) -> list[object]:
    texto_input = 'Ingrese el ID del libro a editar: '
    id_libro = valida_int(texto_input)
    os.system(so)
    pos = ''
    for libro in data_libros:
        if int(libro.id) == id_libro:
            pos = data_libros.index(libro)
            texto_input = 'Ingrese nuevo Título de libro: '
            data_libros[pos].titulo = valida_vacios(texto_input).lower().title()
            texto_input = 'Ingrese nuevo Género de libro: '
            data_libros[pos].genero = valida_vacios(texto_input).lower().title()
            texto_input = 'Ingrese nuevo ISBN de libro: '
            data_libros[pos].ISBN = valida_vacios(texto_input).lower().upper()
            texto_input = 'Ingrese nueva editorial de libro: '
            data_libros[pos].editorial = valida_vacios(texto_input).lower().title()

            texto_nautor = 'Ingrese número de Autor(es): '
            n_autores = valida_int(texto_nautor)
            if n_autores == 1:
                texto_input = 'Ingrese nuevo Autor del libro: '
                autor = valida_vacios(texto_input)
            else:
                autores = []
                for i in range(n_autores):
                    cada_autor = f'Ingrese el Autor {i+1}: '
                    valor_cada_autor = valida_vacios(cada_autor)
                    autores.append(valor_cada_autor)
                autor = ' & '.join(autores).lower().title()

            data_libros[pos].autor = autor
            break      
    print(Fore.YELLOW + '------------------------------------------------------------' + Fore.RESET)
    if pos != '':
        print (Fore.GREEN + f'Libro editado exitosamente.' + Fore.RESET)
    else:
        print (Fore.RED + f'No existe el libro con ID: {id_libro}.' + Fore.RESET)
    sleep(1.5)       
    os.system(so)
    return data_libros


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Lista las Opciones que se pueden realizar en el sistema.
def listar_opciones():
    Opciones = {1:'Leer archivo de disco duro.',
                2:'Listar libros.',
                3:'Agregar libro.',
                4:'Eliminar libro.',
                5:'Buscar libro por Título o ISBN.',
                6:'Ordenar libros por Títulos.',
                7:'Buscar libros por Autor(es), Editorial o Género.',
                8:'Buscar libro por número de Autor(es).',
                9:'Editar datos de un libro.',
                10:'Guardar libros en archivo de disco duro (.txt o csv).'
                }
    print(Fore.YELLOW + '------------------------------------------------------------' + Fore.RESET)
    
    for key in Opciones:
        print(Fore.GREEN + f'{key}: {Opciones[key]}' + Fore.RESET)

    print(Fore.YELLOW + '------------------------------------------------------------' + Fore.RESET)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
accion = ''
inicio = True
while inicio == True:

    # Declara variable so para poder limpiar pantalla
    if os.name == 'posix':
        so = 'clear'
    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        so = 'cls'

    os.system(so)

    if accion == '':
        print(Fore.GREEN + 'BIENVENIDO AL SISTEMA DE REGISTRO DE LIBROS' + Fore.RESET)
        texto_input = 'Ingresa tu nombre: '
        nombre = valida_vacios(texto_input).lower().title()
        os.system(so)
    else:
        print(Fore.GREEN +  f'¡BIENVENIDO NUEVAMENTE!' + Fore.RESET)

    print(Fore.GREEN + f'Es gratificante que te interesen los libros, {nombre}!')
    sleep(0.5)
    print('A continuación te muestro las opciones que puedes realizar.' + Fore.RESET)
    sleep(1.5)
    listar_opciones()

    while True:
        texto_input = f'{nombre}, elige la opción que deseas realizar: '
        opcion = valida_int(texto_input)
        os.system(so)
        sleep(0.5)
        listar_opciones()
        if opcion in range(1,11):
            break

    os.system(so)

    # Carga Data de Libros
    data_libros = leer_libros()

    # OPCIÓN 1: Leer archivo de disco duro.
    if opcion == 1:
        carga_3libros(data_libros)

    # OPCIÓN 2: Listar libros.
    elif opcion == 2:
        listar_libros(data_libros)

    # OPCIÓN 3: Agrega un libro.
    elif opcion == 3:
        agregar_libro(data_libros)

    # OPCIÓN 4: Eliminar libro.
    elif opcion == 4:
        listar_libros(data_libros)
        eliminar_libro(data_libros)

    # OPCIÓN 5: Buscar libro por ISBN o por título.
    elif opcion == 5:
        buscar_libro(data_libros)

    # OPCIÓN 6: Ordenar libros por Títulos.
    elif opcion == 6:
        pass
    
    # OPCIÓN 7: Buscar libros por autor, editorial o género.
    elif opcion == 7:
        pass

    # OPCIÓN 8: Buscar libro por número de autores.
    elif opcion == 8:
        pass

    # OPCIÓN 9: Editar datos de un libro.
    elif opcion == 9:
        pass

    # OPCIÓN 10: Guardar libros en disco duro.
    else:
        pass
    

    print(Fore.YELLOW + '------------------------------------------------------------' + Fore.RESET)
    texto_input = f'¿{nombre}, deseas continuar? (Sí/No): '
    accion = valida_vacios(texto_input).lower()
    
    os.system(so)

    if accion == 'no':
        inicio = False
    else:
        inicio = True

