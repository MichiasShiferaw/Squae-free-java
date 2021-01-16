def squarefree(s):
    """This is a function that has one parameter, s, where s is a string. The function returns
    True if s is squarefree and False otherwise. 
    Precondition:
    s: is a string
    Return boolean"""
    validity = True
    index = 0
    while (index <= (len(s))):
        new_val = 0
        for count in range(index+1, len(s)):
