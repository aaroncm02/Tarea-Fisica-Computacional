#!/usr/bin/env python3

import numpy as np

def gaussxw(N):
    """Calcula los puntos de colocación y pesos para la cuadratura de Gauss-Legendre.

    Args:
        N (int): Número de puntos de la cuadratura.

    Returns:
        tuple: (x, w) donde `x` son los puntos y `w` los pesos.

    Example:
        >>> x, w = gaussxw(4)
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """Escala los puntos y pesos del intervalo [-1, 1] al intervalo [a, b].

    Args:
        a (float): Límite inferior.
        b (float): Límite superior.
        x (array): Puntos originales.
        w (array): Pesos originales.

    Returns:
        tuple: (x', w') puntos y pesos escalados.

    Example:
        >>> gaussxwab(0, np.pi, x, w)
    """
    xp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w
    return xp, wp

def integrando(x):
    """Función a integrar: sin(x²)."""
    return np.sin(x**2)

def cuadratura_gaussiana(N, a=0, b=np.pi):
    """Calcula la integral ∫ sin(x²) dx usando cuadratura gaussiana.

    Args:
        N (int): Número de puntos de cuadratura.
        a (float): Límite inferior (default=0).
        b (float): Límite superior (default=π).

    Returns:
        float: Valor estimado de la integral.

    Example:
        >>> cuadratura_gaussiana(10)
    """
    x, w = gaussxw(N)
    xp, wp = gaussxwab(a, b, x, w)
    return np.sum(wp * integrando(xp))
