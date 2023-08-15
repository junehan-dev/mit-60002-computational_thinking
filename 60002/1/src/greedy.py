from collections.abc import Callable

from knapsack import Knapsack
from item import Item, create_items

def greedy(knapsack: Knapsack, items: list[Item], keyFunction: Callable[[Item], int]) -> Knapsack:
    itemsCopy = sorted(items, key = keyFunction, reverse = True);

    for i in range(len(itemsCopy)):
        item = itemsCopy[i]
        knapsack.push(item) if (knapsack.weight + item.weight) <= knapsack.capacity else print(f"OUT:{item}");

    return (knapsack);

def cmp_efficiency(item: Item):
    return item.value_rate

if __name__ == "__main__":
    knapsack = Knapsack(48);
    items = create_items(10, 22, 24);
    [print(i) for i in items]

    greedy_knapsack = greedy(knapsack, items, cmp_efficiency);
    greedy_knapsack.stat()
