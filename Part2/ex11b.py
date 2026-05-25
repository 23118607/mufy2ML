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