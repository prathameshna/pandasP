a = input("enter the number: ")
print(f"multiplication table of {a} is: ")

try:
   for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
 print("Invalid input")

print("Some imp lines of code")
print("End of prgoram")

# another type of 