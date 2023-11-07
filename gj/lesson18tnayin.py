# N85
# from math import sqrt
# def triangle(a,b):
#     c = sqrt(a ** 2 + b ** 2)
#     return c

# a = float(input('Enter the lenght of first side: '))
# b = float(input('Enter the lenght of second side: '))
# print(triangle(a,b))

# N86
# tarif = 4
# m140 = 0.25
# def taxi(d):
#     c = d * 1000
#     b = c / 140
#     total = tarif + b * m140
#     total = round(total, 2)
#     return total

# d = float(input('Enter a distance(km): '))
# print(taxi(d))


# N87
# def delivery(s):
#     total = 10.95 + (s - 1) * 2.95
#     return total

# s = int(input('Enter the count of products: '))
# print(delivery(s))




# N88
# def median(a, b, c):
#     if a <= b <= c or c <= b <= a:
#         return b
#     elif b <= a <= c or c <= a <= b:
#         return a
#     else:
#         return c

# n1 = int(input('Enter first number: '))
# n2 = int(input('Enter second number: '))
# n3 = int(input('Enter third number: '))
# print(median(n1, n2, n3))



# N89

# def get_ordinal_number(number):
#     ordinals = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
    
#     if 1 <= number <= 12:
#         return ordinals[number - 1]
#     else:
#         return ""
    
# print(get_ordinal_number(5))



# N91
# def ordinal_date(d, m, y):
#     leap = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
#     days = (31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

#     month_days = d
#     for i in range(m - 1):
#         month_days += days[i]
    
#     return month_days

# day = int(input("Enter the day (1-31): "))
# month = int(input("Enter the month (1-12): "))
# year = int(input("Enter the year: "))
# print(ordinal_date(day, month, year))


# N92


# N93
# def centre(s, w):
#     if len(s) >= w:
#         return s
#     pad = (w - len(s)) // 2
#     return " " * pad + s

# s = input('Enter a word: ')
# w = int(input('Enter a width: '))
# print(centre(s, w))


# N94
# def triangle(a, b, c):
#     if a + b < c or a + c < b or b + c < a:
#         return False
#     else:
#         return True
    
# a = float(input('Enter the length of the first line: '))
# b = float(input('Enter the length of the second line: '))
# c = float(input('Enter the length of the third line: '))
# print(triangle(a,b,c))


