a = [1,2,3,4,5,6]
p = 7
a.append(p)  # Add P
a = sorted(a)  # Sort
a = list(set(a))  # Remove Duplicate
print(a.index(p))  # Print Index