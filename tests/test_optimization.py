import unittest
from optimization.production_optimizer import optimize_production

class TestProductionOptimizer(unittest.TestCase):
    def test_production_constraints(self):
        result = optimize_production()
        
        # Перевірка, що розраховані значення не перевищують обмеження ресурсів
        self.assertLessEqual(2 * result['Lemonade'] + result['Fruit_Juice'], 100, "Витрати води перевищують ліміт")
        self.assertLessEqual(result['Lemonade'], 50, "Витрати цукру перевищують ліміт")
        self.assertLessEqual(result['Lemonade'], 30, "Витрати лимонного соку перевищують ліміт")
        self.assertLessEqual(2 * result['Fruit_Juice'], 40, "Витрати фруктового пюре перевищують ліміт")

    def test_optimization_output(self):
        result = optimize_production()
        
        # Перевірка, що результати не є None або негативними
        self.assertIsNotNone(result['Lemonade'])
        self.assertIsNotNone(result['Fruit_Juice'])
        self.assertGreaterEqual(result['Lemonade'], 0, "Кількість лимонаду не може бути від'ємною")
        self.assertGreaterEqual(result['Fruit_Juice'], 0, "Кількість фруктового соку не може бути від'ємною")
        self.assertGreaterEqual(result['Total_Production'], 0, "Загальна кількість продукції повинна бути додатною")

if __name__ == "__main__":
    unittest.main()