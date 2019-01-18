'''
Define a function isPrime/is_prime() that takes one integer argument 
and returns true/True or false/False depending on if the integer is a prime.
Per Wikipedia, 
a prime number (or a prime) is a natural number greater than 1 
that has no positive divisors other than 1 and itself.
'''
def is_prime(num):
    num =int(num)
    if num ==2:
        return True
    end2 =["2","4","6","8"]
    if str(num)[-1] in end2 or num <2:
        return False
    for i in range(2,num):
        if num % i ==0:
            return False
    return True
if __name__ == "__main__":
    try:
        a =input("Number: ")
        print(is_prime(a))
    except TypeError as e:
        print(e)