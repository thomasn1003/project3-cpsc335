def coin_change(coins, amount):
    # Initialize array
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Base case: 0 coins needed for amount 0

    
    for coin in coins:
        for value in range(coin, amount + 1):
            min_coins[value] = min(min_coins[value], min_coins[value - coin] + 1)

    # Check if it's possible to form the amount
    return min_coins[amount] if min_coins[amount] != float('inf') else -1

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
