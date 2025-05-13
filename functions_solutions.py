# Function Basics
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
# Example usage:
print(calculate_average([5, 10, 15, 20])) # 12.5
print(calculate_average([]))  # Should return 0
print(calculate_average([2,4,6,8,12,14,16,18,20])) # 11.111111111




# Default Parameters
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"
# Example usage:
print(greet_user("Mahak")) # Hello, Mahak!
print(greet_user("Bob", "Hi")) # Hi, Bob!





# Variable arguments
def calculate_total(*prices, discount=0):
    total = sum(prices)
    if discount:
        total -= total * (discount / 100)
    return total
# Example usage:
print(calculate_total(10, 20, 30))  # 60
print(calculate_total(10, 20, 30, discount=10))  # 54
print(calculate_total(50, 25, discount=10))  # 67.5




# Closures
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier
# Example usage:
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))   # 10
print(triple(4))   # 12