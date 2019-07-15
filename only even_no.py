numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
list_Even_Numbers= list(filter(lambda x: x % 2 == 0, numbers))
print("Following are Even numbers in a list ="+str(list_Even_Numbers))