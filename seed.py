import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teacher, Student, Subject, Group

fake = Faker('uk-UA')


def insert_students():
    groups = [Group(name=fake.word()) for _ in range(3)]
    session.commit()

    for _ in range(40):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            group=random.choice(groups)
        )
        session.add(student)
    session.commit()


def insert_teachers():
    for _ in range(3, 5):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date='-5y')
        )
        session.add(teacher)
    session.commit()


def insert_subjects():
    teachers = session.query(Teacher).all()

    for _ in range(5, 8):
        subject = Subject(
            name=fake.word(),
            teacher=random.choice(teachers)
        )
        session.add(subject)
    session.commit()


if __name__ == '__main__':
    try:
        insert_students()
        insert_teachers()
        insert_subjects()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
