"""Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements."""

def flatter(list1):
    flat_list = []
    for item in list1:
        if isinstance(item, list):
            flat_list.extend(flatter(item))
        else:
            flat_list.append(item)
            
    return flat_list



list1 = [12, 59, 53, 21, 78, 97, [67, 74, 58, 52]]

print(flatter(list1))

