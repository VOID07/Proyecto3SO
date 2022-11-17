# Ecualización de una image
from PIL import Image  
import matplotlib.pyplot as plt
import numpy as np
from numpy import asarray

fig, axs = plt.subplots(2,2, figsize=(10, 6.5))
axs[0,0].set_title("Imagen original")

A = Image.open(r'Imagenes_5/sydney.jpg')
A = np.uint8(asarray(A))

axs[0,0].imshow(np.repeat(A[:, :, np.newaxis], 3, axis=2))
h = np.histogram(A, bins=256, range=(0,255))[0] # Cálculo de histograma

axs[0,1].set_title("Histograma")
axs[0,1].bar(np.linspace(0, 255, 256), h, width = 1, color = 'k')
# Distribución acumulada

m, n = A.shape;
ac = np.zeros(256)
ac[0] = h[0]
for i in range(1,255):
    ac[i] = ac[i-1] + h[i]

ac /= m*n

# Obtener nueva imagen aplicando técnica de ecualización
B = np.zeros((m, n))

for x in range(0, m):
    for y in range(0,n):
        B[x,y] = round(ac[A[x,y]]*255)
B = np.uint8(B)

axs[1,0].set_title("Imagen ecualizada")
axs[1,0].imshow(np.repeat(B[:, :, np.newaxis], 3, axis=2))
h1 = np.histogram(B, bins=256, range=(0,255))[0] # Cálculo de histograma

axs[1,1].set_title("Histograma de B")
axs[1,1].bar(np.linspace(0, 255, 256), h1, width = 1, color = 'k')