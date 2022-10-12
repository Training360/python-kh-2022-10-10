import mariadb

conn = mariadb.connect(
    user="employees",
    password="employees",
    host="localhost",
    port=3306,
    database="employees")

cur = conn.cursor()

cur.execute(
    "create table if not exists employees (id bigint not null auto_increment, emp_name varchar(255), primary key (id))")

cur.execute("insert into employees(emp_name) values (?)", ("John Doe",))
cur.execute("insert into employees(emp_name) values (?)", ("Jack Doe",))
cur.execute("insert into employees(emp_name) values (?)", ("Jane Doe",))

conn.commit()