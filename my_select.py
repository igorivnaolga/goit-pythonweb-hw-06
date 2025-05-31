from sqlalchemy import func, desc
from connection import session
from models import Student, Grade, Subject, Group, Teacher


def select_1():
    # Find 5 students with the highest average grade across all subjects
    return (
        session.query(Student.full_name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )


def select_2(subject_name: str):
    # Find the student with the highest average grade for a specific subject
    return (
        session.query(Student.full_name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(1)
        .first()
    )


def select_3(subject_name: str):
    # Find the average grade in each group for a specific subject
    return (
        session.query(Group.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Group.id)
        .all()
    )


def select_4():
    # Find the overall average grade (for the entire grades table)
    return session.query(func.avg(Grade.grade)).scalar()


def select_5(teacher_name: str):
    # Find which courses are taught by a specific teacher
    return (
        session.query(Subject.name)
        .join(Teacher)
        .filter(Teacher.full_name == teacher_name)
        .all()
    )


def select_6(group_name: str):
    # Find a list of students in a specific group
    return (
        session.query(Student.full_name)
        .join(Group)
        .filter(Group.name == group_name)
        .all()
    )


def select_7(group_name: str, subject_name: str):
    # Find grades of students from a specific group in a specific subject
    return (
        session.query(Student.full_name, Grade.grade)
        .join(Group)
        .join(Grade)
        .join(Subject)
        .filter(Group.name == group_name, Subject.name == subject_name)
        .all()
    )


def select_8(teacher_name: str):
    # Find the average grade that a specific teacher gives in their subjects
    return (
        session.query(func.avg(Grade.grade))
        .join(Subject, Grade.subject_id == Subject.id)
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .filter(Teacher.full_name == teacher_name)
        .scalar()
    )


def select_9(student_name: str):
    # Find a list of courses that a specific student attends
    return (
        session.query(Subject.name)
        .join(Grade)
        .join(Student)
        .filter(Student.full_name == student_name)
        .distinct()
        .all()
    )


def select_10(student_name: str, teacher_name: str):
    # Find a list of courses that a specific teacher teaches to a specific student
    return (
        session.query(Subject.name)
        .join(Teacher)
        .join(Grade)
        .join(Student)
        .filter(Student.full_name == student_name, Teacher.full_name == teacher_name)
        .distinct()
        .all()
    )
