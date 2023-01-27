#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for text in dir(hidden_4):
        if not text.startswith('__'):
            print("{}".format(text))
