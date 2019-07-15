numbers = [1,56,234,87,4,76,24,69,90,135]

list_Even_Numbers= list(filter(lambda x: x % 2 == 0, numbers))
print("Following are Even numbers in a list ="+str(list_Even_Numbers))