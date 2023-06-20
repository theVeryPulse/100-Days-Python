#Write your code below this line 👇
import math
def prime_checker(number):
    prime_number = True
    for i in range(2, math.ceil(number/2)):
        if number % i == 0:
            prime_number = False
            break
    return prime_number
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
if prime_checker(number=n) == True:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
