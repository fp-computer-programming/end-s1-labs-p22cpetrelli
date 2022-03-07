#author CJP  1/24/12
#define function
def even_or_odd(num):
# if number is divisable by 2 then function will return even 
    if num % 2 == 0:
        return "Even"
#if the number is not then the function will return odd
    else:
        return "Odd"

print(even_or_odd(3) == "Odd")
print(even_or_odd(18) == "Even")
print(even_or_odd(312) == "Even")