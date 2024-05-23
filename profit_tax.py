# Define the parameters
daily_profit_rate = 0.01  # 1% daily profit
tax_rate = 0.15  # 15% tax rate
days_in_month = 20

# Calculate the daily net profit rate after tax
daily_net_profit_rate = daily_profit_rate * (1 - tax_rate)

# Calculate the monthly net profit rate with daily compounding
monthly_net_profit_rate = (1 + daily_net_profit_rate) ** days_in_month - 1

# Convert to percentage
monthly_net_profit_percentage = monthly_net_profit_rate * 100

# Print the result
print(f"The monthly return percentage is approximately {monthly_net_profit_percentage:.4f}%")
