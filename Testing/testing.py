num1 = 0
num2 = 1
fibbonacci = 0
for i in range(0,101):
    print("fibonacci sum")
    print(num1)
    fibbonacci = num1 + num2
    num1 = num2
    num2 = fibbonacci

luku = 1
luku1 = 100
for i in range(50):
    print(luku + i)
    print(luku1 - i)

for i in range(1,9):
    print("#"*i)

print("#"*10)
for i in range(10):
    print("#")
print("#"*10)

for i in range (10):
    print(" "*(5-i) + "#"*i + " "*(5-i))