'''
Given two integers a and b, which can be positive or negative, 
find the sum of all the numbers between including them too and return it. 
If the two numbers are equal return a or b.

Note: a and b are not ordered!
'''

def get_sum(a,b):
    mi =min(a,b)
    if mi == a:
        ma =b
    else:
        ma =a
    result =0
    for i in range(mi,ma+1):
        result +=i
    return result

if __name__ == "__main__":
    a,b =input("Enter 2 number: ").split()
    try:
        res =get_sum(int(a),int(b))
        print(res)
    except ValueError as e:
        print(e)