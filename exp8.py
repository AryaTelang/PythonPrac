
import mysql.connector
# create a connection between the MySQL database and the python application,
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pass@123',
)
mycursor=mydb.cursor()
mycursor.execute("Create database Furniture")

#all mysql functions work through cursor object
#show databases
mycursor.execute("show databases")
for x in mycursor:
    print(x)

mycursor.execute("""create table Cupboard(id int not null,name varchar not null, price float not null, primary key(id))""")

mycursor.execute("""insert into cupboard(id, name, price, count)
values (6, 'cb31', 7500, 8)""")
mydb.commit()
