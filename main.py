import time
x = input("choose from these operacions(+ - * /):")
y = float(input("choose first number:"))
z = float(input("choose second number:"))
if x == "+":
    result = y + z
    print(result)
elif x == "-":
    result = y - z
    print(result)
elif x == "*":
    result = y * z
    print(result)
elif x == "/":
    result = y / z
    print(result)
elif not x =="-" or x =="+" or x =="*" or x =="/":
    print("i said choose from (+ - * /)")

time.sleep(1)
x = "ilia"
x = list('ilia')
print(x)

x = "ilia"
y = "elene"
z = "luka"
res = x + y + z
res = list(res)
print(res)

x = "ilia-go-now"
symbol = "-"
res = x.split(symbol)
print(res)

y = "ilia go now"
res = y.split()
print(res)

z = ["ilia", "go", "now"]
symbol = " "
res = symbol.join(z)
print(res)

x = [1,2,3,4,5]
y = [6,7,8,9]
x.extend(y)
print(x)