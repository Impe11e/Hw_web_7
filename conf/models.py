
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table, MetaData
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    start_work = Column(Date, nullable=False)
    students = relationship("Student", back_populates="teacher")
    subjects = relationship("Subjects", back_populates="teacher")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name



class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    teachers = relationship("Teacher", secondary='teachers_to_students', back_populates="student")
    group_id = Column('group_id', ForeignKey("groups.id", ondelete="CASCADE"))
    groups = relationship("Group", back_populates="student")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    teacher_id = Column('teacher_id', ForeignKey("teachers.id", ondelete="CASCADE"))
    teachers = relationship("Teacher", back_populates="subject")

class Group(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    students_id = Column('students_id', ForeignKey("students.id"))
    students = relationship("Student", back_populates="group")

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column('grade_date', Date)
    student_id = Column('student_id', ForeignKey("students.id", ondelete="CASCADE"))
    subject_id = Column('subject_id', ForeignKey("subjects.id", ondelete="CASCADE"))
    student = relationship("Student", back_populates="grade")
    subject = relationship("Subject", back_populates="grade")
