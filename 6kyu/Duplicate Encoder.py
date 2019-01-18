'''
The goal of this exercise is to convert a string to a new string 
where each character in the new string is '(' if that character appears only once in the original string, 
or ')' if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.
'''

def duplicate_encode(word):
    word =word.lower()
    encMsg =""
    for i in range(len(word)):
        for j in range(len(word)):
            if word[i] == word[j] and i != j:
                same =True
                break
            else:
                same =False
        if same ==True:           
            encMsg +=")"
        else:           
            encMsg +="("            
    return encMsg

if __name__ == "__main__":
    word =input("Sentence: ")
    encMsg =duplicate_encode(word)
    print(encMsg)