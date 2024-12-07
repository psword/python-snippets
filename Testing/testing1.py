# a = input(")
# a = sorted(a)
# a = ''.join(a)
# print(a)

# a = int(input())
# b = int(input())
# c = a + b
# print(a,'+',b,'is',c)
# c = a - b
# print(a,'-',b,'is',c)
# c = a * b
# print(a,'*',b,'is',c)
# c = a / b
# print(a,'/',b,'is',c)
# c = a % b
# print(a,'%',b,'is',c)
# c = a ** b
# print(a,'^',b,'is',c)

# n = int(input())
# a = {}

# for i in range(n):
#     b = i+1
#     a.update({
#         b:b**2
#         })

# print(a)

# n = abs(int(input()))
# b = n * (n + 1) // 2
# print("The sum of the first " + str(n) + " positive integers is {0:d}".format(b)) 

# a = str(input())
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# b = []

# for letters in a:
#     if letters in vowels:
#         b.append(letters)

# print("Number of vowels:",len(b))


# n = 1
# b = 0
# while True:
#     n = input()

#     try:
#         n = int(n)
#     except ValueError: 
#         print("That wasn’t a number.")
#         continue

#     if n == 0:
#         break
#     else:
#         b += n
#         print("The total is now {:.1f}".format(b))

# print ("The grand total is {:.1f}".format(b))


# def custom_encoder(a):
#     reference_string = 'abcdefghijklmnopqrstuvwxyz'
#     temp = []
#     a = a.lower()
#     for char in a:
#         b = reference_string.find(char)
#         temp.append(b)
#     # print(temp)    
#     return temp

# custom_encoder("test!")

# class Person:
#     def __init__(self, name):
#         self.name = name
#         pass

#     def hello(self):
#         print('Hello, my name is',self.name)
#         pass

# p = Person('Matti')
# p.hello()

# class Restaurant:
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine_type = cuisine
#         pass

#     def describe_restaurant(self):
#         print(self.name + " serves wonderful " + self.cuisine_type + ".")
#         pass

#     def open_restaurant(self):
#         print(self.name,"is open. Come on in!")
#         pass

# r = Restaurant('Bistro', 'French')
# print(r.name)
# print(r.cuisine_type)
# r.describe_resaurant()
# r.open_restaurant()

# class User:
#     def __init__(self,first_name,last_name,username,email,location):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.email = email
#         self.location = location
#         pass

#     def describe_user(self):
#         print("Name:", self.first_name, self.last_name)
#         print("Username:", self.username)
#         print("Email:", self.email)
#         print("Location:", self.location)
#         pass

#     def greet_user(self):
#         print("Welcome back " + self.username + "!")
#         pass

# Matti= User('Matti', 'Paajanen', 'mpaajanen', 'm.paajanen@gmail.com', 'Helsinki')
# Matti.describe_user()

# Maila= User('Maila', 'Halonen', 'm_halonen', 'm.halonen@mtv.fi', 'Vaasa')
# Maila.greet_user()

# def combine_lists(list_a,list_b):
#     # list_a = [1, 3, 5, 7, 9]
#     # list_b = [0, 2, 4, 6, 8]

#     size_list_a = len(list_a)
#     size_list_b = len(list_b)
#     list_result = []
#     i, j = 0, 0

#     while i < size_list_a and j < size_list_b:
#         if list_a[i] < list_b[j]:
#             list_result.append(list_a[i])
#             i += 1
#         else:
#             list_result.append(list_b[j])
#             j += 1
#     # print(list_a[i:])
#     # print(list_b[j:])
#     list_result = list_result + list_a[i:] + list_b[j:]
#     return list_result

# print(combine_lists([1, 3, 5, 7, 9],[0, 2, 4, 6, 8]))