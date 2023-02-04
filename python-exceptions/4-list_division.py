#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for num in range(list_length):
        try:
            if isinstance(my_list_1[num], (int, float)) \
                and isinstance(my_list_2[num], (int, float)):

                if my_list_2[num] == 0:
                    result.append(0)
                    print("division by 0")

                else:
                    result.append(my_list_1[num] / my_list_2[num])

            else:
                result.append(0)
                print("wrong type")

        except IndexError:
            result.append(0)
            print("out of range")

    return result
