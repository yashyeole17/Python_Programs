#5.Write Python program to remove the comment character from all the lines in a given Python source file.

def remove_comments(source_file, output_file):
    with open(source_file, "r") as file:
        lines = file.readlines()
    with open(output_file, "w") as file:
        for line in lines:
            if "#" in line:
                line = line[:line.index("#")]
            file.write(line)
    print("Comments removed and saved to", output_file)
source_file = "source.py"
output_file = "output.py"
remove_comments(source_file, output_file)
