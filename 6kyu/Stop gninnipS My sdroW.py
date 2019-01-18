'''
Write a function that takes in a string of one or more words, 
and returns the same string, 
but with all five or more letter words reversed 
(Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.
'''

def spin_words(sentence):
    rStr =""
    spL =sentence.split(" ")
    for k in spL:
        if len(k) >4:
            rWord =""
            for i in range(len(k)-1,-1,-1):
                rWord +=k[i]               
            k =rWord           
        if rStr=="":
            rStr =k
        else:
            rStr +=str(" ")+k
    return rStr

if __name__ == "__main__":
    foo =input("String: ")
    k =spin_words(foo)
    print(k)