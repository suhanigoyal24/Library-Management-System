def readwords():
    
    v,c,u,l=0,0,0,0
    vowel='aeiouAEIOU'
    r='count'
    print('the opened file contains the following data:')
    for i in r:
        if i.isalpha():
            if i in vowel:
                v+=1
            elif i not in vowel:
                c+=1
            else:
                pass
        else:
            pass
    for i in r:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
        else:
            pass
    print('total uppercase letters are',u)    
    print('total lowercase letters are',l)
    print('total vowels are',v)    
    print('total constants are',c)
readwords()
