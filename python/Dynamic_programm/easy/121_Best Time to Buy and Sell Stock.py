"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = float('inf')
    max_profit = 0

    for p in prices:
        # обновляем минимум
        if p < min_price:
            min_price = p

        # считаем прибыль
        profit = p - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit

print(maxProfit([7,1,5,3,6,4]))