n = int(input())
sum_of_even = 0
sum_of_odd = 0
while n > 0:
    r = (n%10)
    if r % 2 == 0:
        sum_of_even = sum_of_even + r
    else:
        sum_of_odd = sum_of_odd + r
    n = (n // 10) 
print(sum_of_even,sum_of_odd)
