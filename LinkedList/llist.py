class LinkedListUnderFLow(ValueError):
    pass


class LinkedListOverFLow(Exception):
    pass


class LNode:
    def __init__(self, elem, _next=None):
        self.elem = elem
        self.next = _next


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        else:
            p = self._head
            while p.next is not None:
                p = p.next
            p.next = LNode(elem)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderFLow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def __len__(self):
        if self._head is None:
            return 0
        else:
            n, p = 1, self._head
            while p.next is not None:
                n += 1
                p = p.next
        return n

    def __str__(self):
        string = ""
        if self._head is None:
            return string
        p = self._head
        while p.next is not None:
            string = string + '\t' + str(p.elem)
            p = p.next
        final_string = string + '\t' + str(p.elem)
        return final_string.lstrip()

    def insert(self, elem, i):
        n, p = 0, self._head
        if i == 0:
            self.prepend(elem)
            return
        while p.next is not None:
            if n + 1 == i:
                p.next = LNode(elem, p.next)
                return
            else:
                p = p.next
                n += 1
        raise LinkedListOverFLow("in insertion")

    def del_last(self):
        p = self._head
        if p is None:
            raise LinkedListUnderFLow("in del")
        else:
            while p.next is not None:
                if p.next.next is None:
                    print(str(p.next.elem))
                    p.next = None
                else:
                    p = p.next
            return

    def delElem(self, i):
        n, p = 0, self._head
        if i == 0 and self._head is not None:
            self._head = self._head.next
            return
        elif i == 0 and self._head is None:
            return
        while p.next is not None:
            if n + 1 == i:
                p.next = p.next.next
                return
            else:
                p = p.next
                n += 1
        raise LinkedListUnderFLow("in delete element")

    def search(self, elem):
        n, p = 0, self._head
        while p.next is not None:
            if p.elem == elem:
                return n
            else:
                p = p.next
                n += 1
        if p.elem == elem:
            return n
        else:
            return -1

    def linkedListFromList(self, lst):
        self._head = None
        n = len(lst) - 1
        while n >= 0:
            self.prepend(lst[n])
            print(lst[n])
            n -= 1
        return

    def linkedListToList(self):
        p = self._head
        lst = []
        while p.next is not None:
            lst.append(p.elem)
            p = p.next
        lst.append(p.elem)
        return lst

    def rev_visit(self, op):
        new = LList()
        p = self._head
        while p.next is not None:
            new.prepend(self.pop())
            p = p.next
        new.prepend(self.pop())
        p = new._head
        while p.next is not None:
            p.elem = op(p.elem)
            print(str(p.elem))
            p = p.next
        p.elem = op(p.elem)
        p = new._head
        while p.next is not None:
            self.prepend(new.pop())
            p = p.next
        self.prepend(new.pop())
        print(self)

    def find_minimal(self):
        p, n = self._head, 0
        min_loc = 0
        min = p.elem
        while p.next is not None:
            if p.elem <= min:
                min = p.elem
                min_loc = n
            p = p.next
            n += 1
        if p.elem <= min:
            min = p.elem
            min_loc = n
        self.delElem(min_loc)
        return min

    def del_if(self, pred):
        p = self._head
        if pred(p.elem):
            self._head = p.next
        while p.next is not None:
            if pred(p.next.elem):
                p.next = p.next.next
            else:
                p = p.next
        return

    def del_duplicate(self):
        record = {}
        p = self._head
        if p is None or p.next is None:
            return
        record[p.elem] = 1
        while p.next is not None:
            if record.get(p.next.elem, 0) == 1:
                p.next = p.next.next
            else:
                record[p.next.elem] = 1
                p = p.next
        return

    def interleaving(self, another):
        self_p, another_p = self._head, another._head
        if another._head is None:
            return
        elif self._head is None:
            self = another
        else:
            while self_p.next is not None and another_p is not None:
                self_p.next = LNode(another_p.elem, self_p.next)
                self_p = self_p.next.next
                if another_p is None:
                    return
                another_p = another_p.next
            self_p.next = another_p

    def rev(self):
        result = LList()
        while self._head is not None:
            result.prepend(self.pop())
        self._head = result._head

    def sortlist(self):
        new = LList()
        n = self.__len__()
        i = 0
        while i < n:
            min = self.find_minimal()
            new.prepend(min)
            i += 1
        self._head = new._head
        self.rev()

    def partition(self, pred):
        newList = LList()
        p = self._head
        if p is None or p.next is None:
            raise LinkedListUnderFLow("in partition")
        if pred(p.elem):
            newList.append(self.pop())
        while p.next is not None:
            if pred(p.next.elem):
                newList.prepend(p.next.elem)
                p.next = p.next.next
            p = p.next
        if pred(p.elem):
            newList.prepend(p.elem)
            self.del_last()
        newList.rev()
        return newList


# class BigInt(LList):


if __name__ == '__main__':
    newList = LList()
    newList.prepend(5)
    newList.prepend(4)
    newList.prepend(3)
    newList.prepend(0)

    anotherList = LList()
    anotherList.append(1)
    anotherList.append(6)
    anotherList.append(8)

    print(newList)
    print(anotherList)
    anotherList.interleaving(newList)
    print(anotherList)
    anotherList.sortlist()
    print(anotherList)
    print(anotherList.partition(lambda x: x % 2 == 0))
    print(anotherList)
