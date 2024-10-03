try:
    l = [1, 3, 4, 6]
    i = int(input("the enter the index: "))
    print(l)
except:
    print("Some error occured")
finally:
    print("I am always executed")   