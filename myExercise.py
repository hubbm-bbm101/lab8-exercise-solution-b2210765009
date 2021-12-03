import sys
student_dict = {}
text_file = sys.argv[1]
names_input = sys.argv[2]
names_input = names_input.split(",")
for i in range(len(names_input)):
    name = names_input[i]
    with open(text_file, "r") as f:
        try:
            lines = f.read().splitlines()
            for line in range(len(lines)):
                student_name, university_and_department = lines[line].split(":")
                student_dict[student_name] = university_and_department
            print("\nName: " + name + ", University: " + student_dict[name] + ".\n")
        except KeyError:
            print("\nError! No record of "+ name + " was found.\n")
