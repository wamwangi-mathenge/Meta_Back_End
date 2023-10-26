# Let's say you want to give a certain discount to customers if they spend over $100.
# You will also provide an extra discount if that customer is part of a loyalty program.
# If the customer is part of the loyalty program and spent over $100, a discount of 20% is applied
# If the customer is not part of the loyalty program but spent over $100, a discount of 10% is applied
# If the customer is not part of the loyalty program and did not spend over $100, a service charge of 5% is applied



bill_total = 120
loyalty_program = True

if loyalty_program and bill_total > 100:
    print("Customer is part of the loyalty program and spent over $100")
    bill_total = bill_total - (0.2 * bill_total)
elif loyalty_program == False and bill_total > 100:
    print("Customer is not part of the loyalty program but spent over $100")
    bill_total = bill_total - (0.1 * bill_total)
else:
    print("Customer is not part of the loyalty program and did not spend over $100")
    bill_total = bill_total + (0.05 * bill_total)
    
    
print(f"Your total bill is {str(bill_total)}")