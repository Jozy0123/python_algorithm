
def naive_matching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:
        if p[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - i + 1
    if i == m:
        return j - i
    return -1

def gen_pnext(p):
    """
    generate pnext table for every char in pattern string.
    useful for non-returning pattern matching.
    """
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = pnext[k]
        else:
            k = pnext[k]
    return pnext

def matching_KMP(t, p):
    pnext = gen_pnext(p)
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j, i = j+1, i+1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1

def replace_(origin_string, pattern_string, target_string):
    """
    target_string: needs to be replaces with pattern string.
    pattern_string: the string which will replace the string
    """
    result_string = ''
    target_string_length = len(target_string)
    pattern_string_length = len(pattern_string)
    position_to_be_replaced = matching_KMP(origin_string, pattern_string)

    moving_starting_pos = position_to_be_replaced - pattern_string_length + target_string_length
    result_string = origin_string[:position_to_be_replaced-1] + target_string + origin_string[moving_starting_pos:]
    return result_string

if __name__ == '__main__':

    print(replace_("abcdef", "cd", 'ace'))
