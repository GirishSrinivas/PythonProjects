# Author: Girish Srinivas
# This program will create and populate an employee database with random dataset.
# This data can be used for testing purpose.

import MySQLdb
import random
import sys
from datetime import date

names = []
sex = ['M', 'F']
nm = 'dept'
no = 'd'
dept_no = []

f = open('names.txt', 'r')
for line in f:
    s = line.split()
    names.append(s)
fnames, lnames = map(list, zip(*names))
f.close()

for i in range(100):
    no1 = no + str(i + 1)
    dept_no.append(no1)

#
try:
    conn = MySQLdb.connect(host = "localhost",
                           user = "root",
                           passwd = "root",
                           db = "sample")
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

try:
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS dept_manager")
    cursor.execute("DROP TABLE IF EXISTS dept_emp")
    cursor.execute("DROP TABLE IF EXISTS salaries")
    cursor.execute("DROP TABLE IF EXISTS departments")
    cursor.execute("DROP TABLE IF EXISTS employee")

    # CREATING EMPLOYEE TABLE
    cre_emp = """
                CREATE TABLE employee
                (
                    emp_no int auto_increment,
                    first_name CHAR(25),
                    last_name CHAR(25),
                    gender CHAR(1),
                    birth_date date,
                    hire_date date,
                    primary key(emp_no)
                )
    """
    cursor.execute(cre_emp)

    # CREATING DEPARTMENTS TABLE
    cre_dept = """
                    CREATE TABLE departments
                    (
                        dept_no char(25),
                        dept_name char(25),
                        primary key (dept_no)
                    )
    """
    cursor.execute(cre_dept)

    # CREATING SALARIES TABLE
    cre_sal = """
                CREATE TABLE salaries
                (
                    emp_no int auto_increment,
                    salary int,
                    from_date date,
                    to_date date,
                    primary key(emp_no),
                    foreign key(emp_no) references employee(emp_no)
                )
    """
    cursor.execute(cre_sal)

    # CREATING DEPT_EMP TABLE
    cre_dept_emp = """
                    CREATE TABLE dept_emp
                    (
                        emp_no int,
                        dept_no char(25),
                        from_date date,
                        to_date date,
                        foreign key(emp_no) references employee(emp_no),
                        foreign key(dept_no) references departments(dept_no)
                    )
    """
    cursor.execute(cre_dept_emp)

    # CREATING DEPT_MANAGER TABLE
    cre_dept_manager = """
                        CREATE TABLE dept_manager
                        (
                            emp_no int,
                            dept_no char(25),
                            from_date date,
                            to_date date,
                            foreign key(emp_no) references employee(emp_no),
                            foreign key(dept_no) references departments(dept_no)
                        )
    """
    cursor.execute(cre_dept_manager)

    # INSERTING DATA INTO EMPLOYEE TABLE
    for i in range(100000):
        f = random.choice(fnames)
        l = random.choice(lnames)
        g = random.choice(sex)
        d = random.sample(range(1, 28), 1)[0]
        m = random.sample(range(1, 12), 1)[0]
        y = random.sample(range(1900, 2015), 1)[0]
        dt = date(y, m, d)
        d1 = random.sample(range(1, 28), 1)[0]
        m1 = random.sample(range(1, 12), 1)[0]
        y1 = random.sample(range(1900, 2015), 1)[0]
        hdt = date(y1, m1, d1)
        ins_emp = "insert into employee (first_name, last_name, gender, birth_date, hire_date) " \
                  "values ('%s', '%s', '%s', '%s', '%s')" % (f, l, g, dt, hdt)
        cursor.execute(ins_emp)

    # INSERTING DATA INTO DEPARTMENTS TABLE
    for i in range(100):
        nm1 = nm + str(i + 1)
        no1 = no + str(i + 1)
        ins_dept = "insert into departments (dept_no, dept_name) values('%s', '%s')" % (no1, nm1)
        cursor.execute(ins_dept)

    # INSERTING DATA INTO SALARIES TABLE
    for i in range(100000):
        sal = random.randint(1111, 999999)
        d = random.sample(range(1, 28), 1)[0]
        m = random.sample(range(1, 12), 1)[0]
        y = random.sample(range(1900, 2015), 1)[0]
        dt = date(y, m, d)
        d1 = random.sample(range(1, 28), 1)[0]
        m1 = random.sample(range(1, 12), 1)[0]
        y1 = random.sample(range(1900, 2015), 1)[0]
        hdt = date(y1, m1, d1)
        ins_sal = "insert into salaries (salary, from_date, to_date) " \
                  "values('%d', '%s', '%s')" % (sal, dt, hdt)
        cursor.execute(ins_sal)

    # INSERTING DATA INTO DEPT_EMP TABLE
    for i in range(90000):
        ids = random.sample(range(1, 100000), 1)[0]
        no1 = random.choice(dept_no)
        d = random.sample(range(1, 28), 1)[0]
        m = random.sample(range(1, 12), 1)[0]
        y = random.sample(range(1900, 2015), 1)[0]
        dt = date(y, m, d)
        d1 = random.sample(range(1, 28), 1)[0]
        m1 = random.sample(range(1, 12), 1)[0]
        y1 = random.sample(range(1900, 2015), 1)[0]
        hdt = date(y1, m1, d1)
        ins_dept_emp = "insert into dept_emp(emp_no, dept_no, from_date, to_date) " \
                       "values('%d', '%s', '%s', '%s')" % (ids, no1, dt, hdt)
        cursor.execute(ins_dept_emp)

    # INSERTING DATA INTO DEPT_MANAGER TABLE
    for i in range(1000):
        ids = random.sample(range(1, 100000), 1)[0]
        no1 = random.choice(dept_no)
        d = random.sample(range(1, 28), 1)[0]
        m = random.sample(range(1, 12), 1)[0]
        y = random.sample(range(1900, 2015), 1)[0]
        dt = date(y, m, d)
        d1 = random.sample(range(1, 28), 1)[0]
        m1 = random.sample(range(1, 12), 1)[0]
        y1 = random.sample(range(1900, 2015), 1)[0]
        hdt = date(y1, m1, d1)
        ins_dept_manager = "insert into dept_manager(emp_no, dept_no, from_date, to_date) " \
                           "values('%d', '%s', '%s', '%s')" % (ids, no1, dt, hdt)
        cursor.execute(ins_dept_manager)

    cursor.close()

except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

conn.commit()
conn.close()



