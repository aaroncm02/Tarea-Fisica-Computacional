# Ejemplo de uso

Este es un ejemplo de cómo utilizar el módulo `cuadrature.py` para estimar la integral de \(\sin(x^2)\) en el intervalo \([0, \pi]\).

```python

from cuadrature import gaussxw, gaussxwab, integrando
import numpy as np

# Definimos el intervalo
a = 0.0
b = np.pi

# Elegimos los número de puntos
N = 10

# Obtenemos puntos y pesos
x, w = gaussxw(N)
x_scaled, w_scaled = gaussxwab(a, b, x, w)

# Calculamos la integral
resultado = np.sum(w_scaled * integrando(x_scaled))
print(f"Resultado con N=10: {resultado:.5f}")
