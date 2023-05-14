import  encriptador as enc



# def decrypter(lineas: list, clave: str)-> list:
#     """
#     Escribir docstring
#     """
#     desencripted_line = []
#     letras_especiales = 0
#     linea = '\n'.join(lineas)
#     for i, c in enumerate(linea):
#         letra_index = c.lower()
#         c = ord(letra_index) - 97

#         if c >= 0 and c <= 25:
#             c = (c - ord(clave[(i - letras_especiales) % len(clave)]) - 97) % 26
#             if c < 0:
#                 c += 26
#                 desencripted_line += chr(c + 97)
#             else:
#                 desencripted_line += chr(c + 97)
#         else: 
#             desencripted_line += chr(c + 97)
#             letras_especiales += 1
#     desencripted_line = ''.join(desencripted_line)
#     return desencripted_line


# def new_file(lineas: list, path: str, clave: str):
#     """
#     escribo docstring
#     """
#     if '.txt' not in path:
#         path += '.txt'
#     with open(path, 'wt') as decrypted_file:        
#         decrypted_lines = decrypter(lineas, clave)
#         decrypted_file.write(decrypted_lines)



# def main2():
#     """
#     escribo docstring
#     """
#     file = enc.file_check(input('Ingrese el path del archivo: '))
#     clave = input('Ingrese la clave: ')
#     while enc.password_check(clave) is False:
#         clave = input('La clave solo puede ser compuesta por letras del abecedario ingles\nIngrese otra clave: ')
#     path = input('Ingrese el path del nuevo archivo: ')
#     lines = enc.encrypterfile2list(file)
#     new_file(lines, path, clave)

if __name__== '__main__':
    enc.main(False)