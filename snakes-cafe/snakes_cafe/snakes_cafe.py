from pickle import APPEND


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
order = []
user_input = input("""***********************************
** What would you like to order? **
*********************************** \n< """) 
order.append(user_input)
i= 0
while True:
    for item in order:
        if order[item] == order 
        i += 1
    print('** {} order of {} have been added to your meal **'.format(i, user_input))
    user_input1= input ('<')
    if user_input1== 'quit':
        break 
    
    
    

# if user_input != 'quit':
#     # def user_input ():
#     print('** 1 order of {} have been added to your meal **'.format(user_input))
#     #   user_input = print ('<')
# else :
#     exit
