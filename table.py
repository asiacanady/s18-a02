#table.py
from Mortgage_Output import mortgage_payment #import the mortgage module


def table(): #define the function table
    home = float(input('Home Price:  ')) #assign variable and create input for home price; change it to a float
    min_payment = int(input('Minimum down Payment:  ')) #assign variable and create input for minimum down payment; change it to an integer
    max_payment = int(input('Maximum down Payment:  ')) #assign variable and create input for minimum down payment; change it to an integer
    interest = float(input('Interest Rate:  ')) #assign variable and create input for imterest rate; change it to a float
    term = float(input('Loan Term (years): ')) ##assign variable and create input for term; change it to an float
    for payment in range(min_payment, max_payment, 1000): #create for loop within the range of min. payment, max. payment in increments of 1000
        loan_amount = home - payment #assign the variable loan amount by subtracting home value from the payment
        monthly_periods= term* 12 #assign the variable monthly periods to term x 12
        interest_rate= ((interest/100)/12) #assign the variable interest_rate to the formula that calculates interest rate
        loan = float(loan_amount) #change loan_amount to loan and change the type to float
        periods = float(monthly_periods) #change monthly_periods to periods and the type to float
        rate = float(interest_rate) #change interest_rate to rate and the type to float
        mortgage = round(mortgage_payment(loan, periods, rate),2) #assign the variable mortgage to the mortgage module and round to the nearest tenth
        print(payment, mortgage) #print both the payment amount and the amount of the the mortgage payment
table() #call the function table
