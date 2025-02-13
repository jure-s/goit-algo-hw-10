import unittest
import scipy.integrate as spi
from monte_carlo_integration.quad_check import analytical_integration, f

class TestQuadCheck(unittest.TestCase):
    def test_quad_accuracy(self):
        a, b = 0, 2
        quad_result, error = analytical_integration(a, b)
        expected_result, _ = spi.quad(f, a, b)
        
        # Перевіряємо, що результат quad відповідає очікуваному значенню
        self.assertAlmostEqual(quad_result, expected_result, delta=1e-6)
    
    def test_quad_non_negative(self):
        a, b = 0, 2
        quad_result, _ = analytical_integration(a, b)
        
        # Інтеграл не може бути від'ємним
        self.assertGreaterEqual(quad_result, 0, "Результат інтегрування повинен бути невід'ємним")

if __name__ == "__main__":
    unittest.main()