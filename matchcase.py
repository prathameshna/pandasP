x = int(input("enter a number x: ")) 
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _:
        # _ this sign represent the default case.
        print(x)