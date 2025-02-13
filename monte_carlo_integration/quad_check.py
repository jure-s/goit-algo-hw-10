import scipy.integrate as spi

def f(x):
    return x ** 2

def analytical_integration(a, b):
    """
    Обчислення визначеного інтегралу функції f(x) методом quad.
    """
    result, error = spi.quad(f, a, b)
    return result, error

if __name__ == "__main__":
    a, b = 0, 2
    integral, error = analytical_integration(a, b)
    print(f"Аналітичне обчислення інтегралу (quad): {integral}")
    print(f"Оцінка похибки: {error}")