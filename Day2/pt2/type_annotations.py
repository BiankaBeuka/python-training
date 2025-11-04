"""
Type hint examples
(Python 3.10+)

1. implement the function
"""

from typing import Any, Literal

Fruit = Literal["apple", "pear", "cantaloupe"]
FruitBasket = set[Fruit]
Basket = set[Any]

FruitPrices = dict[Fruit, float]

PRICES: FruitPrices = {
    "apple": 1.23,
    "pear": 4.56,
    "cantaloupe": 7.89,
    "watermelon": 12.34,  # type: ignore
}


def calc_total_price(basket: Basket, prices: FruitPrices) -> float:
    return sum(prices[item] for item in basket if item in prices)


basket = {"apple", "cantaloupe"}
print(calc_total_price(basket=basket, prices=PRICES))  # should print 9.12
