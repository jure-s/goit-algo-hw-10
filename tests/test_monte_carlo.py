import unittest
import numpy as np
import scipy.integrate as spi
from monte_carlo_integration.monte_carlo import monte_carlo_integration, f

class TestMonteCarloIntegration(unittest.TestCase):
    def test_monte_carlo_accuracy(self):
        a, b = 0, 2
        num_samples = 100000  # Висока кількість вибірок для точності
        monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)
        quad_result, _ = spi.quad(f, a, b)
        
        # Точність Монте-Карло може варіюватися, допускаємо похибку 0.1
        self.assertAlmostEqual(monte_carlo_result, quad_result, delta=0.1)

    def test_monte_carlo_non_negative(self):
        a, b = 0, 2
        result = monte_carlo_integration(f, a, b, num_samples=100000)
        
        # Інтеграл не може бути від'ємним
        self.assertGreaterEqual(result, 0, "Результат інтегрування повинен бути невід'ємним")

if __name__ == "__main__":
    unittest.main()