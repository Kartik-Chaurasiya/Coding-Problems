"""Your task is to sort a given string. Each word in the string will 
contain a single number. This number is the position the word should 
have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the 
input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""

def order(sentence):
    words = sentence.split()
    
    dict = {}                     #dictionary
    str = ""
    for word in words:            #for single word in words
        for a in word:            #for single alphabet in word
            if a.isdigit() :      
                dict[a] = word
    
    for i in sorted(dict.keys()):
        str += dict[i]
        str += ' '
    str = str[:-1]                #remove the last space
    return str

s = order("is2 Thi1s T4est 3a")
print(s)

"""Output :-
Thi1s is2 3a T4est
[Finished in 0.2s]
"""

#Same can be done in one sentence:-

def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))