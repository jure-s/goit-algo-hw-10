from optimization.production_optimizer import optimize_production
from monte_carlo_integration.monte_carlo import monte_carlo_integration, f
from monte_carlo_integration.quad_check import analytical_integration

def main():
    print("=== Оптимізація виробництва ===")
    production_result = optimize_production()
    print(f"Оптимальна кількість лимонаду: {production_result['Lemonade']}")
    print(f"Оптимальна кількість фруктового соку: {production_result['Fruit_Juice']}")
    print(f"Максимальна загальна кількість напоїв: {production_result['Total_Production']}")
    
    print("\n=== Обчислення визначеного інтегралу ===")
    a, b = 0, 2
    monte_carlo_result = monte_carlo_integration(f, a, b, num_samples=100000)
    quad_result, _ = analytical_integration(a, b)
    
    print(f"Метод Монте-Карло: {monte_carlo_result}")
    print(f"Аналітичне рішення (quad): {quad_result}")
    
if __name__ == "__main__":
    main()
