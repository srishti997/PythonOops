def list_methods_demo():
    my_list = [1, 2, 3, 4, 5]
    my_list.append(6)
    print("Append method:", my_list)
    my_list.extend([7, 8, 9])
    print("Extend method:", my_list)
    my_list.insert(2, 10)
    print("Insert method:", my_list)
    my_list.remove(3)
    print("Remove method:", my_list)
    popped_element = my_list.pop()
    print("Popped element using pop method:", popped_element)
def tuple_methods_demo():
    my_tuple = (1, 2, 3, 4, 5)
    index = my_tuple.index(3)
    print("Index of element 3:", index)
    count = my_tuple.count(4)
    print("Count of element 4:", count)
def set_methods_demo():
    my_set = {1, 2, 3, 4, 5}
    my_set.add(6)
    print("Add method:", my_set)
    my_set.remove(3)
    print("Remove method:", my_set)
    popped_element = my_set.pop()
    print("Popped element using pop method:", popped_element)
def dictionary_methods_demo():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    value = my_dict.get('b')
    print("Value for key 'b' using get method:", value)
    popped_value = my_dict.pop('c')
    print("Popped value for key 'c' using pop method:", popped_value)
    my_dict.update({'d': 4})
    print("Updated dictionary using update method:", my_dict)
def main():
    print("List methods:")
    list_methods_demo()
    print("\nTuple methods:")
    tuple_methods_demo()
    print("\nSet methods:")
    set_methods_demo()
    print("\nDictionary methods:")
    dictionary_methods_demo()
if __name__ == "__main__":
    main()
