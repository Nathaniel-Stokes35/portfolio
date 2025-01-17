import datetime
import os

keep_going = True
add_text = ''

def calculate_total(value):
    global keep_going
    discount = 0
    if value == 0:
        keep_going = False
        return
    weekday = now.weekday()
    if (value > 50 and weekday in [1, 2]):
        discount = 0.1
        add_text = f'Discount: {discount * 100}%{os.linesep}Discount amount: {(value * discount):.2f}'
    elif (weekday in [1, 2]):
        add_text = f'Purchasing ${(50 - value):.2f} would allow you a 10% discount'
    else:
        discount = 0
    total = (value * (1 - discount))* 1.06 #discount times 6% sales tax
    tax = value * 0.06
    print(f'Sales Tax Amount: {tax:.2f}{os.linesep}Total: ${total:.2f}{os.linesep}' + add_text)

while keep_going == True:
    now = datetime.datetime.now()
    dow = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    value = input('Please present your subtotal: ')
    value = float(value)
    calculate_total(value)