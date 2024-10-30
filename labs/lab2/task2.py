def f(x, d):
    n = 1
    sum_series = 0
    term = (x - 1)  

    while abs(term) >= d:
        sum_series += term
        n += 1
        term = ((-1) ** (n + 1)) * (x - 1) ** n / n  

    return sum_series

a = 1.0
b = 1.5
h = 0.05
d = 1e-5

x_values = []
f_values = []

x = a
while x <= b + h / 2:  
    x_values.append(round(x, 2))
    f_values.append(f(x, d))
    x += h
    x = round(x, 2)
    print(x)

print(f"{'x':<10} {'f(x)':<20}")
print("-" * 30)
for x_val, f_val in zip(x_values, f_values):
    print(f"{x_val:<10} {f_val:<20.6f}")
