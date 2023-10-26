# Refactor the discount program using the match_case statement

# If the customer is part of the loyalty program and spent over $100, a discount of 20% is applied
# If the customer is not part of the loyalty program but spent over $100, a discount of 10% is applied
# If the customer is not part of the loyalty program and did not spend over $100, a service charge of 5% is applied

loyalty_program = False
bill_total = 10

match (loyalty_program, bill_total > 100):
    case True, True:
        print("Customer is in the loyalty program and spent over $100")
        bill_total = bill_total - (0.2 * bill_total)
    case False, True:
        print("Customer is not in the loyalty program but spent over $100")
        bill_total = bill_total - (0.1 * bill_total)
    case True, False:
        print("Customer is in the loyalty program but did not spend over $100")
        bill_total = bill_total - (0.1 * bill_total)
    case _:
        print("Customer is not in the loyalty program and did not spend over $100")
        print("5% Service Charge Applies")
        bill_total = bill_total + (0.05 * bill_total)
        
        
print(f"The customer's total bill is: {str(bill_total)}")