countries = ("spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "finland"
countries = tuple(temp)
print(countries)

tp1 = (1, 3, 5, 6, 7, 4, 3, 6, 3, 7, 6)
res1 = tp1.count(3)
print("Count of 6 in tuple is:",res1)