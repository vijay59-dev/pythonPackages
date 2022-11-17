from datetime import datetime
import random as r


prices = {"Coffee": 2, "French_Vanilla": 2.5,"Cup_Cake": 1.5, "Croissant": 2}
customer_order = []
customer_satisfied = False
bill_number = ""

total_amount = 0.0

def order_more():
    IsNext_Order = bool(input('Do you like to order something more: '))
    if not IsNext_Order:
        global customer_satisfied
        customer_satisfied = True

def genetrate_bill_number():
   temp_billNumber_list = []
   temp_billNumber = ""
   for i in range(0,15):
       temp_billNumber_list.append(r.randint(0,9))
       temp_billNumber += str(temp_billNumber_list[i])
   return temp_billNumber


while not customer_satisfied:
    order = int(input('Please enter your order \n'
                      ' 1. Coffee\n '
                      '2. Cup Cake\n '
                      '3. Croissant\n '
                      '4. French Vanilla\n '))

    if order in range(1,5):
        customer_order.append('Coffee' if order == 1 else 'Cup_Cake' if order == 2
        else 'Croissant' if order == 3 else 'French_Vanilla'
        if order == 4 else 'please enter valid menu number')
    else:
        print('please enter valid menu number')
        continue

    order_more()


for i in customer_order:
    if i in prices.keys():
        total_amount += prices[i]

TPS = 0.05 * total_amount
TVQ = 0.09975 * total_amount
total_amount_with_taxes = total_amount + TPS + TVQ
bill_number = genetrate_bill_number()

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('***************** TIM HORTONS ****************')
print('        550 sherbrooke, Trebas Insitute       ')
print('               514-842-74915                  ')
print('           '+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+'            ')
print('         Bill Number: '+bill_number+'                      ')
for i in customer_order:
    print(i+'                      '+str(prices[i]))
print('            SUBTOTAL:'+'    '+str(total_amount))
print('            5.0% TPS:'+'    '+str(TPS))
print('          9.975% TVQ:'+'    '+str(TVQ))
print(str(len(customer_order))+' Items'+'          TOTAL:       '+        '$'+str(total_amount_with_taxes))
print('*****Thank You for purchase in Tim Hortons******')
print('*************Bon Journee*************************')