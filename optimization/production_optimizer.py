from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

def optimize_production():
    # Створюємо модель оптимізації
    model = LpProblem(name="production-optimization", sense=LpMaximize)
    
    # Змінні: кількість вироблених напоїв
    lemonade = LpVariable(name="Lemonade", lowBound=0, cat='Integer')
    fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat='Integer')
    
    # Обмеження ресурсів
    model += (2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint")
    model += (1 * lemonade <= 50, "Sugar_Constraint")
    model += (1 * lemonade <= 30, "Lemon_Juice_Constraint")
    model += (2 * fruit_juice <= 40, "Fruit_Puree_Constraint")
    
    # Цільова функція - максимізувати загальну кількість вироблених напоїв
    model += lemonade + fruit_juice, "Total_Production"
    
    # Вимкнення додаткового виводу розв'язувача
    solver = PULP_CBC_CMD(msg=False)
    model.solve(solver)
    
    # Повертаємо результати
    return {"Lemonade": lemonade.varValue, "Fruit_Juice": fruit_juice.varValue, "Total_Production": model.objective.value()}

if __name__ == "__main__":
    result = optimize_production()
    print(f"Оптимальна кількість лимонаду: {result['Lemonade']}")
    print(f"Оптимальна кількість фруктового соку: {result['Fruit_Juice']}")
    print(f"Максимальна загальна кількість напоїв: {result['Total_Production']}")