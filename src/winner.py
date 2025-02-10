
def find_2nd_max(list):
    if len(list) < 2:
        return None
    new_list = list.copy()
    new_list.sort()
    next_largest = new_list[-2]
    return next_largest
