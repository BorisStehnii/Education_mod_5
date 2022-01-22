from sqlalchemy import create_engine, Column, String, Integer, func, or_, text, ForeignKey, Date, Numeric, Float, DECIMAL
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, aliased
from pprint import pprint

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
    __tablename__ = 'department'

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


# 1
def full_name(session_, table):
    # SELECT first_name as 'First Name' || ' ' || last_name as 'Last Name' FROM employees;

    workers = session_.query(table.first_name + " " + table.last_name).all()
    return workers


# 2
def id_department(session_, table):
    # SELECT  DISTINCT  department_id FROM employees ORDER BY department_id;

    departments = session_.query(table.department_id).order_by(table.department_id).distinct().all()
    return departments


# 3
def name_and_department(session_, em, dp):
    # SELECT first_name, last_name, department_id, depart_name
    # FROM employees
    # JOIN departments
    # ON departments.department_id = employees.department_id;

    # print("____1___")
    # name_depart = session_.query(em.first_name + ' ' + em.last_name, dp.department_name)\
    #     .filter(dp.department_id == em.department_id).all()
    # print(name_depart)

    # print("____2___")
    name_depart = session_.query(em.first_name + ' ' + em.last_name, dp.department_name).join(dp, dp.department_id == em.department_id).all()
    # print(name_depart)
    return name_depart


# 4
def name_and_department_40_80(session_, em, dp):
    # SELECT first_name, last_name, department_id, depart_name
    # FROM employees
    # JOIN departments
    # ON departments.department_id = employees.department_id
    # WHERE departments.department_id = 40 or departments.department_id = 80;

    inquiry = session_.query(em.last_name,  dp.department_name, dp.department_id)\
        .join(dp, dp.department_id == em.department_id)\
        .filter(dp.department_id.in_([40, 80])).all()
    return inquiry


# 5
def depart_count(session_, em, dp):
    # SELECT D.depart_name, (SELECT COUNT(E.department_id) FROM employees as E WHERE E.department_id = D.department_id)
    # AS workers
    # FROM departments as D;
    inquiry = session_.query(dp.department_name, func.count(em.department_id))\
        .join(em, dp.department_id == em.department_id).group_by(em.department_id).all()
    return inquiry


# 6
def name_salary_difference(session_, *table):
    # SELECT E.first_name, E.last_name, J.job_title, E.salary-J.max_salary
    # FROM employees as E
    # JOIN jobs as J
    # ON E.job_id = J.job_id;

    inquiry = session_.query(table[0].last_name, table[1].job_title, table[0].salary - table[1].max_salary) \
        .filter(table[0].job_id == table[1].job_id).all()
    return inquiry


# 7
def avg_salary(session_, em, jb):
    # SELECT D.depart_name, (SELECT COUNT(E.department_id) FROM employees as E WHERE E.department_id = D.department_id)
    # AS workers
    # FROM departments as D;
    inquiry = session_.query(jb.job_title, func.avg(em.salary))\
        .join(em, jb.job_id == em.job_id).group_by(em.job_id).all()
    return inquiry


# 8
def name_depart_(session_, *table):
    # SELECT E.last_name, E.salary, D.depart_name
    # FROM employees as E
    # JOIN department as D
    # ON D.department_id = E.department_id OR D.depart_name = 'Sales'

    inquiry = session_.query(table[0].last_name, table[0].salary, table[0].department_id, table[1].department_name)\
        .filter(table[1].department_id == table[0].department_id)\
        .filter(table[1].department_name == 'Sales').all()
    return inquiry


# 9
def max_min_salary(session_, *table):
    # SELECT MAX(salary) as mas_salary, MIN(salary) as min_salary FROM employees;
    inquiry = session_.query(func.min(table[0].salary), func.max(table[0].salary)).all()
    return inquiry


# 10
def monthly_salary(session_, table):
    # SELECT first_name, last_name, salary, salary*0.12 as PF FROM employees;
    inquiry = session_.query(table.first_name + " " + table.last_name, table.salary * 0.12).all()
    return inquiry


if __name__ == "__main__":
    session = Session()

    # print(full_name(session, Employees))      # 1
    # print(id_department(session, Employees))      # 2
    # print(name_and_department(session, Employees, Departments))       # 3
    # print(name_and_department_40_80(session, Employees, Departments))     # 4
    # print(depart_count(session, Employees, Departments))      # 5
    # print(name_salary_difference(session, Employees, Jobs))       # 6
    print(avg_salary(session, Employees, Jobs))       # 7
    # print(name_depart_(session, Employees, Departments))        # 8
    # print(max_min_salary(session, Employees))       # 9
    # print(monthly_salary(session, Employees))       # 10
    # name_and_department(session, Employees, Departments)

    session.commit()
    session.close()
