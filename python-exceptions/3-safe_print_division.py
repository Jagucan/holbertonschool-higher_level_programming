#!/usr/bin/python3
def safe_print_division(a, b):
    try:
       div = (a / b)
       return div
    except:
        if b == 0:
            return None
    finally:
        if a >= 0 and b > 0:
            div = (a / b)
            return div