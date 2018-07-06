from itertools import islice
import compute

class Record:
    student_class = {}
    marks_a1 = {}
    marks_a2 = {}
    marks_proj = {}
    marks_test1 = {}
    marks_test2 = {}
    max_marks_a1 = None
    max_marks_a2 = None
    max_proj = None
    max_marks_t1 = None
    max_marks_t2 = None

    with open('class.txt', 'rt') as in_file:
        for line in in_file:
            line_input = line.strip().split('|')
            student_class[line_input[0]] = line_input[1] + "," + line_input[2]

    with open('a1.txt') as f_a1:
        max_marks_a1 = f_a1.readline()
        for line in islice(f_a1,0,500):
            input = line.strip().split('|')
            marks_a1[input[0]] = input[1]

    with open('a2.txt') as f_a2:
        max_marks_a2 = f_a2.readline()
        for line in islice(f_a2,0,500):
            input = line.strip().split('|')
            marks_a2[input[0]] = input[1]

    with open('project.txt') as f_proj:
        max_proj = f_proj.readline()
        for line in islice(f_proj,0,500):
            input = line.strip().split('|')
            marks_proj[input[0]] = input[1]

    with open('test1.txt') as f_t1:
        max_marks_t1 = f_t1.readline()
        for line in islice(f_t1,0,500):
            input = line.strip().split('|')
            marks_test1[input[0]] = input[1]

    with open('test2.txt') as f_t2:
        max_marks_t2 = f_t2.readline()
        for line in islice(f_t2,0,500):
            input = line.strip().split('|')
            marks_test2[input[0]] = input[1]



def main():
    option='''1> Display individual component
2> Display component average 
3> Display Standard Report 
4> Sort by alternate column 
5> Change Pass/Fail point 
6> Exit'''

    while True:
        print(option)
        choice= input("Enter your choice (1-6):")
        if choice == "1":
            compute.individual_component()
        elif choice == "2":
            compute.Average_component()
        elif choice == "3":
            compute.report()
        elif choice == "4":
            compute.sorted_component()
        elif choice == "5":
            compute.change_grade()
        elif choice == "6":
            print("Good Bye",end="")
            exit(0)

if __name__ == '__main__':
    main()



