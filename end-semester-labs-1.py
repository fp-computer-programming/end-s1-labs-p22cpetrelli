#author CJP  1/24/12
#defining function
def shortcut(x): 

# making variable
    for vowel in "aeiou": 
         x = x.replace(vowel, "") 
    return x # return result to function


print(shortcut("crab"))
print(shortcut("train"))
print(shortcut("horse"))