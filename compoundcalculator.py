def compound_calculator_with_table(initial_investment, return_rate_percent, num_periods):
    rate = return_rate_percent / 100
    amount = initial_investment

    print(f"\nCompound Growth Table")
    print(f"{'Period':<10}{'Start Amount':<20}{'Interest Earned':<20}{'End Amount':<20}")
    print("-" * 70)

    for period in range(1, num_periods + 1):
        start_amount = amount
        interest = start_amount * rate
        amount = start_amount + interest
        print(f"{period:<10}{start_amount:,.2f}<{' ':<10}{interest:,.2f}<{' ':<10}{amount:,.2f}")

    total_profit = amount - initial_investment
    print(f"\nInitial Investment: ${initial_investment:,.2f}")
    print(f"Return per Period: {return_rate_percent:.2f}%")
    print(f"Total Periods: {num_periods}")
    print(f"Final Amount: ${amount:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")

# Example usage:
compound_calculator_with_table(
    initial_investment=800,        # Enter initial investment
    return_rate_percent=10,        # % return per period
    num_periods=12                 # Number of compounding periods
)
