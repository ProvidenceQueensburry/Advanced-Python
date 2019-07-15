def is_Even(x):
    if x % 2 == 0:
       return True
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(is_Even, numbers)))

