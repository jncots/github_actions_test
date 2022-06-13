B = []
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in A:
    if x%2 == 0:
        B.append(x**2)
        
print("A = ", A)
print("B = ", B)
print("That is all!")