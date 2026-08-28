"""Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is."""

def dict_merger(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value
        
    return merged_dict


A = {
    "apple" : 5,
    "banana" : 3,
    "mango" : 2
}

B = {
    "banana" : 7,
    "mango" : 4,
    "orange" : 6
}

print(dict_merger(A, B))