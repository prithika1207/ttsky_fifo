class FIFO:
    def __init__(self, depth=4):
        self.depth = depth
        self.mem = []

    def write(self, data):
        if len(self.mem) < self.depth:
            self.mem.append(data)
            return True
        return False  # full

    def read(self):
        if len(self.mem) > 0:
            return self.mem.pop(0)
        return None  # empty


# -------- TEST --------
fifo = FIFO(depth=4)

print("Write test:")
for i in [10, 20, 30, 40, 50]:
    print(i, "->", fifo.write(i))  # last one should fail

print("\nRead test:")
for _ in range(5):
    print(fifo.read())
