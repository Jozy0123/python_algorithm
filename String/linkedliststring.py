from linkedlist import LList, LNode

class string(LList):

    def __init__(self, txt = ''):
        LList.__init__(self)
        if len(txt) > 0:
            self._head = LNode(txt[0])
            p = self._head
            for i in txt[1:]:
                p.next = LNode(i)
                p = p.next

    def __str__(self):
        p = self._head
        str_ = ''
        while p.next is not None:
            str_ = str_ + p.elem
            p = p.next
        return str_ + p.elem





if __name__ == "__main__":
    t = string("xdfadfasd")
    print(t)
    print(t.len())
