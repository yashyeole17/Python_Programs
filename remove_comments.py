def remove(fileOne):
    try:
        with open(fileOne, 'r') as file:
            lines = file.readlines()

        with open(fileOne, 'w') as file:
            for line in lines:
                line = line.split('#')[0]  # Access the first element after splitting
                file.write(line + '\n')  # Write the line without comment symbol
            print("Comments removed successfully!")

    except FileNotFoundError:
        print('File NOT found')

    except Exception as e:
        print("An error occurred while removing comments:", str(e))

if __name__ == "__main__":
    fileOne = input("Enter File Name: ")
    remove(fileOne)
