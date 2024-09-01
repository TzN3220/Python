import OverflowError as o, UnderflowError as u

class Stack:
    def __init__(self,maxSize):
        self.arr = []
        self.maxSize = maxSize
        self.size = 0

    def push(self, x):
        if self.size < self.maxSize:
            self.arr.append(x)
            self.size += 1
        else:
            raise o.OverflowError("The stack is full")

    def pop(self):
        if self.isEmpty():
            raise u.UnderflowError("The stack is empty")
        else:
            self.size -= 1
            return self.arr.pop()

    def isEmpty(self):
        return len(self.arr) == 0


def main():
    s=Stack(5)

if __name__ == "__main__":
    main()