def is_Odd(x):
    if x % 2 == 1:
        return True
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(is_Odd, numbers)))