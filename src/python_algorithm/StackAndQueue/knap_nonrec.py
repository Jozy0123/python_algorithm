from python_algorithm.StackAndQueue import SStack


def knap_nonrec(weight, wlist, n):

    stack = SStack()

    dyna_n = n - 1
    dyna_weight = weight

    while dyna_weight > 0 and dyna_n > 0:
        stack.push((dyna_weight, dyna_n))
        dyna_n = dyna_n - 1
        dyna_weight = dyna_weight - wlist[dyna_n]

    while True:
        if stack.top()[0] == 0:
            return True, stack._elems
        elif stack.top()[0] < 0:
            stack.pop()
            dyna_weight = stack.top()[0]
            dyna_n = stack.top()[1] - 1
            stack.push((dyna_weight, dyna_n))
            while dyna_weight > 0 and dyna_n > 0:
                dyna_n = dyna_n - 1
                dyna_weight = dyna_weight - wlist[dyna_n]
                if dyna_n < 0:
                    break
                stack.push((dyna_weight, dyna_n))
                print(stack._elems)
            continue
        elif stack.top()[0] == weight and dyna_n > 0:
            dyna_n = stack.pop()[1] - 1
            dyna_weight = weight
            if dyna_n <= 0:
                break
            stack.push((dyna_weight, dyna_n))
            while dyna_weight > 0 and dyna_n > 0:
                dyna_n = dyna_n - 1
                dyna_weight = dyna_weight - wlist[dyna_n]
                stack.push((dyna_weight, dyna_n))
            print(stack._elems)
            continue
        elif stack.pop()[0] > 0:
            dyna_n = dyna_n - 1
            if dyna_n < 0:
                break
            dyna_weight = dyna_weight - wlist[dyna_n]
            stack.push((dyna_weight, dyna_n))
            while  dyna_weight > 0 and dyna_n > 0:
                dyna_n = dyna_n - 1
                dyna_weight = dyna_weight -wlist[dyna_n]
                stack.push((dyna_weight, dyna_n))
            print(stack._elems)
            continue
        else:
            break
    return False

weight_goal = 100
wlist = [92, 20, 17, 20, 60, 87]
result = knap_nonrec(weight_goal, wlist, 6)
print(result)
