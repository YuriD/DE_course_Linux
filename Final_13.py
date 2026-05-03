purchases = [
  {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
  {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
  {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
  {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
  total = 0
  for purchase in purchases:
    total += purchase['price'] * purchase['quantity']
  return total

def items_by_category(purchases):
  category_dict = {}
  for purchase in purchases:
    category = purchase['category']
    if category not in category_dict:
      category_dict[category] = []
    category_dict[category].append(purchase['item'])
  return category_dict                    

def expensive_purchases(purchases, min_price):
  expensive = []
  for purchase in purchases:
    if purchase['price'] >= min_price:
      expensive.append(purchase)
  return expensive

def average_price_by_category(purchases):
  category_totals = {}
  category_counts = {}
  for purchase in purchases:
    category = purchase['category']
    if category not in category_totals:
      category_totals[category] = 0
      category_counts[category] = 0
    category_totals[category] += purchase['price'] * purchase['quantity']
    category_counts[category] += purchase['quantity']
  average_prices = {}
  for category in category_totals:
    average_prices[category] = round(category_totals[category] / category_counts[category], 2)
  return average_prices

def most_frequent_category(purchases):
  category_counts = {}
  for purchase in purchases:
    category = purchase['category']
    category_counts[category] = category_counts.get(category, 0) + purchase['quantity']
  return max(category_counts, key=category_counts.get)

if __name__ == "__main__":
    total = total_revenue(purchases)
    print(f"Общая выручка: {total:.1f}")
    print(f"Товары по категориям: " + str(items_by_category(purchases)))
    print("Покупки дороже 1.0: " + str(expensive_purchases(purchases, 1.0)))
    average_prices = average_price_by_category(purchases)
    print(f"Средняя цена по категориям: " + str(average_prices))
    most_frequent = most_frequent_category(purchases)
    print(f"Категория с наибольшим количеством проданных товаров: {most_frequent}")