def increment (y):
    return (lambda x: x+1) (y)
a = int(input("enter the value"))
print("a = ", a)
print("a after incrementing = ")
b = increment(a)
print(b)
