def desencriptador (encripted_file , clave):
    """ 
    Pide al usuario una clave y un path para un archivo el cual desea que su contenido sea desencripado.
    Guarda el texto desencriptado en un nuevo archivo con un nombre elegido por el usuario.
    Si no existe el archivo que quiere desencriptar pide que ingresen un path hasta que exista el archivo con dicho path.
    La clave debe ser compuesta unicamente por letras de abecedario ingles minusculas.
    """



    while True: #reviso si existe el path. si no existe, sigue preguntando hasta que exista. Uso el try-except por los Errores.
        try:
            with open(encripted_file, 'r'):
                break
        except FileNotFoundError:
            print('No existe el archivo.')
            encripted_file = input('Ingrese el path de un archivo: ')

    
    while clave.isalpha() is not True: #reviso que la contrasena este compuesta solamente por letras del abecedario ingles.
        print('La clave solo puede contener letras del alfabeto inglés')
        clave = input('Ingrese una clave: ')

    with open(encripted_file, 'rt') as encripted_file: #abro el file en modo de lectura porque simplemente me interesa la informacion del archivo

        destination = input('Cree un nombre para el archivo desencriptado: ') #pido el nombre del archivo donde se va a guardar el exto desencriptado.
        if '.txt' not in destination: #si el usuario escribe el archivo si el '.txt' se lo agrego.
            destination +='.txt'

        with open (destination,'wt') as desencripted_file: #creo el archivo donde se va a guardar el texto desencriptado.
            lineas = encripted_file.readlines()
    
            for linea in lineas:
                desencripted_line = []
                for i in range(len(linea)):
                    letra_index = linea[i].lower() 
                    c = ord(letra_index) - 97
                    if c >= 0 and c <= 25:
                        c = c - ord(clave[i % len(clave)]) + 97
                        if c < 0:
                            c += 26
                        if c > 25:
                            c -= 26
                            desencripted_line += chr(c + 97)
                        else:
                            desencripted_line += chr(c + 97) 
                    else: 
                        desencripted_line += chr(c + 97) 
                desencripted_file.write(''.join(desencripted_line))
encripted_file = input('Ingrese el path del archivo que desea desencriptar: ')
clave = input('ingrese la clave: ')
desencriptador(encripted_file,clave)