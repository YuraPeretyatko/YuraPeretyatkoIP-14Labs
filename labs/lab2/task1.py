import math

def func1(x):
    return 1 / math.cos(x ** 2)

def func2(x):
    return math.cos(math.sin(x))

def func3(x):
    return math.sin(1 / math.cos(x))

def tabulate_func(func_index, a, b, h):
    x_values = []
    results = []

    x = a
    while x <= b:
        x_values.append(x)
        if func_index == 1:
            y = func1(x)
        elif func_index == 2:
            y = func2(x)
        elif func_index == 3:
            y = func3(x)
        else:
            raise ValueError("неправильний індекс функції")
        
        results.append((x, y))
        x += h
        x = round(x, 2)
        

    return results


a = 0.3
b = 0.9
h = 0.05
func_index = 1

table = tabulate_func(func_index, a, b, h)

print("x\t\ty")
for x, y in table:
    print(f"{x}\t{y:.5f}")