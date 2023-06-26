#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ divides element by element 2 lists.

    Args:
        my_list_1: The first list.
        my_list_2: The second list.
        list_length: number of elements to divide.

    Returns:
        A a new list with all divisions
    """
    div_list = []
    for i in range(0, list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_result = 0
        except ZeroDivisionError:
            print("division by 0")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            div_list.append(div_result)
    return (div_list)
