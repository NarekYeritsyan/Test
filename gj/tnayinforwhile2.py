# N76
# word = input('Enter a word: ').lower()
# filtr = ''

# for i in word:
#     if i.isalnum():
#         filtr += i




# for i in range(len(word) // 2):
#     if filtr[i] != filtr[len(filtr) - 1 - i]:
#         print('Not polidrom')
#         break
# else:
#     print('Polidrom')


# N77
# print(' ', end='\t')
# for i in range(1, 11):
#     print(i, end='\t')
# print() 

# for i in range(1, 11):
#     print(i, end='\t')  
#     for j in range(1, 11):
#         res = i * j
#         print(res, end='\t')
#     print()  



# N78
# number = int(input('Enter a number: '))

# while number > 1:
#     if number % 2 == 0:
#         number = number // 2
#     else: 
#         number = 3 * number + 1
#     print(number)


# N79
# n = int(input('Enter first number: '))
# m = int(input('Enter second number: '))
# d = min(n, m)

# while n % d != 0 or m % d != 0:
#     d -= 1

# print(d)



# N80
# n = int(input('Enter a number: '))
# factor = 2
# while factor <= n:
#     if n % factor == 0:
#         save = factor
#         n = n // factor
#     else:
#         factor += 1
#     print(factor)


# N81
# N82

# N83
# import random
# ran = random.randint(1, 100)
# max = ran
# count = 0

# print(max)

# for i in range(99):
#     ran2 = random.randint(1, 100)
#     if ran2 > max:
#         max = ran2
#         count += 1
#         print(f'{max} <== Tarmacum')
#     else:
#         print(ran2)

# print(f'Amenamec tivy: {max}')
# print(f'Tarmacumneri qanaky: {count}')



# N84
# import random

# krknel = 10

# for i in range(krknel):
#     o = 0
#     p = 0
    
#     while p < 3 and o < 3:
#         ran = random.randint(1, 2)
#         if ran == 1:
#             o += 1
#             print('O', end=' ')
#         elif ran == 2:
#             p += 1
#             print('P', end=' ')
    
#     print(f"(Porceri qanaky: {o + p})")

        
        
            
