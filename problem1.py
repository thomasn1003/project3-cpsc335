def coin_change(coins, amount):
    # Initialize dp array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # Populate dp array using the coins
    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)

    # Check if it's possible to form the amount
    return dp[amount] if dp[amount] != float('inf') else -1

def main():
    # Take input from the user
    coins = list(map(int, input("Enter the coin denominations (space-separated): ").split()))
    amount = int(input("Enter the amount: "))

    # Call the coin_change function
    result = coin_change(coins, amount)

    # Output the result
    print(f"Output: {result}")

# Run the program
if __name__ == "__main__":
    main()
