principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest per annum: "))
time_period = float(input("Enter the time period in years: "))

simple_interest = (principal_amount * rate_of_interest * time_period) / 100
print(f"Principal Amount: {principal_amount}")
print(f"Rate of Interest: {rate_of_interest}")
print(f"Time Period (in years): {time_period}")
print(f"Simple Interest: {simple_interest}")
