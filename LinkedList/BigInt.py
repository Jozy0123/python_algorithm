from llist import LList, LNode, LinkedListUnderFLow, LinkedListOverFLow

class Digit(LNode):
    def __init__(self, elem, next_ = None, digit10Exponential = 0):
        LNode.__init__(self, elem, next_)
        self.digit10Exponential = digit10Exponential

class BigInt(LList):
    """
    The element in every node should be an integer between 0 and 9 (inclusive). 
    """
    @staticmethod
    def digit_add(m = 0, n = 0, last_digit = 0):
        return (m + n + last_digit)%10, (m + n + last_digit) > 9

    def __init__(self, digits = 0):
        LList.__init__(self)
        self._digits = 0

    def prepend(self, n):
        if not isinstance(n, int) or n < 0 or n > 9:
            raise LinkedListOverFLow("digit must be number and must be between 0-9")
        self._head = Digit(n, self._head, self._digits + 1)

    def __add__(self, another):
        self.rev()
        another.rev()
        result = BigInt()
        p_s, p_a = self._head, another._head
        if self._head is None or another._head is None:
            raise ValueError("cannot add None")

        bigger_than_9 = 0
        while p_s.next is not None and p_a.next is not None:
            result_digit, bigger_than_9 = BigInt.digit_add(p_s.elem, p_a.elem, bigger_than_9)
            result.prepend(result_digit)
            p_s = p_s.next
            p_a = p_a.next
        result_digit, bigger_than_9 = BigInt.digit_add(p_s.elem, p_a.elem, bigger_than_9)
        result.prepend(result_digit)

        if p_a.next is None and p_s.next is not None:
            p = p_s.next
        elif p_s.next is None and p_a.next is not None:
            p = p_a.next
        else:
            if bigger_than_9:
                result.prepend(1)
            return result
        while p.next is not None:
            result_digit, bigger_than_9 = BigInt.digit_add(p.elem, 0, bigger_than_9)
            p = p.next
        result_digit, bigger_than_9 = BigInt.digit_add(p.elem, 0, bigger_than_9)
        result.prepend(result_digit)
        if bigger_than_9:
            result.prepend(1)
        return result

    def __sub__(self, another):
        pass


if __name__ == "__main__":
    a = BigInt()
    b = BigInt()
    number = [2,9,9,99]
    number_1 = [7,4,9,4]
    for i in number:
        a.prepend(i)
    for i in number_1:
        b.prepend(i)
    print(a)
    print(b)
    print(a + b)
