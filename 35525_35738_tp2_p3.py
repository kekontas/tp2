import matplotlib.pyplot as plt

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


def file2text(file2encrypt: str)->list:
    """
    Lee el archivo y devuelve su contenido como una lista de cadenas.
    Argumentos: file2encrypt(str)-> path del archivo a encriptar.
    Returns: lineas(list)-> contenido del archivo en listas.
    """
    texto = ''
    with open(file2encrypt, 'rt') as archivo:
        lineas = [i.rstrip().lower() for i in archivo if i != "\n"]  # listas de compresion para pasar el contenido a una lista. Lineas vacias seran eliminadas.
    for linea in lineas:
        for c in linea:
            if c.isalpha():
                texto += c
    return texto


def sep_groups(texto: str, largo_clave: int)-> list:
    """
    Separa el texto en listas con el largo de la clave -1 de separacion entre caracteres.
    Argumentos:
        texto(str)-> texto que va a ser separado
    Returns:
        lista_letras(list)-> lista del texto separado.
    """
    
    lista_letras = []
    
    for i in range(largo_clave):
        lista_letra = [texto[j] for j in range(i, len(texto), largo_clave)]
        lista_letras.append(lista_letra)
    return lista_letras


def ioc_calc(lista_letras: list)-> float:
    """
    Calcula el IoC.
    Argumentos:
        lista_letras(list)-> lista del texto separado
    Returns:
        avg_ioc(float)->Promedio del IoC de las listas.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'

    ioc = []
    for lista in lista_letras:
        numerador = 0
        for j in letters:
            numerador += lista.count(j) * (lista.count(j) - 1)
        denominador = len(lista) * (len(lista) - 1)
        ioc.append(numerador / denominador)
    avg_ioc = 0
    for i in ioc:
        avg_ioc += i
    avg_ioc = avg_ioc / len(ioc)
    return avg_ioc

def plot1(texto: str):
    """
    Prepara el primer gafico con los posibles largos de la clave.
    Argumentos:
        texto(str)->texto el cual va a calcular los valores para el grafico.
    """
    x = [clave for clave in range(1,31)]
    y = []
    for a in range(1,31):
        y.append(ioc_calc(sep_groups(texto, a))) # calcula el IoC de los distintos grupos.
    plt.bar(x, y)
    plt.axhline(y = 0.0686, color = 'black' , linestyle ='--', label = '6.86%')
    plt.axhline(y = 0.0385, color = 'black' , linestyle ='--', label = '3.85%')
    plt.xlabel('Largo de la clave')
    plt.ylabel('Índice de coincidencia (IoC)')

    plt.show()

def graf_ing():
    """
    Genera el grafico de frecuencias de las letras del abecedario ingles.
    """
    plt.subplot(3,2,1) # Ubica al grafico en la posicion 1 del subplot
    english_frequencies = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
    }

    plt.bar(english_frequencies.keys() , english_frequencies.values()  ) # Grafico con valores de X e Y
    plt.title('Ingles')
    plt.ylabel('Frecuencia')

def graficos(texto: str, largo_clave: int):
    """
    Genera los graficos correspondientes a la frecuencia de las letras,
    agrupadas en 'n' grupos ('n' siendo el largo de la clave), para el texto.
    Argumentos:
    texto -- cadena a evaluar
    largo_clave -- largo de la clave
    """
    for j in range(largo_clave): # Generador de graficos
        plt.subplot(3,2, j + 2) # Ubica a los graficos en la posicion correspondiente del subplot  
        values = [texto[i] for i in range(j, len(texto), largo_clave)] 

        dict_freq = {}
        abc = 'abcdefghijklmnopqrstuvwxyz'
        for i in abc:
            cantidad = values.count(i)
            freq = cantidad / len(values)
            dict_freq[i] = freq

        x = dict_freq.keys()

        y = dict_freq.values()
        plt.bar(x, y)
        plt.ylabel('Frecuencia')
        plt.title(f'Letra {j + 1} de la clave')
    plt.tight_layout()
    plt.show()


def main():
    """
    Función principal del programa de análisis de texto encriptado.
    No recibe argumentos.
    No devuelve argumentos.
    """
    file = file_check(input('Ingrese el nombre del archivo encriptado: '))
    texto = file2text(file)
    plot1(texto)
    largo_clave = int(input('ingrese el valor que representa el primer pico maximo del grafico: '))
    graf_ing()
    graficos(texto, largo_clave)


if __name__ == '__main__':
    main()