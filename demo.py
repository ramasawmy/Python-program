
option =int(input("1-all student, 2-add student, 3-remove student. Please enter 1, 2, 3:"))

if option == 1:
    print(student_list)
    student = input("add students:")
    student_list.append(student)
    print(student_list)

elif option == 2:
    student = input("insert a student:")
    pos = int(input("where to add him/her:"))
    if pos<len(student_list):
        student_list.insert(pos,student)
        print(student_list)
    else:
        print("invalid")

elif option == 3:
    student_to_remove = input("which student to remove:")

    if student_to_remove in student_list:
        student_list.remove(student_to_remove)
        print(student_list)
    else:
        print("that is not a student")

