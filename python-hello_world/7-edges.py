#!/usr/bin/python3
word = "Holberton"
word_last_2 = "Hol"
word_first_3 = "on"
middle_word = word_last_2[1:3] + word[3:-2] + word_first_3[0]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
