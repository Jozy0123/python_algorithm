from pattern_matching import matching_KMP

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

def tokens(string, seps):
    print("***********************************")
    final = string
    while len(final) > len(seps):
        position_to_be_replaced = matching_KMP(final, seps)
        if position_to_be_replaced > 0:
            yield final[0: position_to_be_replaced]
            final = final[position_to_be_replaced + len(seps):]
        elif position_to_be_replaced == 0:
            final = final[position_to_be_replaced + len(seps):]
        else:
            yield final
            break

for i in tokens("abcdefgabdabadfasddfafd","ab"):
    print(i)
