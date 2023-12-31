![logo](https://github.com/Beexchangeio/Crypto-Staking-Facility/assets/108594892/11d27a25-2075-4029-b57d-fefb4af92e64)

def calculate_roi(principal, interest_rate, duration):
    # Calculate the ROI
    interest = principal * (interest_rate / 100) * duration
    total_amount = principal + interest
    return total_amount

def main():
    principal = float(input("Enter the principal amount: "))
    interest_rate = float(input("Enter the interest rate (%): "))
    duration = float(input("Enter the stacking duration (in years): "))

    # Calculate the ROI
    roi = calculate_roi(principal, interest_rate, duration)

    print("After", duration, "years, the total amount will be:", roi)

if __name__ == "__main__":
    main()
