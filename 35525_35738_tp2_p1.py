def file_check(file2encript: str)-> str:
    """
    Verifica la existencia del archivo y si el mismo puede ser accedido.
    Argumentos: 
        file2encrypt(str)-> es el path del archivo que va a ser encriptado.
    Returns: 
        file2encrypt (str)-> el path del archivo verificado
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
    Argumentos: 
        file2encrypt(str)-> path del archivo a encriptar.
    Returns: 
        lineas(list)-> contenido del archivo en listas.
    """
    with open(file2encrypt, 'rt') as archivo:
        lineas = [i.rstrip() for i in archivo if i != "\n"]  # listas de compresion para pasar el contenido a una lista de str. Lineas vacias seran eliminadas. Y elimina el \n.
    return lineas


def saca_tildes(lineas:list)->list:
    """
    Lee el contenido del archivo y reemplaza cualquier vocal con tilde por la vocal sin tilde.
    Argumentos: 
        lineas(list)->contenido del archivo en lista
    Returns: 
        lineas_sin_tildes(list)-> contenido del archivo en lista sin tildes.
    """
    print('Aviso: El programa no encripta tildes. Si el archivo contiene alguna va a ser cambiada a su respectiva vocal.')
    tildes = {'a': 'áâàãäå', 
              'e': 'éêèë',
              'i': 'íîìï',
              'o': 'óôòõö',
              'u': 'úûùü'}
    lineas_sin_tildes = [] 
    for linea in lineas:
        linea_sin_tildes = []        
        for letra in linea:
            for vocal, vocal_tildes in tildes.items():
                if letra in vocal_tildes:
                    letra = vocal   # intercambio vocal con tilde por su vocal correspondiente.
                    break
            linea_sin_tildes.append (letra)
        linea_sin_tildes = ''.join(linea_sin_tildes)
        lineas_sin_tildes.append(linea_sin_tildes) 
    return lineas_sin_tildes
                

def encrypter(lineas: list, clave: str)-> list:
    """
    Encripta el texto usando el cifrado de Vigenere.
    Argumentos:
        lineas(list)-> Contenido del archivo en lista de lineas.
        clave(str)-> contrasena que va a ser usada para encriptar.
    Return:
        encripted_line(list)-> Contenido del archivo ya encriptado en una lista.
    """
    encripted_line = []
    letras_especiales = 0
    linea = '\n'.join(lineas)
    for i, c in enumerate(linea):
        letra_index = c.lower()
        c = ord(letra_index) - 97
        if c >= 0 and c <= 25:
            c = (c + ord(clave[(i - letras_especiales) % len(clave)]) - 97) % 26  # uso la formula dada para calcular el valor encriptador.
            encripted_line += chr(c + 97)
        else: 
            encripted_line += chr(c + 97)
            letras_especiales += 1
    encripted_line = ''.join(encripted_line)
    return encripted_line

      
def new_file(lineas: list, path: str, clave: str):
    """
    Crea un archivo y le escribe el archivo viejo ya encriptado.
    Argumentos:
        lineas(list)-> contenido del archivo ya encriptado en una lista
        path(str)-> nombre del archivo que va a ser creado.
        clave(str)-> contrasena que va a ser usada para encriptar.
    Returns:
        None-> no devuelve nada; solamente crea el archivo con el texto encriptado.
    """
    if '.txt' not in path:
        path += '.txt'
    with open(path, 'wt') as encripted_file:   # crea el archivo como 'wt' asi lo crea de cualquier manera, y si el archivo ya existe , lo escribe por arriba.     
        encripted_lines = encrypter(lineas, clave) 
        encripted_file.write(encripted_lines)


def password_check(clave:str)->str:
    """
    Revisa que la contraseña este solamente compuesta por letras del abecedario ingles.
    Argumentos:
        clave(str)-> contraseña que va a ser usada para encriptar.
    Returns:
        valid_pass(bool)-> True si la contraseña es valida y False si no lo es.
    """
    clave = clave.lower()
    valid_pass = True
    for letra in clave:
        if ord(letra) > 122 or ord(letra) < 97:
            valid_pass = False
    return valid_pass


def main():
    """
    Funcion principal que ejecuta el programa.
    No recibe argumentos.
    No devuelve ningun valor.
    """
    print('≡≡Encriptador de Cifrado de Vigenère≡≡')
    file = file_check(input('Ingrese el path del archivo en texto plano: '))
    clave = input('Ingrese la clave: ')
    while password_check(clave) is False: # si la contraña es invalida; la pido devuelta hasta que sea valida. 
        clave = input('La clave solo puede ser compuesta por letras del abecedario ingles\nIngrese otra clave: ')
    
    path = input('Ingrese el nombre del archivo para la encripcion: ')
    lines = file2list(file)
    sin_tildes = saca_tildes(lines)
    new_file(sin_tildes, path, clave)


if __name__== '__main__':  # comienzo el programa
    main()