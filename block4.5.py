def copyDict(dict_to_copy):
    new_dict = {}
    for key in dict_to_copy:
        new_dict[key] = dict_to_copy[key]
    return new_dict


my_dict = {"a": 1, "b": 2, "c": 3}
new_dict = copyDict(my_dict)

print(my_dict)
print(new_dict)

my_dict["d"] = 4 
print(my_dict)
print(new_dict) 
my_list = [1, 2, 3]
new_list = my_list[:] 
my_list[0] = 4

print(my_list)
print(new_list)




my_dict2 = {"a": 1, "b": 2, "c": 3}
new_dict2 = my_dict2[:]  
print(new_dict2)
