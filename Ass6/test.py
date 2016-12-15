class Reverse:
    "Iterator for looping over a sequence backwards"
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        for x in self.data:
            if self.index is 0:
                raise StopIteration
            self.index = self.index - 1
            yield self.data[self.index]

for x in Reverse('spam'):
    print x