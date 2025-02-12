#!/usr/bin/env python3

#Using a list comprehension, write a function return_evens() 
# that returns a list of all of the even elements of a sequence of integers.
# return_evens([0, 1, 3, 5, 7, 8, 9])
# [0, 8]
# Using a list comprehension, write a function make_exclamation()
#  that takes a list of sentence strings and returns a list of sentence strings with exclamation marks at the end.
# make_exclamation(["Hello", "I'm doing great", "Python is fun"])
# ["Hello!", "I'm doing great!", "Python is fun!"]

def return_evens(num_list):
    even_list = [num for num in num_list if num % 2 == 0]

    return even_list

print(return_evens([0, 1, 3, 5, 7, 8, 9]))


# Using a list comprehension, write a function make_exclamation() that takes a list of sentence strings and returns a list of sentence strings with exclamation marks at the end
# make_exclamation(["Hello", "I'm doing great", "Python is fun"])
# ["Hello!", "I'm doing great!", "Python is fun!"]

def make_exclamation(sentence_list):
    exclamation_list = [sentence + "!" for sentence in sentence_list]

    return exclamation_list

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
    