"""

1- "Create variables for the following information of a customer.
    Customer Name
    Customer Surname
    Customer Name + Surname
    Customer Gender
    Customer Turkish ID Number
    Customer Birth Year
    Customer Address
    Customer Age

"""
from datetime import datetime

customerName = 'Nurdan'
customerSurname = 'Kolay'
CustomerNameSurname = customerName + ' ' + customerSurname
customerGender = True # Female
customerIdNum = '12345678912'
customerBirthYear = 1993
customerAddress = 'Istanbul Turkiye'
customerAge = datetime.now().year - customerBirthYear

"""

2- Calculate the total amount of the following orders.
    order1 => 110 TL
    order2 => 1100.5 TL
    order3 => 356.95 TL

""" 

order1 = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3
print(total)

