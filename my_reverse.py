def my_reverse (list):
    reversed_list = []
    while len(list) > 0:
        length = len(list)
        lastinlist = (list[length-1])
        reversed_list.append (lastinlist)
        del list[-1]
    return reversed_list