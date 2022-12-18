import math

def sure_tailor_rows(n, x):
    if n < 0:
        mess = f"n must be bigger then 0, not {n}"
        raise ValueError(mess)
    if type(n) != int:
        mess = f"n must be int type, not {type(n)}"
        raise TypeError(mess)
    if type(x) not in (int, float):
        mess = f"x must be int or float type, not {type(x)}"
        raise TypeError(mess)

def factorial(n):
    if n < 0:
        return 1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def tailor_exp(n, x = 1):
    sure_tailor_rows(n, x)
    if n == 0:
        return 1
    else:
        return x ** n / factorial(n) + tailor_exp(n - 1, x)

def tailor_sin(n, x = 1):
    sure_tailor_rows(n, x)
    if n == 0:
        return x
    else:
        return ((-1) ** n * x ** (2 * n + 1)) / factorial(2 * n + 1) + tailor_sin(n - 1, x)

def tailor_cos(n, x = 1):
    sure_tailor_rows(n, x)
    if n == 0:
        return 1
    else:
        return ((-1) ** n  * x ** (2 * n)) / factorial(2 * n) + tailor_cos(n - 1, x)

def tailor_arcsin(n, x = 1):
    sure_tailor_rows(n, x)
    if n == 0:
        return x
    else:
        return (factorial(2 * n) * x ** (2 * n + 1)) / ((4 ** n) * (factorial(n) ** 2) * (2 * n + 1)) + tailor_arcsin(n - 1, x)

def tailor_arccos(n, x = 1):
    sure_tailor_rows(n, x)
    if n == 0:
        return x
    else:
        return math.pi / 2 - tailor_arcsin(n, x)
