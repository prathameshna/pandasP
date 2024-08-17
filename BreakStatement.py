for i in  range(12):
    if(i == 10):
        break 
    print("5 X" , i+1, "=",5*(i+1))

print("loop ko chod kei nikal gaya")

for n in range (13):
    if(n == 10):
        print("skip the iteration")
        continue      # continue statement are used to skip the perticular loop
    print("5 X", n, "=", 5*(n+1))
