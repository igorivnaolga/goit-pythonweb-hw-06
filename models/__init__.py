from models.models import Group, Student, Teacher, Subject, Grade

print("I am in __init__.py")
__all__ = ["Group", "Student", "Teacher", "Subject", "Grade"]

print("__all__ was defined")
