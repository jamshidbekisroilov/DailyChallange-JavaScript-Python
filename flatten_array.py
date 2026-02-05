def flatten(arr):
    flat_list = []
    for item in arr:
        # Agar element list yoki tuple bo'lsa, yana o'zini chaqiramiz
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
#Demo test    
print(flatten([5, [4, [3, 2]], 1]))
