from pickle import APPEND
from re import I


print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")
order = {}
user_input = input("""***********************************
** What would you like to order? **
*********************************** \n< """) 
order[user_input] = 1
if user_input != 'quit':
    print('** 1  order of {} have been added to your meal **'.format( user_input))
else :
    exit
while True:
    user_input= input ('<')
    if user_input== 'quit':
        break 
    else:
            if user_input in order:
                    order[user_input] += 1
            else:
                order[user_input] = 1
            print('** {} order of {} have been added to your meal **'.format(  order[user_input],user_input))
            # print(order)

# if user_input != 'quit':
#     # def user_input ():
#     print('** 1 order of {} have been added to your meal **'.format(user_input))
#     #   user_input = print ('<')
# else :
#     exit
# order = {}
# user_input = input("""***********************************
# ** What would you like to order? **
# *********************************** \n< """) 
# order[user_input]
# while True:
#     print('** 1 order of {} have been added to your meal **'.format( user_input))
#     user_input1= input ('<')
#     if user_input1== 'quit':
#         break 
#     else:
#         order.append(user_input1)
#         # while (i <= len (order)):
#         #     if 
#         for i in range (len(order)):
#             for j in range (len(order)):
#                 if order [i] == order [j+1]:
#                     i+=1
#                     print('**  order of {} have been added to your meal **'.format( i ,user_input1))
#                     break
                