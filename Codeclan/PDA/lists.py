my_list = [1, 4, 7, 10, 15, 75, 3, 1]

# should return 8
def length_of_list(list):
    return len(list)

print(length_of_list(my_list))

# should add 7 to the end of my_list
def add_item_to_list(list_name, num_1):
    list_name.append(num_1)
    print(list_name)

add_item_to_list(my_list, 7)

# should remove 7 from the end of my_list
def remove_num_from_end_of_list(list_name):
    list_name.pop()
    print(list_name)

remove_num_from_end_of_list(my_list)

# should return 10
def find_element_by_index(list_name, index):
    return list_name[index]

print(find_element_by_index(my_list, 3))

#  will return the sum of all the items on the list
def sum_list(list_name):
    total = 0
    for number in list_name:
        total += number

    print(total)

sum_list(my_list)


