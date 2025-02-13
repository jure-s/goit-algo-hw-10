import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

def plot_integration(a, b):
    """
    Побудова графіка функції f(x) та області під кривою на інтервалі [a, b].
    """
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = f(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2, label='f(x) = x²')
    
    # Заповнення області під кривою
    ix = np.linspace(a, b, 100)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    
    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x² від {a} до {b}')
    ax.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    a, b = 0, 2
    plot_integration(a, b)
