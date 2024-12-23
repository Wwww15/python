from sqlalchemy import Column, String, create_engine, INT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    no = Column(INT, primary_key=True)
    name = Column(String(20))
    age = Column(INT)

    def print_info(self):
        s = "no:%s,name:%s,age:%d" % (self.no, self.name, self.age)
        print(s)


def select_student(session):
    student = session.query(Student).filter(Student.no == 1).one()
    student.print_info()
    session.close()


def save_student(session):
    student = Student()
    student.no = 2
    student.name = "李四"
    student.age = 90
    session.add(student)

    session.commit()
    session.close()


if __name__ == "__main__":
    engine = create_engine("mysql+mysqlconnector://root:123456@192.168.119.151:3307/test")
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    # select_student(session)
    save_student(session)
