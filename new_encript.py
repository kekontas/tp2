def file_check(file2encript):
    """
    escribo doc
    """
    while True:  # reviso si existe el path. si no existe, sigue preguntando hasta que exista.
        try:
            with open(file2encript, 'r'):
                break
        except FileNotFoundError:  # atajo errores si el archivo no puede ser encontrado
            print('No existe el archivo.')
            file2encript = input('Ingrese el path de un archivo: ')
        except PermissionError:  # atajo errores si el archivo no se puede abrir por permisos.
            print("No se puede abrir un archivo que requiere permisos.")
            file2encript = input('Ingrese el path de un archivo: ')
        except IsADirectoryError:  # atajo errores si el usuario ingresa un directorio.
            print("Es un directorio.")
            file2encript = input('Ingrese el path de un archivo: ')
    return file2encript


def file2list(file: str):
    with open(file, 'rt') as archivo:
        # lineas = archivo.readlines()
        lineas = [i.rstrip() for i in archivo if i != "\n"]
        # sep_lineas = []
        # for linea in lineas:
        #     linea = linea.rstrip()
        #     sep_lineas.append(linea)
        # lineas = '\n'.join(sep_lineas)
    return lineas

def encriptador(lineas: str, clave: str):
    """
    Escribir docstring
    """
    encripted_line = []
    letras_especiales = 0
    linea = '\n'.join(lineas)
    for i, c in enumerate(linea):
        letra_index = c.lower()
        c = ord(letra_index) - 97

        if c >= 0 and c <= 25:
            c = (c + ord(clave[(i - letras_especiales) % len(clave)]) - 97) % 26
            if c > 25:
                c -= 26
                encripted_line += chr(c + 97)
            else:
                encripted_line += chr(c + 97)
        else: 
            encripted_line += chr(c + 97)
            letras_especiales += 1

    return ''.join(encripted_line)

    
    
def nuevo_archivo(lineas: str, path: list, clave: str):
    """
    escribo docstring
    """
    if '.txt' not in path:
        path += '.txt'
    with open(path, 'wt') as encripted_file:        
        encripted_lines = encriptador(lineas, clave)
        encripted_file.write(encripted_lines)


def password_check(clave):
    """
    Escribir docstring
    """
    clave = clave.lower()
    valid_pass = True
    for letra in clave:
        if ord(letra) > 122 or ord(letra) < 97:
            valid_pass = False
    return valid_pass


def main(file, clave, path):
    """
    escribo docstring
    """
    while password_check(clave) is False:
        clave = input('La clave solo puede ser compuesta por letras del abecedario ingles\nIngrese otra clave: ')
    lines = file2list(file)
    nuevo_archivo(lines, path, clave)


file = file_check(input('Ingrese el path del archivo: '))
clave = input('ingrese la clave: ')
path = input('Ingrese el path del nuevo archivo: ')
main(file, clave, path)

