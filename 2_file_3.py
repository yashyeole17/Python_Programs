# 3   Write a program that reads the contents of the file and counts the
# occurrences of each letter. Prompt the user to enter the filename.

def count_letter_occurrences(filename):
    occurrences = {}
    with open(filename, 'r') as file:
        content = file.read()
        for char in content:
            if char.isalpha():
                char = char.lower()
                occurrences[char] = occurrences.get(char, 0) + 1
    return occurrences

filename = input("Enter the file name: ")
letter_counts = count_letter_occurrences(filename)
print("Letter Occurrences:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")
