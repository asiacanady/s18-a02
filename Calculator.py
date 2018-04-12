#calculator.py
from Mortgage_Output import mortgage_payment #import the mortgage module

def calculator(): #define the function
    home = float(input('Home Price:  ')) #create input for home price; change it to a float
    payment = float(input('Down Payment:  '))#create input for  change it to a float
    interest = float(input('Interest Rate:  ')) #create input for interest rate; change it to a float
    term = float(input('Loan Term (years): ')) #create input for loan terms; change it to a float
    print('\nYour Loan Amount Is...') #print 'Your Loan Amount Is' with a break
    loan_amount = home - payment #assign loan amount
    print('>>>',loan_amount) #print loan amount with '>>>'
    print('\nThe Number of Months in Your Loan...') #print 'The Number of Months in Your Loan'
    monthly_periods= (term * 12) #assign monthly periods
    print('>>>', monthly_periods) #print monthly periods with break '>>>'
    print('\nYour Monthly Interest Rate Is...') #print
    interest_rate= ((interest/100)/12) #assign the variable interest rate by take interest rate and divide it by 12
    print('>>>',interest_rate) #print the statement
    loan = int(loan_amount) #assign the variable loan and turn it into an interest rate
    periods = float(monthly_periods) #assign variable periods. Keep as float
    rate = float(interest_rate) #assign the variable rate and assign as float
    print('\nYour Mortgage Payment Is...') #print with a break
    mortgage = round(mortgage_payment(loan, periods, rate),2) #assign the variable mortgage to the mortgage module and round to the nearest tenth
    print(mortgage) #print variable mortgage
calculator() #call the function calculator
