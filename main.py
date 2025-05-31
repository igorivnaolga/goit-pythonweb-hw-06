from my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)


def run_queries():
    print("1. Top 5 students by average grade:")
    for row in select_1():
        print(row)

    print("\n2. Top student in 'Math':")
    print(select_2("Math"))

    print("\n3. Average grade in groups for 'Math':")
    for row in select_3("Math"):
        print(row)

    print("\n4. Average grade overall:")
    print(select_4())

    print("\n5. Courses taught by 'Miss Hannah Smith':")
    for row in select_5("Miss Hannah Smith"):
        print(row)

    print("\n6. Students in group 'Group 2':")
    for row in select_6("Group 2"):
        print(row)

    print("\n7. Grades in 'Group 1' for subject 'Geography':")
    for row in select_7("Group 1", "Geography"):
        print(row)

    print("\n8. Average grade given by 'Miss Hannah Smith':")
    print(select_8("Miss Hannah Smith"))

    print("\n9. Subjects attended by student 'Brian Anderson':")
    for row in select_9("Brian Anderson"):
        print(row)

    print("\n10. Courses 'Brian Anderson' attends taught by 'Miss Hannah Smith':")
    for row in select_10("Brian Anderson", "Miss Hannah Smith"):
        print(row)


if __name__ == "__main__":
    run_queries()
