from linkedlist import LNode

class StackUnderFlow(ValueError):
    pass

class SStack:

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return len(self._elems) == 0

    def top(self):
        if self.is_empty():
            raise StackUnderFlow("in peeking the top element")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderFlow("in pop")
        p = self._elems[-1]
        self._elems = self._elems[:-1]
        return p

class LStack:

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderFlow("in peeking the first element")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderFlow("in pop")
        p = self._top.elem
        self._top = self._top.next
        return p

def check_parens(text):
    parents = "()[]{}"
    open_parens = "([{"
    opposite = {"(":")", "[":"]", "{":"}"}

def knap_rec_r(weight_goal, wlist, n):
    if weight_goal == 0:
        return True
    if knap_rec_r(weight_goal - wlist[n-1], wlist, n-1):
        return 

def knap_rec(weight_goal, wlist, n):

    stack = SStack()
    current_weight = 0
    while len(wlist) > 0:
        current_weight == 0
        for i in range(len(wlist)):
            print(wlist[i:])
            print("-----------------------")
            current_weight += wlist[i]
            if current_weight < weight_goal:
                stack.push(wlist[i])
            elif current_weight == weight_goal:
                stack.push(wlist[i])
                while not stack.is_empty():
                    print(str(stack.pop()))
                return
            else:
                if stack.is_empty():
                    break
                e = stack.pop()
                if stack.is_empty():
                    wlist.remove(e)
                    break
                else:
                    current_weight -= e
                    continue

    #
    #
    #
    #
    #
    #
    #
    # # stack_info = SStack()
    #
    # weight_tol = 0
    # for i in wlist:
    #     stack_info.push(i)
    #     weight_tol += i
    #
    # while not stack_info.is_empty() or not stack.is_empty():
    #     if weight_tol == weight_goal:
    #         return True
    #     elif weight_tol < weight_goal:
    #
    #     else:
    #         weight_top = stack_info.pop()
    #         weight_tol = weight_tol - weight_top
    #         if weight_goal == weight_tol - weight_top:
    #             return True
    #         elif weight_goal < weight_tol:
    #             continue
    #         else:
    #
    #
    #
    #
    # while len(wlist) >= 0
    #     weight += i
    #     if weight_goal > weight:
    #         stack.push(i)
    #     elif weight_goal = weight:
    #         print(i)
    #         while not stack.is_empty():
    #             print(stack.pop())
    #     else:
    #         stack.pop()




if __name__ == "__main__":

    weight_goal = 40
    wlist = [3, 23, 17, 60]
    knap_rec(weight_goal, wlist, 0)
