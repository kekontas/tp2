 #%%
def encriptador (file, clave):
    """
    Escribir docstring
    """
    with open(file, 'r') as archivo:
        with open ('encripted.txt','w') as encripted_archive:
            lineas = archivo.readlines()
            encripted_line = []
            for linea in lineas:
                for i in range(len(linea)):
                    c = ord(linea[i]) - 97
                    if c >= 0 or c <= 26:
                        c = c + ord(clave[i % len(clave)])
                        encripted_line += chr(c) 
                    else: 
                        encripted_line += chr(c + 97) 
                encripted_archive.write(''.join(encripted_line))
            
print(encriptador('prueba1.txt','hola'))


# %%
