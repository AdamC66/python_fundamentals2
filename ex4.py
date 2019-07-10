#Define a function that accepts a string as an argument 
# and returns False if the word is less than 8 characters long 
# (or True otherwise).

def len_check(string):
    if len(string)>=8:
        return(True)
    else: 
        return(False)

print(len_check("apple"))
print(len_check("orange"))
print(len_check("adamjcote"))
print(len_check("mapleleafs"))
print(len_check("hello"))
print(len_check("hello world"))
print(len_check("battery"))