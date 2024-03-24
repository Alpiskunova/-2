import numpy as np

class SegmentTree:
    def __init__(self, data, func=lambda a, b: a + b, neutral_element=0):
        self.data = data
        self._func = func
        self.neutral_element = neutral_element
        self.build_tree()

    def build_tree(self):
        ln = len(self.data)
        lb = np.log2(ln)
        if lb == int(lb):
            self.neutral_element = 0
        else:
            lb = int(lb) + 1
            self.data.extend([0] * (2**lb - ln))
        self.tree = [0] * (2 * len(self.data))
        self._size = len(self.data)
        self.calc_tree()

    def calc_tree(self):
        for i in range(len(self.tree) - 1, 1, -2):
            self.tree[(i - 1) // 2] = self._func(self.tree[i - 1], self.tree[i])

    def query(self, start, stop):
        start += self._size
        stop += self._size + 1
        res_left = res_right = self.neutral_element
        while start < stop:
            if start % 2 == 1:
                res_left = self._func(res_left, self.tree[start])
                start += 1
            if stop % 2 == 1:
                stop -= 1
                res_right = self._func(self.tree[stop], res_right)
            start //= 2
            stop //= 2
        return self._func(res_left, res_right)

    def __getitem__(self, idx):
        return self.data[idx]

    def update(self, index, new_item):
        if len(self.data) == len(self.tree) // 2:
            self.data[index] = new_item
            self.build_tree()
        else:
            del self.data[-len(self.data) + len(self.tree) // 2:]
            self.data[index] = new_item
            self.build_tree()

tree = SegmentTree([1, 2, 3, 4, 5, 6, 7, 8])
print(tree.data)

print(tree.query(0, 7))

print(tree.tree)
print(tree.data)

tree.update(2, 45)

print(tree.data)
print(tree.tree)


