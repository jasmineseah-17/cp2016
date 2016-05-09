def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
#check whether input is even and greater than 3
even = False
while even == False:
    if n % 2 != 0:
        print("Please enter an even number!")
        n = int(input())
    elif n < 3:
        print("Please enter a number greater than 3!")
        n = int(input())
    else:
        even = True

#assuming input is an even number greater than 3
quotient = n // 2
solved = False
while solved == False:
    if is_prime(quotient) == True:
        solved = True
    else:
        quotient -= 1

print(quotient , '+', n-quotient, '=', n)
