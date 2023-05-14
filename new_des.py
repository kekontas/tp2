def file_check(file2encript: str)-> str:
    """
    Verifica la existencia del archivo y si el mismo puede ser accedido.
    Argumentos: file2encrypt(str)-> es el path del archivo que va a ser encriptado.
    Returns: file2encrypt (str)-> es el path del archivo verificado
    """
    # Verifica la accesibilidad y existencia del archivo.
    while True:
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

def file2list(file2encrypt: str)->list:
    """
    Lee el archivo y devuelve su contenido como una lista de cadenas.
    Argumentos: file2encrypt(str)-> path del archivo a encriptar.
    Returns: lineas(list)-> contenido del archivo en listas.
    """
    with open(file2encrypt, 'rt') as archivo:
        lineas = [i.rstrip() for i in archivo if i != "\n"]  # listas de compresion para pasar el contenido a una lista. Lineas vacias seran eliminadas.
    return lineas

def decrypter(lineas: list, clave: str)-> list:
    """
    Escribir docstring
    """
    desencripted_line = []
    letras_especiales = 0
    linea = '\n'.join(lineas)
    for i, c in enumerate(linea):
        letra_index = c.lower()
        c = ord(letra_index) - 97

        if c >= 0 and c <= 25:
            c = (c - ord(clave[(i - letras_especiales) % len(clave)]) - 97) % 26
            if c < 0:
                c += 26
                desencripted_line += chr(c + 97)
            else:
                desencripted_line += chr(c + 97)
        else: 
            desencripted_line += chr(c + 97)
            letras_especiales += 1
    desencripted_line = ''.join(desencripted_line)
    return desencripted_line


def new_file(lineas: list, path: str, clave: str):
    """
    escribo docstring
    """
    if '.txt' not in path:
        path += '.txt'
    with open(path, 'wt') as decrypted_file:        
        decrypted_lines = decrypter(lineas, clave)
        decrypted_file.write(decrypted_lines)


def password_check(clave:str)->str:
    """
    Revisa que la contrasena este solamente compuesta por letras del abecedario ingles.
    Argumentos:
        clave(str)-> contrasena que va a ser usada para encriptar.
    Returns:
        valid_pass(bool)-> True si la contrasena es valida y False si no lo es.
    """
    clave = clave.lower()
    valid_pass = True
    for letra in clave:
        if ord(letra) > 122 or ord(letra) < 97:
            valid_pass = False
    return valid_pass

def main():
    print('≡≡Desencriptador de Cifrado de Vigenère≡≡')
    file = file_check(input('Ingrese el path del archivo encriptado: '))
    clave = input('Ingrese la clave: ')
    while password_check(clave) is False:
        clave = input('La clave solo puede ser compuesta por letras del abecedario ingles\nIngrese otra clave: ')
    path = input('Ingrese el nombre del archivo para la desencripcion: ')
    lines = file2list(file)
    new_file(lines, path, clave)
main()