'''Write a function that removes duplicate elements from a list. You cannot use set() because sets do not maintain the original order of elements.'''


mylist = [4, 4, 2, 10, 10, 8, 3, 2, 9, 2, 2, 7, 5, 1, 8, 5, 10, 5, 4, 9]

#print(list(set(mylist))) ❌ it will not preserve the order

filtered_list = []

for item in mylist:
    if item not in filtered_list:
        filtered_list.append(item)
        
print(f"Given list: {mylist} \nFiltered list: {filtered_list}")
