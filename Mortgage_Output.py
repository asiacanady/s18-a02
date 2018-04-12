def mortgage_payment(loan, periods, rate): #define the function
    result = (rate * loan) / (1-(1+rate)**(-1 * periods)) #assign the variable result
    return result #return result
