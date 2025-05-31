from sqlalchemy.orm import Session
from datetime import datetime
import random
from faker import Faker
from models.models import Group, Student, Teacher, Subject, Grade
from connection import session

faker = Faker()


def seed_database():
    # Create groups
    groups = [Group(name=f"Group {i+1}") for i in range(3)]
    session.add_all(groups)
    session.flush()

    # Create teachers
    teachers = [Teacher(full_name=faker.name()) for _ in range(5)]
    session.add_all(teachers)
    session.flush()

    # Create subjects assigned to teachers
    subject_names = [
        "Math",
        "Physics",
        "History",
        "Art",
        "Biology",
        "Philosophy",
        "Science",
        "Geography",
    ]
    subjects = [
        Subject(name=name, teacher=random.choice(teachers)) for name in subject_names
    ]
    session.add_all(subjects)
    session.flush()

    # Create students in random groups
    students = [
        Student(full_name=faker.name(), group=random.choice(groups)) for _ in range(50)
    ]
    session.add_all(students)
    session.flush()

    # Create grades for each student
    for student in students:
        for _ in range(random.randint(10, 20)):
            grade = Grade(
                student=student,
                subject=random.choice(subjects),
                grade=random.randint(60, 100),
                date_received=faker.date_time_between(start_date="-1y", end_date="now"),
            )
            session.add(grade)

    session.commit()
    print("✅ Database seeded successfully.")


if __name__ == "__main__":
    seed_database()
