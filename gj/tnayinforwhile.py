# N66

# total = 0
# cash = 0

# while True:
#     price = input('Grel apranqi arjeqy(kam bac toxnel): ')
    
#     if not price:
#         break
    
#     if price.replace('.', '', 1).isdigit():
#         price = float(price)
#         total += price  
#     else:
#         print('Error')

# print(f'Yndhanur: {total:.2f}$')


# cents = int(total * 100) % 5
# if cents < 2.5:
#     cash = total - (cents / 100)
# else:
#     cash = total + (0.05 - (cents / 100))

# print(f'Kanxik vcharum: {cash:.2f}$')


# N68
# count = 0
# score = 0
# while True:
#     gnahatakan = input('Grel tvayin gnahatakany: ')

#     if not gnahatakan:
#         break

#     if gnahatakan == 'A+':
#         score = 4.0
#     elif gnahatakan == 'A':
#         score = 4.0
#     elif gnahatakan == 'A-':
#         score = 3.7
#     elif gnahatakan == 'B+':
#         score = 3.3
#     elif gnahatakan == 'B':
#         score = 3.0
#     elif gnahatakan == 'B-':
#         score = 2.7
#     elif gnahatakan == 'C+':
#         score = 2.3
#     elif gnahatakan == 'C':
#         score = 2.0
#     elif gnahatakan == 'C-':
#         score = 1.7
#     elif gnahatakan == 'D+':
#         score = 1.3
#     elif gnahatakan == 'D':
#         score = 1.0
#     elif gnahatakan == 'F':
#         score = 0.0

#     count += 1

# if count > 0:
#     michin = score / count
#     print(f'Michin gnahantakany: {michin:.1f}')
# else:
#     print('Duq cheq grel gnahatak')


