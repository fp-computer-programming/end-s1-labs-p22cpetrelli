#author CJP  1/24/12
def is_triangle(a, b, c):

#makes sure sides are able to form triangle
    if ((a < b + c) and (b < a + c) and (c < a + b)) == True:
        return True 
# if false it is not a triangle and the function will return false
    else: 
        return False 

print(is_triangle(3, 4, 5) == True)
print(is_triangle(2, 2, 6) == False)
print(is_triangle(7, 2, 3) == False)