def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if amount == 0:
        return amount

    counter = 0
    for coin in coins:
        while amount != 0:
            if amount - coin > 0:
                amount -= coin
                counter += 1
            else:
                break
            print(coin, amount)
    if amount == 0:
        return counter
    else:
        return -1

print(coinChange([1, 2, 5], 11))