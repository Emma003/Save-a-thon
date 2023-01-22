#Base calculator functions
#Taxes
#Wage Calculator
#Interest
#Inverse Interest

def calculator_prompt():
    return "$tax VALUE %TAX(optional) --- Will return total cost with tax \n" \
           "$wage AMOUNT FREQUENCY PERIOD(optional) --- Will return wages earned in a month\n" \
           "$interest AMOUNT INTEREST TIME --- Will return the new value after collecting interest over specified TIME \n" \
           "$inv_interest AMOUNT INTEREST GOAL_AMOUNT --- Will return the amount of time until the GOAL_AMOUNT is met"



def calculate_tax(cost, tax_amount=0.14975):
    if tax_amount != 0.14975:
        tax_amount/=100
    return cost + (tax_amount*cost)


def calculate_inverse_tax(income):
    yearly_income = income*12
    tax_rate = 0
    if yearly_income <= 45295:
        tax_rate = 0.15
    elif yearly_income > 45295 and yearly_income <= 92580:
        tax_rate = 0.2
    elif yearly_income > 92580 and yearly_income <= 112655:
        tax_rate = 0.24
    elif yearly_income > 112655:
        tax_rate = 0.2575
    income -= income * tax_rate
    return income

def calculate_wage(amount, frequency, period="default"):
    wage = 0
    if frequency == 'h':
        if period == "default":
            period = 40
        wage = (period * 4) * amount
    if frequency == 'm':
        if period != "default":
            wage = (amount/period)
        else:
            wage = amount
    if frequency == 'y':
        if period != "default":
            wage = (amount/period)/12
        else:
            wage = amount/12
    #wage = calculate_inverse_tax(wage)
    return wage

def calculate_interest(amount, interest, time):
    #interest in years i assume?
    interest /= 100
    yearly_return = amount
    for i in range(time):
        yearly_return += yearly_return * interest
    return yearly_return

def calculate_inverse_interest(amount, interest, goal_amount):
    interest /= 100
    i=0
    while amount<goal_amount:
        amount += amount*interest
        i+=1
    return i
