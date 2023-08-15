from random import randrange

class Item:
    def __init__(self, n, v, w):
        self.name = n;
        self.value = v;
        self.weight = w;

    @property
    def value_rate(self):
        return round(self.value / self.weight, 3);

    def __repr__(self):
        return f"name: {self.name} value: {self.value} weight: {self.weight}, {self.value_rate}"
    

def _create_item(name, max_value, max_weight):
    return (Item(
        name,
        randrange(1, max_value, 1),
        randrange(1, max_weight, 1)
    ));

def create_items(count, max_value, max_weight):
    return ([
        _create_item(f'{i}', max_value, max_weight) for i in range(count)
    ]);


if __name__ == "__main__":
    items = create_items(10, 22, 24);
    [print(item) for item in items];
