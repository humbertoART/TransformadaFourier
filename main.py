import numpy as np
"""
MATRIZ DE LA TRANSFORMADA DE FOURIER
"""
print('MATRIZ DE LA TRANSFORMADA DE FOURIER')
n = 4
j = np.arange(n)
k = j.reshape((n,1))
w = np.exp((-2j * np.pi) / n)
F = w**(j*k)
print(np.round(F))
print('============================================\n')

"""
MATRIZ INVERSA DE LA TRANSFORMADA DE FOURIER
"""
print('MATRIZ INVERSA DE LA TRANSFORMADA DE FOURIER')
wn1 = np.exp(2j * np.pi / n)
Finv = wn1**(j*k)
print(np.round(Finv))
