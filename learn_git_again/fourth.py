A = int(input("Enter A:"))
B = int(input("Enter B:"))
C = int(input("Enter C:"))
print("a is: " + str(A))
print("b is: " + str(B))
print("c is: " + str(C))

X1 = (-B-((B**2)-(4*A*C)))/(2*A)
X2 = (-B+((B**2)-(4*A*C)))/(2*A)

print('The solution are {0:.2f} and {1:.2f}'.format(X1,X2))