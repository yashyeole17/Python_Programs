#   1. Write a Python Program to Read the Contents of a text File and display the following information.
#   a. Total number of characters, digits, special symbols, words, spaces and lines.
import os
def count_characters(string):
    return len(string)

def count_digits(string):
    return sum(1 for char in string if char.isdigit())

def count_special_symbols(string):
    special_symbols = "!@#$%^&*()-_+=~`[]{}|:;\"'<>,.?/"
    return sum(1 for char in string if char in special_symbols)

def count_words(string):
    words = string.split()
    return len(words)

def count_spaces(string):
    return sum(1 for char in string if char.isspace())

def count_lines(string):
    lines = string.splitlines()
    return len(lines)

def Given_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()

            characters = count_characters(file_contents)
            digits = count_digits(file_contents)
            special_symbols = count_special_symbols(file_contents)
            words = count_words(file_contents)
            spaces = count_spaces(file_contents)
            lines = count_lines(file_contents)

            print("Path of the current file:", os.path.abspath(file_name))
            print("Total characters:", characters)
            print("Total digits:", digits)
            print("Total special symbols:", special_symbols)
            print("Total words:", words)
            print("Total spaces:", spaces)
            print("Total lines:", lines)

    except FileNotFoundError:
        print("File not found!")

# Usage example:
file_name = "sample.txt"
Given_file(file_name)
