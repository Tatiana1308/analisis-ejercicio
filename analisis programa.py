import numpy as np # esta linea importa la biblioteca numpy y su alias np
import matplotlib.pyplot as plt # esta linea importa la biblioteca matplotlib y su alias plt
def mandelbrot(h, w, maxit=20, r=2): # crea una funcion determinando 4 parametros los cuales son (h, w, maxit=20, r=2)
    """Returns an image of the Mandelbrot fractal of size (h,w).""" 
    x = np.linspace(-2.5, 1.5, 4*h+1) # esta linea crea una matriz o funcion de 1 dimension
    y = np.linspace(-1.5, 1.5, 3*w+1) # esta linea crea una matriz o funcion de 1 dimension
    A, B = np.meshgrid(x, y) #crea listas de dos dimensiones
    C = A + B*1j # crea una dimension en la que usa numeros complejos
    z = np.zeros_like(C) #crea un arreglo con dos dimensiones y dos elementos en cada una
    divtime = maxit + np.zeros(z.shape, dtype=int) # almacena la secuencia de los iterables

    for i in range(maxit): # es un ciclo el cual itera en maxir
        z = z**2 + C # utiliza los valores de z elevandolo al cuadrado y sumando c
        diverge = abs(z) > r                    # crea una lista booleana cuando su la magnitud de r es verdadera
        div_now = diverge & (divtime == maxit)  # crea una lista booleana cuando el valor de divtime es igual a maxit
        divtime[div_now] = i                    # actualiza los datos divtime
        z[diverge] = r                          # 

    return divtime # borra la cifra que actual del terminal
plt.clf()
plt.imshow(mandelbrot(400, 400))