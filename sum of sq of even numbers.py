n = int(input("Enter the number : "))
s=0
for i in range(1,n+1):
    if(i%2 == 0):
        term = i**2
    else:
        term=0
    s = s+term
print ("The sum of squares of even number less than", n, "is", s)
