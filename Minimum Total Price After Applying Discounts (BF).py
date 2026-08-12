class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        total = 0

        for price, discount in zip(prices, discounts):
            total += price * (100 - discount) / 100

        total += sum(prices[len(discounts):])
        return total