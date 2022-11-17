import sqlite3
con = sqlite3.connect('users.db')
cur = con.cursor()
"""
id integer (primary key)
name string
last string
username string
age string (Male, Female, Other)
sex string
years integer
"""
# Create table
try:
    cur.execute('''CREATE TABLE employees (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        last TEXT, 
                        username TEXT, 
                        age INTEGER, 
                        sex TEXT, 
                        years INTEGER )''')
except :
    pass

try:
    initial_datas = [
        [1, "Noah","James", "Noah James", 20, "Male", 1],
        [2, "Liam", "John", "Liam John", 23, "Female", 3],
        [3, "Oliver", "Jake", "Oliver Jake", 33, "Male", 5],
        [4, "Jack", "Connor", "Mark Jhon", 30, "Male", 3],
        [5, "Harry", "Callum", "Jack Connor", 34, "Male", 4],
        [6, "Jacob", "Jacob", "Jacob Jacob", 17, "Female", 1],
        [7, "Charlie","Kyle", "Charlie Kyle", 45, "Female", 10],
        [8, "Thomas","Joe", "Thomas Joe", 66, "Male", 20],
        [10, "George","Reece", "George Reece", 44, "Female", 14],
        [11, 'Oscar',"Rhys", "Oscar Rhys", 33, "Male", 3],
        [12, "James",'Charlie', "James Charlie", 32, "Male", 1],
        [13, 'William','Damian', "William Damian", 52, "Other", 23],
        [14, 'Mason','Robert', "Mason Robert", 45, "Female", 12],
        [15, 'Jacob','Michael', "Jacob Michael", 31, "Male", 2],
        [16, 'William','William', "William William", 29, "Male", 5]
    ]

    query = """
        INSERT INTO employees (id, name , last, username, age, sex, years) 
        values (?, ?, ?, ?, ?, ?, ?)
    """
    excute = cur.executemany(query, (initial_datas))
    
except Exception as e:
    # print(repr(e))
    pass

con.commit()
cur.close()
con.close()
