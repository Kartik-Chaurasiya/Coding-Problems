"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces."""

# basic solution

def getCount(inputStr):
    num_vowels = 0
    # your code here
    for i in range (0, len(inputStr)):
        if (inputStr[i] == "a") or (inputStr[i] == "i") or (inputStr[i] == "u") or (inputStr[i] == "e") or (inputStr[i] == "o"):
            num_vowels = num_vowels + 1
    
    return num_vowels

# Logical Solution

import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))