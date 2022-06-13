B = []
A = [1, 2, 3, 4, 5]
for x in A:
    if x%2 == 0:
        B.append(x**2)
        
print("A = ", A)
print("B = ", B)
print("That is all!")