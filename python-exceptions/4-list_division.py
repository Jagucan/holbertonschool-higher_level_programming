#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    list_1 = 0
    list_2 = 0

    for num in range(list_length):
        try:
            list_1 = my_list_1[num]
            list_2 = my_list_2[num]

        except IndexError:
            result.append(0)
            print("out of range")

        finally:
            if isinstance(list_1, (int, float)) \
                and isinstance(list_2, (int, float)):

                if list_2 != 0:
                    result.append(list_1 / list_2)

                else:
                    result.append(0)
                    print("division by 0")

            else:
                result.append(0)
                print("wrong type")

    return result
