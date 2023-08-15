from collections.abc import Callable

from knapsack import Knapsack
from item import Item, create_items

def greedy(knapsack: Knapsack, items: list[Item], keyFunction: Callable[[Item], int]) -> Knapsack:
    itemsCopy = sorted(items, key = keyFunction, reverse = True);

    for i in range(len(itemsCopy)):
        item = itemsCopy[i];
        if (knapsack.weight + item.weight) <= knapsack.capacity:
            knapsack.push(item);

    return (knapsack);

def cmp_value_rate(item: Item):
    return (item.value_rate);

def cmp_value_priority(item: Item):
    return (item.value);

def cmp_weight_efficiency(item: Item):
    return (1/item.weight);

def test_greedys(max_units):
    if (max_units < 1):
        return 0;

    # create knapsack
    knapsack = Knapsack(max_units * 100);
    max_value = 100;
    max_weight = max_units * 40; 
    # create items
    items = create_items(max_units, max_value, max_weight);
    [print(i) for i in items];
    # run greedy by value priority
    print("Use greedy by value to allocate", max_units, "items\n");
    greedy_knapsack = greedy(knapsack, items, cmp_value_priority);
    greedy_knapsack.stat();
    # run greedy by weight priority
    print("Use greedy by weight cost to allocate", max_units, "items\n");
    greedy_knapsack = greedy(knapsack, items, cmp_weight_efficiency);
    greedy_knapsack.stat();
    # run greedy by value_rate(density)
    print("Use greedy by value_rate to allocate", max_units, "items\n");
    greedy_knapsack = greedy(knapsack, items, cmp_value_rate);
    greedy_knapsack.stat();

if __name__ == "__main__":
    test_greedys(100);
