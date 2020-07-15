x = str(input("строка\n"))
a = list(x) 
a.reverse()
y = "".join(a)

if x == y:
    print("true")
else: 
    print("false")

