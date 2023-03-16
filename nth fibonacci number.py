def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2) 
        
n=int(input())
print(Fibonacci(n))

#Use this if run time error occurs

n = int(input())
a = 0
b = 1
c = -1
for i in range(n) :
    c = a + b
    a = b
    b = c 
print(a)
