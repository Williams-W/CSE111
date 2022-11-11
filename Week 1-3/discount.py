import datetime 
import math 

sub = float(input("Please enter the subtotal: $"))

#day_of_week = datetime.datetime.today().isoweekday()
day_of_week = 2

if sub >= 50 and (day_of_week == 2 or day_of_week == 3):
        discount = round(float(sub - sub * .9),2)
        sub_new = round(float(sub - discount),2)
        tax = round(float(sub_new * .06),2)
        total= round(float(sub_new + tax),2)
        print(f"Discount: ${discount:.2f} \nSales tax amount: ${tax:.2f} \nTotal: ${total:.2f}")

elif sub < 50 and (day_of_week == 2 or day_of_week == 3):
        tax = round(float(sub * .06),2)
        total = round(float(sub + tax), 2)
        needed = float(50 - sub)
        print(f"Sales tax amount: ${tax:.2f} \nTotal: ${total:.2f}")
        print(f"No discount. Short ${needed:.2f}")

else:
        tax = round(float(sub * .06),2)
        total = round(float(sub + tax), 2)
        print(f"Sales tax amount: ${tax:.2f} \nTotal: ${total:.2f}")