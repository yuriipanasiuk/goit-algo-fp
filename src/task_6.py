# Adjusting the code to use a dictionary for items instead of a list of tuples.

# Define the items with their cost and calorie value.
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


# Greedy approach
def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for item_name, details in sorted_items:
        if details["cost"] <= remaining_budget:
            chosen_items.append(item_name)
            total_calories += details["calories"]
            remaining_budget -= details["cost"]

    return total_calories, budget - remaining_budget, chosen_items


# Dynamic Programming approach
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(items)

    # Create a DP table where rows represent up to the i-th item and columns represent budget
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    # Побудова таблиці оптимального вибору калорій
    for i in range(1, n + 1):
        item = items[item_names[i - 1]]
        for w in range(budget + 1):
            if item["cost"] <= w:
                dp_table[i][w] = max(
                    dp_table[i - 1][w],  # не брати страву
                    dp_table[i - 1][w - item["cost"]] + item["calories"],
                )  # взяти страву
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    # Реалізація отримання оптимального набору страв через використання обчисленої таблиці
    chosen_items = []
    temp_budget = budget

    for i in range(n, 0, -1):
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            item_name = item_names[i - 1]
            chosen_items.append(item_name)
            temp_budget -= items[item_name]["cost"]

    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


if __name__ == "__main__":
    # Execute both algorithms
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print(greedy_result, dp_result)
