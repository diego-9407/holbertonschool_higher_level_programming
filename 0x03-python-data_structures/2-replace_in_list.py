def replace_in_list(my_list, idx, element):
    counter = 0;

    for int in my_list:
        if counter > idx:
            return my_list
        if counter == idx:
            my_list[idx] = element
            return my_list
        counter += 1
    return my_list
