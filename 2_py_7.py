# Write Python Program to Find the Longest Word in a File. Get the File Name from User.

def find_longest_word(filename):
    with open(filename, "r") as file:
        words = file.read().split()

    longest_word = max(words, key=len)
    return longest_word


# Example usage
filename = input("Enter the file name: ")

try:
    longest_word = find_longest_word(filename)
    print("The longest word in the file is:", longest_word)
except FileNotFoundError:
    print("File not found. Please make sure the file exists.")
