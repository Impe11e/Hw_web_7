from sqlalchemy import func, desc

from conf.db import session
from conf.models import Student, Grade, Subject, Group, Teacher


def select_1():
    session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()


def select_2(subject_name: str):
    session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subject_name == subject_name).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all()


def select_3(subject_name: str):
    session.query(Student.group_id, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).filter(Grade.subject_name == subject_name).group_by(
        Student.group_id).order_by(
        desc('average_grade')).all()


def select_4():
    session.query(func.avg(Grade.grade)).label('avg_grade').join(Grade).scalar()


def select_5(teacher_name: str):
    session.querry(Teacher.fullname, Subject.name).select_from(Teacher). \
        join(Subject, Teacher.id == Subject.teacher_id).filter(Teacher.fullname == teacher_name).all()


def select_6(group_name: str):
    session.querry(Student.fullname).select_from(Student).join(Group, Student.group_id == Group.id). \
        filter(Group.name == group_name).all()


def select_7(subject_id: int, groups_id: int):
    session.query(Grade.grade, Student.fullname, Subject.name, Group.name).select_from(Student). \
        join(Group, Student.group_id == Group.id).join(Grade, Grade.subject_id == Subject.id). \
        join(Subject, Grade.subject_id == Subject.id).filter(Subject.id == subject_id, Group.id == groups_id).all()


def select_8():
    session.query(func.avg(Grade.grade), Teacher.fullname, Subject.name).select_from(Grade). \
        join(Subject, Grade.subject_id == Subject.id).join(Teacher, Subject.teacher_id == Teacher.id).scalar()


def select_9(student_id: int):
    session.query(Subject.fullname).select_from(Subject). \
        join(Grade, Subject.id == Grade.subject_id).join(Student, Grade.student_id == Student.id). \
        filter(Student.id == student_id).all()


def select_10(student_id: int, teacher_id: int):
    session.query(Subject.name).select_from(Subject).join(Grade, Subject.id == Grade.subject_id). \
        join(Student, Grade.student_id == Student.id).join(Teacher, Subject.teacher_id == Teacher.id). \
        filter(Student.id == student_id, Teacher.id == teacher_id).all()
