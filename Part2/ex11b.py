def calculate(x,y,z):
    if y == "+" :
        return x + z
    elif y == "-" :
        return x - z
    elif y == "*" :
        return x * z
    elif y == "/" :
        return x / z
    else:
        print("something wrong")

print(calculate(10,"+",10))
print(calculate(10,"-",10))
print(calculate(10,"*",10))
print(calculate(10,"/",10))

