#search.py
import Mortgage_Output

home = float(input('Home Price:  ')) #create input for home price; change it to a float
payment = int(input('Desired Montly Payment:  '))#create input for  change it to a float
interest = float(input('Interest Rate:  ')) #create input for interest rate; change it to a float
term = float(input('Loan Term (years): ')) #create input for loan terms; change it to a float

a = 0 #assign a to 0
b = home #assign b to home. This is important because any home value can use this calculator
term_months=term*12 #assign the loan term in the number of months
interest_rate=(interest/100)/12 #assign the interest rate in the number of loops

while True:
    c = (a + b)/2
    Fc = Mortgage_Output.mortgage_payment(home-c, term_months, interest_rate) #assign Fc to the mortgage module
    if abs(Fc - payment) < .01: #set the conditon that if Fc minus the desired monthly payment to less than .01 (as close to zero)
        break #
    elif Fc < payment: #this needs to be desired monthly payment
            b = c #replace interval with home value = mortgage payment. (left half)
    else:
            a = c #replace interval with 0 = mortgage payment. (right half)
print(round(c),2) #print the statement
