import grades
from operator import itemgetter

def report():
    print("ID    LN     FN     A1  A2  PR  T1  T2  GR    FL")
    Data=grades.Record.student_class.keys()
    for i in sorted(Data):
            print("{0:<6}".format(i),end="")
            Data1 = grades.Record.student_class.get(i).split(',')
            print("{0:<7}".format(Data1[1]),end="")
            print("{0:<7}".format(Data1[0]),end="")
            if grades.Record.marks_a1.get(i) == " ":
                print("{0:<4}".format(" "), end="")
            else:
                Data2 = grades.Record.marks_a1.get(i)
                print("{0:<4}".format(Data2), end="")

            if grades.Record.marks_a2.get(i) == " ":
                print("{0:<4}".format(" "), end="")
            else:
                Data3 = grades.Record.marks_a2.get(i)
                print("{0:<4}".format(Data3), end="")

            if grades.Record.marks_proj.get(i) == " ":
                print("{0:<4}".format(" "), end="")
            else:
                Data4 = grades.Record.marks_proj.get(i)
                print("{0:<4}".format(Data4), end="")

            if grades.Record.marks_test1.get(i) == 0:
                print("{0:<4}".format(" "), end="")
            else:
                Data5 = grades.Record.marks_test1.get(i)
                print("{0:<4}".format(Data5), end="")

            if grades.Record.marks_test2.get(i) == 0:
                print("{0:<4}".format(" "), end="")
            else:
                Data6 = grades.Record.marks_test2.get(i)
                print("{0:<4}".format(Data6), end="")

            sum = 0
            if Data2.isdigit():
                sum += int(Data2)/int(grades.Record.max_marks_a1) * 7.5

            if Data3.isdigit():
                sum += int(Data3)/int(grades.Record.max_marks_a2) * 7.5

            if Data4.isdigit():
                sum += int(Data4)/int(grades.Record.max_proj) * 25

            if Data5.isdigit():
                sum += int(Data5)/int(grades.Record.max_marks_t1) * 30

            if Data6.isdigit():
                sum += int(Data6)/int(grades.Record.max_marks_t2) * 30

            print("{0:<6}".format(float("{0:.2f}".format(sum))), end="")
            if sum >= 94:
                print("A+",end="")
            elif sum >= 87:
                print("A",end="")
            elif sum >= 80:
                print("A-",end="")
            elif sum >= 73:
                print("B+",end="")
            elif sum >= 66:
                print("B",end="")
            elif sum >= 59:
                print("B-",end="")
            elif sum >= 50:
                print("C",end="")
            else:
                print("F",end="")
            print("\n", end="")
    print("\n")

def individual_component():
    while True:
        value = input("Enter the component name (A1,A2,PR,T1,T2) : ").lower()
        if value == "a1":
            print("A1 grades (" + grades.Record.max_marks_a1.strip() + ")")
            Data = grades.Record.student_class.keys()
            for i in Data:
                print("{0:<6}".format(i), end="")
                Data1 = grades.Record.student_class.get(i).split(",")
                print("{0:<13}".format(Data1[1]+","+Data1[0]),end="")
                if grades.Record.marks_a1.get(i) == " ":
                    Data2 == 0
                    print("{0:<13}".format(" "), end="")
                elif grades.Record.marks_a1.get(i).isdigit():
                    Data2 = grades.Record.marks_a1.get(i)
                    print("{0:<13}".format(Data2), end="")
                print("\n",end="")
            print("\n")
            break
        elif value == "a2":
            print("A2 grades (" + grades.Record.max_marks_a2.strip() + ")")
            Data = grades.Record.student_class.keys()
            for i in Data:
                print("{0:<6}".format(i), end="")
                Data1 = grades.Record.student_class.get(i).split(",")
                print("{0:<13}".format(Data1[1]+","+Data1[0]), end="")
                if grades.Record.marks_a2.get(i) == " ":
                    Data2 == 0
                    print("{0:<13}".format(" "), end="")
                elif grades.Record.marks_a2.get(i).isdigit():
                    Data2 = grades.Record.marks_a2.get(i)
                    print("{0:<13}".format(Data2), end="")
                print("\n", end="")
            print("\n")
            break
        elif value == "pr":
            print("PR grades (" + grades.Record.max_proj.strip() + ")")
            Data = grades.Record.student_class.keys()
            for i in Data:
                print("{0:<6}".format(i), end="")
                Data1 = grades.Record.student_class.get(i).split(",")
                print("{0:<13}".format(Data1[1]+","+Data1[0]), end="")
                if grades.Record.marks_proj.get(i) == " ":
                    Data2 == 0
                    print("{0:<13}".format(" "), end="")
                elif grades.Record.marks_proj.get(i).isdigit():
                    Data2 = grades.Record.marks_proj.get(i)
                    print("{0:<13}".format(Data2), end="")
                print("\n", end="")
            print("\n")
            break
        elif value == "t1":
            print("T1 grades (" + grades.Record.max_marks_t1.strip() + ")")
            Data = grades.Record.student_class.keys()
            for i in Data:
                print("{0:<6}".format(i), end="")
                Data1 = grades.Record.student_class.get(i).split(",")
                print("{0:<13}".format(Data1[1]+","+Data1[0]), end="")
                if grades.Record.marks_test1.get(i) == " ":
                    Data2 == 0
                    print("{0:<13}".format(" "), end="")
                elif grades.Record.marks_test2.get(i).isdigit():
                    Data2 = grades.Record.marks_test1.get(i)
                    print("{0:<13}".format(Data2), end="")
                print("\n", end="")
            print("\n")
            break
        elif value == "t2":
            print("T2 grades (" + grades.Record.max_marks_t2.strip() + ")")
            Data = grades.Record.student_class.keys()
            for i in Data:
                print("{0:<6}".format(i), end="")
                Data1 = grades.Record.student_class.get(i).split(",")
                print("{0:<13}".format(Data1[1]+","+Data1[0]), end="")
                if grades.Record.marks_test2.get(i) == " ":
                    Data2 == 0
                    print("{0:<13}".format(" "), end="")
                elif grades.Record.marks_test2.get(i).isdigit():
                    Data2 = grades.Record.marks_test2.get(i)
                    print("{0:<13}".format(Data2), end="")
                print("\n", end="")
            print("\n")
            break
        else:
            print("Invalid component name, Please keyin proper name")
            continue

def Average_component():
    while True:
        option = input("Enter the component name (A1,A2,PR,T1 or T2) to check the average: ").lower()
        sum = 0
        count = 0
        if option == "a1":
            Data = grades.Record.student_class.keys()
            for i in Data:
                if grades.Record.marks_a1.get(i) == " ":
                    Data2 == 0
                    sum += Data2
                elif grades.Record.marks_a1.get(i).isdigit():
                    Data2 = int(grades.Record.marks_a1.get(i))
                    sum += Data2
                    count += 1
            print(" A1 average: ",(float("{0:.2f}".format(sum/count))),"/",grades.Record.max_marks_a1,end="")
            print("\n")
            break
        elif option == "a2":
            Data = grades.Record.student_class.keys()
            for i in Data:
                if grades.Record.marks_a2.get(i) == " ":
                    Data2 == 0
                    sum += Data2
                elif grades.Record.marks_a2.get(i).isdigit():
                    Data2 = int(grades.Record.marks_a2.get(i))
                    sum += Data2
                    count += 1
            print(" A2 average: ", (float("{0:.2f}".format(sum/count))), "/", grades.Record.max_marks_a2,end="")
            print("\n")
            break
        elif option == "pr":
            Data = grades.Record.student_class.keys()
            for i in Data:
                if grades.Record.marks_proj.get(i) == " ":
                    Data2 == 0
                    sum += Data2
                elif grades.Record.marks_proj.get(i).isdigit():
                    Data2 = int(grades.Record.marks_proj.get(i))
                    sum += Data2
                    count += 1
            print(" PR average: ", (float("{0:.2f}".format(sum/count))), "/", grades.Record.max_proj,end="")
            print("\n")
            break
        elif option == "t1":
            Data = grades.Record.student_class.keys()
            for i in Data:
                if grades.Record.marks_test1.get(i) == " ":
                    Data2 == 0
                    sum += Data2
                elif grades.Record.marks_test1.get(i).isdigit():
                    Data2 = int(grades.Record.marks_test1.get(i))
                    sum += Data2
                    count += 1
            print(" T1 average: ", (float("{0:.2f}".format(sum/count))), "/", grades.Record.max_marks_t1,end="")
            print("\n")
            break
        elif option == "t2":
            Data = grades.Record.student_class.keys()
            for i in Data:
                if grades.Record.marks_test2.get(i) == " ":
                    Data2 == 0
                    sum += Data2
                elif grades.Record.marks_test2.get(i).isdigit():
                    Data2 = int(grades.Record.marks_test2.get(i))
                    sum += Data2
                    count += 1
            print(" T2 average: ", (float("{0:.2f}".format(sum/count))), "/", grades.Record.max_marks_t2,end="")
            print("\n")
            break
        else:
            print("Invalid component name, Please keyin proper name")
            continue

def sorted_component():
    list ={}
    Data = grades.Record.student_class.keys()
    for i in Data:
        Data2 = grades.Record.student_class.get(i).split(",")
        list[i]=Data2[1]

    list1={}
    for i in Data:

        Data2 = grades.Record.marks_a1.get(i)
        Data3 = grades.Record.marks_a2.get(i)
        Data4 = grades.Record.marks_proj.get(i)
        Data5 = grades.Record.marks_test1.get(i)
        Data6 = grades.Record.marks_test2.get(i)

        sum = 0
        if grades.Record.marks_a1.get(i) == " ":
            Data2 == 0
            sum += int(Data2) / int(grades.Record.max_marks_a1) * 7.5
        elif Data2.isdigit():
            sum += int(Data2) / int(grades.Record.max_marks_a1) * 7.5

        if grades.Record.marks_a2.get(i) == " ":
            Data3 == 0
            sum += int(Data3) / int(grades.Record.max_marks_a2) * 7.5
        elif Data3.isdigit():
            sum += int(Data3) / int(grades.Record.max_marks_a2) * 7.5

        if grades.Record.marks_proj.get(i) == " ":
            Data4 == 0
            sum += int(Data4) / int(grades.Record.max_proj) * 7.5
        elif Data4.isdigit():
            sum += int(Data4) / int(grades.Record.max_proj) * 25

        if grades.Record.marks_test1.get(i) == " ":
            Data5 == 0
            sum += int(Data5) / int(grades.Record.max_marks_t1) * 7.5
        elif Data5.isdigit():
            sum += int(Data5) / int(grades.Record.max_marks_t1) * 30

        if grades.Record.marks_test2.get(i) == " ":
            Data6 == 0
            sum += int(Data6) / int(grades.Record.max_marks_t2) * 7.5
        elif Data6.isdigit():
            sum += int(Data6) / int(grades.Record.max_marks_t2) * 30

        list1[i] = sum

    while True:
        option = input("Select the Sort order: LT(last name) or GR(numeric grade): ").lower()
        if option == "lt":
            print("ID    LN     FN     A1  A2  PR  T1  T2  GR    FL")
            for i in sorted(list.items(), key=itemgetter(1)):
                print("{0:<6}".format(i[0]), end="")
                Data1 = grades.Record.student_class.get(i[0]).split(',')
                print("{0:<7}".format(Data1[1]), end="")
                print("{0:<7}".format(Data1[0]), end="")
                if grades.Record.marks_a1.get(i[0]) == " ":
                    print("{0:<4}".format(" "), end="")
                else:
                    Data2 = grades.Record.marks_a1.get(i[0])
                    print("{0:<4}".format(Data2), end="")

                if grades.Record.marks_a2.get(i[0]) == " ":
                    print("{0:<4}".format(" "), end="")
                else:
                    Data3 = grades.Record.marks_a2.get(i[0])
                    print("{0:<4}".format(Data3), end="")

                if grades.Record.marks_proj.get(i[0]) == " ":
                    print("{0:<4}".format(" "), end="")
                else:
                    Data4 = grades.Record.marks_proj.get(i[0])
                    print("{0:<4}".format(Data4), end="")

                if grades.Record.marks_test1.get(i[0]) == 0:
                    print("{0:<4}".format(" "), end="")
                else:
                    Data5 = grades.Record.marks_test1.get(i[0])
                    print("{0:<4}".format(Data5), end="")

                if grades.Record.marks_test2.get(i[0]) == 0:
                    print("{0:<4}".format(" "), end="")
                else:
                    Data6 = grades.Record.marks_test2.get(i[0])
                    print("{0:<4}".format(Data6), end="")

                sum = 0
                if Data2.isdigit():
                    sum += int(Data2) / int(grades.Record.max_marks_a1) * 7.5

                if Data3.isdigit():
                    sum += int(Data3) / int(grades.Record.max_marks_a2) * 7.5

                if Data4.isdigit():
                    sum += int(Data4) / int(grades.Record.max_proj) * 25

                if Data5.isdigit():
                    sum += int(Data5) / int(grades.Record.max_marks_t1) * 30

                if Data6.isdigit():
                    sum += int(Data6) / int(grades.Record.max_marks_t2) * 30

                print("{0:<6}".format(float("{0:.2f}".format(sum))), end="")
                if sum >= 94:
                    print("A+", end="")
                elif sum >= 87:
                    print("A", end="")
                elif sum >= 80:
                    print("A-", end="")
                elif sum >= 73:
                    print("B+", end="")
                elif sum >= 66:
                    print("B", end="")
                elif sum >= 59:
                    print("B-", end="")
                elif sum >= 50:
                    print("C", end="")
                else:
                    print("F", end="")
                print("\n", end="")
            print("\n")
            break
        elif option == "gr":
            print("ID    LN     FN     A1  A2  PR  T1  T2  GR    FL")
            for i in sorted(list1.items(), key=itemgetter(1)):
                print("{0:<6}".format(i[0]), end="")
                Data1 = grades.Record.student_class.get(i[0]).split(',')
                print("{0:<7}".format(Data1[1]), end="")
                print("{0:<7}".format(Data1[0]), end="")
                if grades.Record.marks_a1.get(i[0]) == " ":
                    print("{0:<4}".format(" "), end="")
                else:
                    Data2 = grades.Record.marks_a1.get(i[0])
                    print("{0:<4}".format(Data2), end="")

                if grades.Record.marks_a2.get(i[0]) == " ":
                    print("{0:<4}".format(" "), end="")
                else:
                    Data3 = grades.Record.marks_a2.get(i[0])
                    print("{0:<4}".format(Data3), end="")

                if grades.Record.marks_proj.get(i[0]) == " ":
                    print("{0:<4}".format(" "), end="")
                else:
                    Data4 = grades.Record.marks_proj.get(i[0])
                    print("{0:<4}".format(Data4), end="")

                if grades.Record.marks_test1.get(i[0]) == 0:
                    print("{0:<4}".format(" "), end="")
                else:
                    Data5 = grades.Record.marks_test1.get(i[0])
                    print("{0:<4}".format(Data5), end="")

                if grades.Record.marks_test2.get(i[0]) == 0:
                    print("{0:<4}".format(" "), end="")
                else:
                    Data6 = grades.Record.marks_test2.get(i[0])
                    print("{0:<4}".format(Data6), end="")

                sum = 0
                if Data2.isdigit():
                    sum += int(Data2) / int(grades.Record.max_marks_a1) * 7.5

                if Data3.isdigit():
                    sum += int(Data3) / int(grades.Record.max_marks_a2) * 7.5

                if Data4.isdigit():
                    sum += int(Data4) / int(grades.Record.max_proj) * 25

                if Data5.isdigit():
                    sum += int(Data5) / int(grades.Record.max_marks_t1) * 30

                if Data6.isdigit():
                    sum += int(Data6) / int(grades.Record.max_marks_t2) * 30

                print("{0:<6}".format(float("{0:.2f}".format(sum))), end="")
                if sum >= 94:
                    print("A+", end="")
                elif sum >= 87:
                    print("A", end="")
                elif sum >= 80:
                    print("A-", end="")
                elif sum >= 73:
                    print("B+", end="")
                elif sum >= 66:
                    print("B", end="")
                elif sum >= 59:
                    print("B-", end="")
                elif sum >= 50:
                    print("C", end="")
                else:
                    print("F", end="")
                print("\n", end="")
            print("\n")
            break
        else:
            print("Invalid Option")
            continue


def change_grade():
    choice = input("Enter a new Pass/Fail mark: ")
    cutoff = float(choice)
    print("ID    LN     FN     A1  A2  PR  T1  T2  GR    FL")
    Data = grades.Record.student_class.keys()
    for i in sorted(Data):
        print("{0:<6}".format(i), end="")
        Data1 = grades.Record.student_class.get(i).split(',')
        print("{0:<7}".format(Data1[1]), end="")
        print("{0:<7}".format(Data1[0]), end="")
        if grades.Record.marks_a1.get(i) == " ":
            print("{0:<4}".format(" "), end="")
        else:
            Data2 = grades.Record.marks_a1.get(i)
            print("{0:<4}".format(Data2), end="")

        if grades.Record.marks_a2.get(i) == " ":
            print("{0:<4}".format(" "), end="")
        else:
            Data3 = grades.Record.marks_a2.get(i)
            print("{0:<4}".format(Data3), end="")

        if grades.Record.marks_proj.get(i) == " ":
            print("{0:<4}".format(" "), end="")
        else:
            Data4 = grades.Record.marks_proj.get(i)
            print("{0:<4}".format(Data4), end="")

        if grades.Record.marks_test1.get(i) == " ":
            print("{0:<4}".format(" "), end="")
        else:
            Data5 = grades.Record.marks_test1.get(i)
            print("{0:<4}".format(Data5), end="")

        if grades.Record.marks_test2.get(i) == " ":
            print("{0:<4}".format(" "), end="")
        else:
            Data6 = grades.Record.marks_test2.get(i)
            print("{0:<4}".format(Data6), end="")

        sum = 0
        if Data2.isdigit():
            sum += int(Data2)/int(grades.Record.max_marks_a1) * 7.5

        if Data3.isdigit():
            sum += int(Data3)/int(grades.Record.max_marks_a2) * 7.5

        if Data4.isdigit():
            sum += int(Data4)/int(grades.Record.max_proj) * 25

        if Data5.isdigit():
            sum += int(Data5)/int(grades.Record.max_marks_t1) * 30

        if Data6.isdigit():
            sum += int(Data6)/int(grades.Record.max_marks_t2) * 30

        print("{0:<6}".format(float("{0:.2f}".format(sum))), end="")
        marks = float(100-cutoff)/7
        if sum >= 100 - marks:
            print("A+", end="")
        elif sum >= 100 - (2 * marks):
            print("A", end="")
        elif sum >= 100 - (3 * marks):
            print("A-", end="")
        elif sum >= 100 - (4 * marks):
            print("B+", end="")
        elif sum >= 100 - (5 * marks):
            print("B", end="")
        elif sum >= 100 - (6 * marks):
            print("B-", end="")
        elif sum >= cutoff:
            print("C", end="")
        else:
            print("F", end="")
        print("\n", end="")
    print("\n")










