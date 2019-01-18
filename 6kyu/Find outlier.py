'''
You are given an array 
which will have a length of at least 3, but could be very large
containing integers. The array is either entirely comprised of odd integers 
or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.
'''

def find_outlier(integers):
    a =list()
    for i in range(len(integers)):
        a.append(integers[i] %2)
        for backItem in a[:i+1]:
            if a[i] != backItem:
                if i <2:
                    if integers[i+1] %2 ==a[i]:
                        return integers[0]
                return integers[i]
    return None
    
if __name__ == "__main__":
    testAry =[[2, 4, 0, 100, 4, 11, 2602, 36],\
              [160, 3, 1719, 19, 11, 13, -21]]
    for i in range(len(testAry)):
        res =find_outlier(testAry[i])
        print(res)