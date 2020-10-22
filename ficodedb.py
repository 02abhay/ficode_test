# first install mysql-connector-python
# import here mysql connctor to connect database
import mysql.connector

# creating input for database connection
hostname = input('Enter Db Host:')
username= input('Enter DB Username:')
passwd = input('Enter DB Password: ')

mydb = mysql.connector.connect(
 host=hostname,
 user=username,
 passwd=passwd,
)

# creating functions to use our database
def initDB():
    mycursor = mydb.cursor()
    mycursor.execute('USE ficodedb')
initDB()

# Now you can see your table that you had created in schemas
def ficode():
    cursor =  mydb.cursor()
    cursor.execute('SHOW TABLES')
    res = cursor.fetchall()
    print(res)
ficode()

# By giving input to department_id as 1,2
def data():
    dept_id = input('Enter your department ID:')
    cursor=mydb.cursor()
    cursor.execute("SELECT * FROM employees where dept_id = %s", (dept_id, ))
    test=cursor.fetchall()
    print(test)
data()

# Enter input as employee name that have database and get timing
def dep_emp_name():
    cursor = mydb.cursor()
    name = input('Enter emp name:')
    sql = "SELECT * FROM  departmenttimings where dept_id = (select dept_id from employees where employees_name = '"+name+"' )"
    # print(sql)
    cursor.execute(sql)
    timing = cursor.fetchall()
    print(timing)
dep_emp_name()

# input department name and get sum of all employee according to id
def emp_salary():
    dept_id = input('Enter your department ID:')
    cursor = mydb.cursor()
    cursor.execute("SELECT sum(salary) FROM employees where dept_id = %s", (dept_id,))
    test = cursor.fetchall()
    print(test)
emp_salary()





