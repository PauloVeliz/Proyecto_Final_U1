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
        pass

    # OPCIÓN 5: Buscar libro por ISBN o por título.
    elif opcion == 5:
        pass

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