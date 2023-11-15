import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
# print("Dimension of the array is " , arr.ndim)
# print("Shape of the array is" , arr.shape)
# print("data type of the array is " , arr.dtype)
# print(arr.itemsize)
# print(arr.data)


# arr2 = np.arange(15).reshape(3,5).astype(dtype=complex)

# print(arr2)


# arr3 = np.zeros((3,4))
# print(arr3)


# arr4 = np.linspace(0 , 1000 , 100)
# print(arr4)

# a = np.array([[1,2,3,4,5],[6,7,8,9,1]])
# b = np.array([[5,4,3,2,1],[1,2,3,4,5]])
# print( "Addition of the two matrix is ", a + b)
# print("Subtraction of two matrix is ", a - b)
# print("Multiplication of two matrix " , a*b)

# np.column_stack() it is used to two 1D array is convert into 2D array


# print(np.arange(12)**2)

# palette = np.array([[0, 0, 0],         # black
#                     [255, 0, 0],       # red
#                     [0, 255, 0],       # green
#                     [0, 0, 255],       # blue
#                     [255, 255, 255]]) 

# image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
#                   [0, 3, 4, 0]])

# print(palette[image] )


import numpy as np
import matplotlib.pyplot as plt
def mandelbrot(h, w, maxit=20, r=2):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x = np.linspace(-2.5, 1.5, 4*h+1)
    y = np.linspace(-1.5, 1.5, 3*w+1)
    A, B = np.meshgrid(x, y)
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))