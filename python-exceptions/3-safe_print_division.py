#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = (a / b)
        return div

    except ZeroDivisionError:
            return None

    finally:
        if a >= 0 and b > 0:
            div = (a / b)
            print("Inside result: {}".format(div))
            return div

        else:
            div = None
            print("Inside result: {}".format(div))
            return div
