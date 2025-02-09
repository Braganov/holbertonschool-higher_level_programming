class CountedIterator:
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item
