# in python,we can raise custom errors by using the raise keyword
a = int(input("Enter number between 5 or 9"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9") 

# for more custom error visit https://docs.python.org/3/library/exceptions.html.

