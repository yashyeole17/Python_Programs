
#Write Python Program to Read and Print Each Line in "India. txt" file. (use with statement)

filename = "India.txt"

with open(filename, "r") as file:
    for line in file:
        print(line.rstrip())