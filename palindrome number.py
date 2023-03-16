def checkPalindrome(n):
    Revese = 0
    while n > 0:
        Remainder = n % 10
        n = int(n / 10)
        Revese = Revese * 10 + Remainder
    return Revese


num = int(input())
Rev=checkPalindrome(num)
if (num==Rev):
    print('true')
else:
    print('false')
    
    
#Another Solution Of Above Problem


num = int(input())
real_num=num
test_num = 0
while (num > 0):
    remainder = num % 10
    test_num = (test_num * 10) + remainder
    num = num // 10
if int(test_num)==real_num:
    print("true")
else:
    print("false")
