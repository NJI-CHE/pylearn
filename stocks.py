import json

def optimize_stock_trading(prices):
    """
    Optimizes stock trading for maximum short-term profit.

    Args:
        prices: A list of integers representing predicted stock prices.

    Returns:
        A list of integers representing buy and sell indices.
    """
    transactions = []
    holding = False

    for i in range(len(prices)):
        if not holding:
            # Check for potential buy
            if i + 1 < len(prices):
                if prices[i + 1] > prices[i]:
                    transactions.append(i)
                    holding = True
        else:
            # Check for potential sell
            if i + 1 < len(prices):
                if prices[i + 1] < prices[i]:
                    transactions.append(i)
                    holding = False
            else:
                # Sell at the last price if holding
                transactions.append(i)
                holding = False

    # Remove trailing buy if any
    if holding and len(transactions)>0:
        transactions.pop()
    
    # Check for consecutive buys and sells that are not profitable
    
    optimized_transactions = []
    
    i = 0
    while i < len(transactions):
        if i + 1 < len(transactions):
            optimized_transactions.append(transactions[i])
            optimized_transactions.append(transactions[i+1])
            i+=2
        else:
            break
            

    return optimized_transactions

# Example usage
input_prices = [108, 45, 216, 215, 213, 96, 167, 245]
result = optimize_stock_trading(input_prices)
print(json.dumps(result))

input_prices2 = [10, 11, 12, 13, 14, 15]
result2 = optimize_stock_trading(input_prices2)
print(json.dumps(result2))

input_prices3 = [15, 14, 13, 12, 11, 10]
result3 = optimize_stock_trading(input_prices3)
print(json.dumps(result3))

input_prices4 = [1,2,3,2,1,2,3,4,3,2,1,2,3,4]
result4 = optimize_stock_trading(input_prices4)
print(json.dumps(result4))