# Chapter 6

print("Chapter 6")
print("\n")

summa = 0
for i in range(1,101):
    summa += i
    print(summa)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

summa = 0
for i in range(2,101,2):
    summa += i
print(summa)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

summa = 0
for i in range(1,101):
    summa += 2**i
print(summa)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

luku = 1
ero = 1
for i in range(100):
    print(luku)
    luku += ero
    ero += 1

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

summa = 0
for i in range(1,100,2):
    summa += i
    # print(i)
print(summa)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

summa = 0
for i in range(1,101):
    summa += i**2
    # print(i**2)
print(summa)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

kertoma = 1
for i in range(100,0,-1):
    kertoma = kertoma * i
    # print(num)
print(kertoma)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

summa = 0
for i in range(1,101):
    summa += i**i
print(summa)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

n1 = 0
n2 = 1
summa = 0
print(n1)
print(n2)
for i in range(1,101):
    summa = n1 + n2
    n1 = n2
    n2 = summa
    print(summa)

   

print("-----------------------------")
print("-----------------------------")
print("\n")
###########################
# Chapter 6
print("Chapter 7")
print("\n")

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

for i in range(1,9):
    if i%2 == 1:
        print("pariton",i)
    elif i%2 == 0:
        print("parillinen",i)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

for i in range(0,101):
    if i%3 == 0:
        print("apina")
    else:
        print(i)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

for i in range(1,101):
    if i%2 == 1:
        print(i+1)
    elif i%2 == 0:
        print(i-1)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

for i in range(1,15):
    for j in range(1,i+1):
        print(i)

for i in range(1,101):
    for j in range(1,i+1):
        print(i, end="")
    print()

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

for i in range(1,15):
    for j in range(1,i+1):
        print(j)

for i in range(1,101):
    for j in range(1,i+1):
        print(j, end="")
    print()

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

for i in range(1800,2200):
    if i%4 == 0: 
        print(i)
    elif i%100 == 0 and i%400 == 0:
        print(i)

for i in range(1800,2200):
    if i%100 == 0 and i%400 == 0:
        print(i)

for i in range(1800,2200):
    if i%100 == 0 and i%400 != 0:
        noprint=i
    elif i%4 == 0 and i != noprint: 
        print(i)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

# Chapter 8

print("Chapter 8")
print("\n")
###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

for i in range(1,60):
    if i*(i+1)*(i+2) == 42840:
        print(i, i+1, i+2)

for i in range(1,60):
    if i*(i+1)*(i+2) == 42840:
        print(i)

###########################
print("\n")
# Start a new line
print("-----------------------------")
print("\n")

for x in range(1,100):
    if x + 20 == 3*x:
        print(x)