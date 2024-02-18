def calculate_compound_interest(principal, rate, time):

    compound_interest = principal * (pow((1 + rate / 100), time)) - principal
    return compound_interest
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest per annum: "))
time_period = float(input("Enter the time period in years: "))

interest_result = calculate_compound_interest(principal_amount, rate_of_interest, time_period)

print(f"Principal Amount: {principal_amount}")
print(f"Rate of Interest: {rate_of_interest}")
print(f"Time Period (in years): {time_period}")
print(f"Compound Interest: {interest_result}")
