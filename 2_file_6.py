# Write Python Program to Reverse Each Word in "data.txt" file.

def reverse_words(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    reversed_lines = []
    for line in lines:
        words = line.split()
        reversed_words = [word[::-1] for word in words]
        reversed_line = " ".join(reversed_words)
        reversed_lines.append(reversed_line)
    with open(filename, "w") as file:
        file.write("\n".join(reversed_lines))

    print("Words reversed and saved to", filename)
filename = "data.txt"
reverse_words(filename)
