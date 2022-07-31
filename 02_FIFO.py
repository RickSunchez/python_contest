from random import randint

class FIFOIndexes:
    def __init__(self, size:int=256) -> None:
        self.head:int = 0
        self.tail:int = 0
        self.size:int = size
        self.buf:list = [0] * size
        self.isFull:bool = False
        self.isEmpty:bool = True

    def __next(self, val:int) -> int:
        return (val + 1) % self.size

    def put(self, value:int):
        if self.isFull: return

        self.buf[self.head] = value
        self.isFull = self.__next(self.head) == self.tail
        self.isEmpty = False

        if not self.isFull:
            self.head = self.__next(self.head)

    def get(self) -> int:
        if self.isEmpty: return

        val:int = self.buf[self.tail]
        self.buf[self.tail] = 0
        self.isEmpty = self.tail == self.head
        self.isFull = False
        self.tail = self.__next(self.tail)

        return val

class FIFOList:
    def __init__(self, size:int=256) -> None:
        self.buf:list = []
        self.size:int = size
        self.isFull:bool = False
        self.isEmpty:bool = True

    def put(self, val:int):
        if len(self.buf) >= self.size: 
            self.isFull = True
            return

        self.buf.append(val)
        self.isEmpty = False

    def get(self):
        if len(self.buf) == 0:
            self.isEmpty = True
            return

        self.isFull = False
        return self.buf.pop(0)
        
def test(fifo):
    for i in range(99):
        fifo.put(randint(0, 99))

        if i % 6 == 0:
            getCount = randint(1, 6)
            print("\nCheck #%d" % (i // 6))
            print("count:", getCount)

            print("Previous state:")
            print(fifo.buf)

            print("Getted items:", end=" ")

            for j in range(getCount):
                print(fifo.get(), end=" ")

            print()
            print(fifo.buf)

fi = FIFOIndexes(10)
fl = FIFOList(10)

test(fi)
test(fl)
