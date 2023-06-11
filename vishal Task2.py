def calculate_emi(principal, tenure, interest_rate):
    monthly_interest_rate = interest_rate / (12 * 100)
    total_emis = tenure * 12
    emi_amount = (principal * monthly_interest_rate * (1 + monthly_interest_rate) * total_emis) / ((1 + monthly_interest_rate) * total_emis - 1)
    
    return round(emi_amount, 2)

def print_emis(principal, tenure, interest_rate):
    emi_amount = calculate_emi(principal, tenure, interest_rate)
    
    print('Principal amount:', principal)
    print('Tenure:', tenure)
    print('Interest Rate:', interest_rate)
    print('---------------------------------------')
    
    balance = principal
    total_payment = 0
    monthly_emi = float(emi_amount)
    
    for i in range(tenure * 12):
        interest_payment = balance * (interest_rate / (12 * 100))
        principal_payment = monthly_emi - interest_payment
        balance -= principal_payment
        total_payment += monthly_emi
        
        months = ['jan','Feb','march', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','oct','Nov.', 'Dec']
        month = months[i % 12]
        
        print(f'E2023 {month}')
        print(f'Principal (A): €{balance:.2f}')
        print(f'Total Payment (A + B): €{total_payment:.2f}')
        print('---------------------------------------')

# Example usage
principal = 100000
tenure = 5
interest_rate = 10

print_emis(principal, tenure, interest_rate)