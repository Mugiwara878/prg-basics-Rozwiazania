import math


tree_circumference = int(input("Enter tree circumference in cm: "))
tcbcd = tree_circumference/math.pi >= 50
print(f"Tree can be cut down: {tcbcd}") 