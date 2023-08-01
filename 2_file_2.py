
# Write a program to read the first and last ‘n’ lines of a file.
# Prompt the user to enter the value for n.


def read_first_last_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()

        print(f"First {n} lines:")
        for line in lines[:n]:
            print(line.strip())

        print(f"\nLast {n} lines:")
        for line in lines[-n:]:
            print(line.strip())

filename = "sample.txt"
n = int(input("Enter the value of 'n': "))
read_first_last_lines(filename, n)
