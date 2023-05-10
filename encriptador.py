def encriptador(file: str, clave: str):
    """
    Pide al usuario una clave y un path para un archivo el cual desea que su contenido sea encripado.
    Guarda el texto encriptado en un nuevo archivo con un nombre elegido por el usuario.
    Si no existe el archivo pide que ingresen un path hasta que exista el archivo con dicho path.
    La clave debe ser compuesta unicamente por letras de abecedario ingles minusculas.
    El archivo no devuelve nada. Solamente crea un archivo con el texto encriptado.
    """



    while True:  # reviso si existe el path. si no existe, sigue preguntando hasta que exista.
        try:
            with open(file, 'r'):
                break
        except FileNotFoundError:  # atajo errores si el archivo no puede ser encontrado
            print('No existe el archivo.')
            file = input('Ingrese el path de un archivo: ')
        except PermissionError:  # atajo errores si el archivo no se puede abrir por permisos.
            print("No se puede abrir un archivo que requiere permisos.")
            file = input('Ingrese el path de un archivo encriptado: ')
        except IsADirectoryError:  # atajo errores si el usuario ingresa un directorio.
            print("Es un directorio.")
            file = input('Ingrese el path de un archivo encriptado: ')
    
    while clave.isalpha() is not True:  # reviso que la contrasena este compuesta solamente por letras del abecedario ingles.
        print('La clave solo puede contener letras del alfabeto inglés')
        clave = input('Ingrese una clave: ')

    with open(file, 'rt') as archivo:  # abro el file en modo de lectura porque simplemente me interesa la informacion del archivo

        destination = input('Cree un nombre para el archivo encriptado: ')  # pido el nombre del archivo donde se va a guardar el exto encriptado.
        if '.txt' not in destination:
            destination += '.txt'

        with open(destination, 'wt') as encripted_archive:  # creo el archivo donde se va a guardar el texto encriptado.
            lineas = archivo.readlines()
    
            for linea in lineas:
                encripted_line = []
                for i in range(len(linea)):
                    letra_index = linea[i].lower() 
                    c = ord(letra_index) - 97
                    if c >= 0 and c <= 25:
                        c = c + ord(clave[i % len(clave)]) - 97
                        if c > 25:
                            c -= 26
                            encripted_line += chr(c + 97)
                        else:
                            encripted_line += chr(c + 97) 
                    else: 
                        encripted_line += chr(c + 97) 
                encripted_archive.write(''.join(encripted_line))


file = input('Ingrese el path del archivo: ')
clave = input('ingrese la clave: ')
encriptador(file, clave)