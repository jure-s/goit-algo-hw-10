import numpy as np
import scipy.integrate as spi

def monte_carlo_integration(f, a, b, num_samples=100000):
    """
    Обчислення визначеного інтегралу методом Монте-Карло.
    """
    x_samples = np.random.uniform(a, b, num_samples)
    y_max = max(f(x_samples))
    y_samples = np.random.uniform(0, y_max, num_samples)
    
    under_curve = y_samples <= f(x_samples)
    integral = (b - a) * y_max * np.sum(under_curve) / num_samples
    
    return integral

def f(x):
    return x ** 2

if __name__ == "__main__":
    a, b = 0, 2
    monte_carlo_result = monte_carlo_integration(f, a, b, num_samples=100000)
    quad_result, _ = spi.quad(f, a, b)
    
    print(f"Метод Монте-Карло: {monte_carlo_result}")
    print(f"Аналітичне рішення (quad): {quad_result}")