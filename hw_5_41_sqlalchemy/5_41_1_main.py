from sqlalchemy import create_engine, Column, String, Integer, or_, text, ForeignKey, Date, Numeric, Float, DECIMAL
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, aliased


engine = create_engine('sqlite:///hr.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Employees(Base):

    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    hire_date = Column(Date)
    job_id = Column(String)
    salary = Column(String)
    commission_pct = Column(Numeric)
    manager_id = Column(Integer)
    department_id = Column(Integer)
    Avg_Salary = Column(Numeric)


class Departments(Base):

    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True)
    department_name = Column(String)
    manager_id = Column(String)
    location_id = Column(String)


class Jobs(Base):

    __tablename__ = 'jobs'

    job_id = Column(String, primary_key=True)
    job_title = Column(String)
    min_salary = Column(String)
    max_salary = Column(String)


if __name__ == "__main__":
    session = Session()

    job = session.query(Employees).filter(Employees.first_name == 'John').all()
    print(list(x.last_name for x in job))
    
    session.commit()
    session.close()


