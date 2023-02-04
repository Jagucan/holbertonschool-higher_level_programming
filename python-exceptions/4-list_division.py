#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for num in range(list_length):
        a = 0
        b = 0

        if num >= len(my_list_2):
            result += [0] * (list_length - len(my_list_2))
            print("out of range")
            break

        try:
            a = my_list_1[num]
            b = my_list_2[num]

        except IndexError:
            result.append(0)
            print("out of range")

        finally:
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):

                if b == 0:
                    result.append(0)
                    print("division by 0")

                else:
                    result.append(a / b)

            else:
                result.append(0)
                print("wrong type")

    return result
