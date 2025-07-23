def compound_calculator_with_table():
    while True:
        try:
            initial_investment = float(input("\nEnter your initial investment amount: $"))
            return_rate_percent = float(input("Enter your return rate per period (in %): "))
            num_periods = int(input("Enter the number of compounding periods: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
            continue

        rate = return_rate_percent / 100
        amount = initial_investment

        print(f"\nCompound Growth Table")
        print(f"{'Period':<10}{'Start Amount':<20}{'Interest Earned':<20}{'End Amount':<20}")
        print("-" * 70)

        for period in range(1, num_periods + 1):
            start_amount = amount
            interest = start_amount * rate
            amount = start_amount + interest
            print(f"{period:<10}${start_amount:,.2f}{'':<8}${interest:,.2f}{'':<8}${amount:,.2f}")

        total_profit = amount - initial_investment
        print(f"\nInitial Investment: ${initial_investment:,.2f}")
        print(f"Return per Period: {return_rate_percent:.2f}%")
        print(f"Total Periods: {num_periods}")
        print(f"Final Amount: ${amount:,.2f}")
        print(f"Total Profit: ${total_profit:,.2f}")

        # Ask if user wants to run another calculation
        again = input("\nWould you like to do another calculation? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye! 👋")
            break

# Run the calculator
compound_calculator_with_table()
