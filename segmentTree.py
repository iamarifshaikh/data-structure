class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, left, right):
        if left == right:
            self.tree[node] = nums[left]
            return
        mid = (left + right) // 2
        self.build(nums, 2 * node + 1, left, mid)
        self.build(nums, 2 * node + 2, mid + 1, right)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, left, right, l, r):

        if r < left or l > right:
            return 0

        if l <= left and right <= r:
            return self.tree[node]

        mid = (left + right) // 2
        left_sum = self._query(2 * node + 1, left, mid, l, r)
        right_sum = self._query(2 * node + 2, mid + 1, right, l, r)
        return left_sum + right_sum

    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, left, right, index, value):
        if left == right:
            self.tree[node] = value
            return
        mid = (left + right) // 2
        if index <= mid:
            self._update(2 * node + 1, left, mid, index, value)
        else:
            self._update(2 * node + 2, mid + 1, right, index, value)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

nums = [1, 2, 3, 4]
seg_tree = SegmentTree(nums)
print("Segment Tree array after build:")
print(seg_tree.tree)

print(seg_tree.query(1, 3))

seg_tree.update(2, 10)     
print(seg_tree.query(1, 3)) 
