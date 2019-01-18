def longest_consec(strarr, k):
    longest =""
    maxlen =0
    if k >len(strarr) or k <=0:
        return ""
    for i in range(len(strarr)):
        c_maxlen =0
        for j in range(k):     
            if i +k>len(strarr):
                break
            c_maxlen +=len(strarr[i+j])
        if maxlen < c_maxlen:
            maxlen =c_maxlen   
            headPos =i
    for i in range(headPos,headPos+k):
        longest +=strarr[i]
    return longest
if __name__ == "__main__":
    k =["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
    a =longest_consec(k,2)
    print(a)