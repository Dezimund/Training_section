from student import Student
from group import Group


def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)
    print (gr.find_student('Jobs'))
    print (gr.find_student('Jobs2'))

    gr.delete_student('Taylor')
    print(gr)


if __name__ == "__main__":
    main()
