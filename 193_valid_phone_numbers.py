from typing import List


def maxProfit(self, prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0          

    for preco in prices:
        if preco < min_price:
            min_price = preco
        elif preco - min_price > max_profit:
            max_profit = preco - min_price

    return max_profit
