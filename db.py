import mysql.connector
from mysql.connector import Error

import commands


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")



connection = create_server_connection("localhost", "root", "killmenow")
# create_database(connection, "CREATE DATABASE budgeting")
# connection = create_db_connection("localhost", "root", "killmenow", "budgeting") # Connect to the database

def add_profile(profile):
    print(profile)
    placeholders = ', '.join(['%s'] * len(profile))
    columns = ', '.join(profile.keys())
    sql = "INSERT INTO profiles.profiles ( %s ) VALUES ( %s )" % (columns, placeholders)
    # valid in Python 3
    cursor = connection.cursor()
    print(sql)
    cursor.execute(sql, list(profile.values()))
    connection.commit()

def add_goal(goal):
    print(goal)
    placeholders = ', '.join(['%s'] * len(goal))
    columns = ', '.join(goal.keys())
    sql = "INSERT INTO profiles.goals ( %s ) VALUES ( %s )" % (columns, placeholders)
    # valid in Python 3
    cursor = connection.cursor()
    print(sql)
    cursor.execute(sql, list(goal.values()))
    connection.commit()

def add_expense(expense):
    print(expense)
    placeholders = ', '.join(['%s'] * len(expense))
    columns = ', '.join(expense.keys())
    sql = "INSERT INTO profiles.expenses ( %s ) VALUES ( %s )" % (columns, placeholders)
    # valid in Python 3
    cursor = connection.cursor()
    print(sql)
    cursor.execute(sql, list(expense.values()))
    connection.commit()

