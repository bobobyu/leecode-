class Operations:

    def __init__(self):
        pass

    def minus(self, a: int, b: int) -> int:
        b = bin(eval('0b' + ''.join(['0' if i == '1' else '1' for i in bin(b)[2:]])) + 1)
        b = -1 * eval(b) if b[2] == '1' else eval(b)
        return a + b

    def multiply(self, a: int, b: int) -> int:
        return sum([a for _ in range(b)])

    def divide(self, a: int, b: int) -> int:
        pass


s = Operations()
print(s.multiply(9, 4))
