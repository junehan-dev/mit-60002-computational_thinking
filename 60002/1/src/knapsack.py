from item import create_items 

class Knapsack:
    def __init__(self, capacity):
        self.data = [];
        self.capacity = capacity;
        self.weight = 0;
        self.value = 0;
    def __str__(self):
        return f"weight:{self.weight}/{self.capacity}, value:{self.value}";

    def __push__(self, item):
        self.data.append(item);
        self.weight += item.weight;
        self.value += item.value;
        return 1;

    def push(self, item):
        return 0 if (self.weight + item.weight) > self.capacity else self.__push__(item);

    def pop(self):
        self.data.pop();
        return None;

    def stat(self):
        print(self.data);
        return None;

    def __gt__(self, k):
        return self.value > k.value;

    def __lt__(self, k):
        return self.value < k.value;

    def __eq__(self, k):
        return self.value == k.value;


def greedy(knapsack, items):
    pass;

if __name__ == "__main__":
    knapsack = Knapsack(48);
    items = create_items(10, 22, 24);
    [print(i) for i in items]

