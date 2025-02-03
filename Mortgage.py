def mortgage_payments(principal, rate, amortization):
    # Convert rate from percent to decimal
    rq = rate / 100
    
    # Calculate the number of periods
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52
    
    # Calculate periodic interest rates
    r_monthly = (1 + rq / 2) ** (2/12) - 1
    r_semi_monthly = (1 + rq / 2) ** (2/24) - 1
    r_bi_weekly = (1 + rq / 2) ** (2/26) - 1
    r_weekly = (1 + rq / 2) ** (2/52) - 1
    
    # Present Value of Annuity Factor (PVA)
    def pva(r, n):
        return (1 - (1 + r) ** -n) / r
    
    # Calculate payments
    monthly_payment = principal / pva(r_monthly, n_monthly)
    semi_monthly_payment = principal / pva(r_semi_monthly, n_semi_monthly)
    bi_weekly_payment = principal / pva(r_bi_weekly, n_bi_weekly)
    weekly_payment = principal / pva(r_weekly, n_weekly)
    
    # Rapid payments (extra payments per year)
    rapid_bi_weekly_payment = bi_weekly_payment * 26 / 24
    rapid_weekly_payment = weekly_payment * 52 / 48
    
    return (monthly_payment, semi_monthly_payment, bi_weekly_payment, weekly_payment, rapid_bi_weekly_payment, rapid_weekly_payment)

# Set predefined principal amount
principal = 500000
rate = 5.5
amortization = 25

# Calculate payments
payments = mortgage_payments(principal, rate, amortization)

# Display results
print("\nMortgage Payments:")
print(f"Monthly Payment: ${payments[0]:,.2f}")
print(f"Semi-Monthly Payment: ${payments[1]:,.2f}")
print(f"Bi-Weekly Payment: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Rapid Bi-Weekly Payment: ${payments[4]:,.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:,.2f}")
