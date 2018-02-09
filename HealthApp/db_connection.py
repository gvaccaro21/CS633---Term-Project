"""
Module contains all database contructs for accessing health application database
"""
import sqlite3
from sqlite3 import Error
import json

def create_connection(db_file):
    """ 
    Attempts to create a generic database connection
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e_error:
        print(e_error)
    return None

def save_my_measurements(conn, values):
    """
    Saves the passed in measurements for the user to the connected database.
    """
    sql = '''INSERT INTO measure(MEASURE_ID, USER_ID, MEASURE_BMI, MEASURE_HEIGHT, MEASURE_WEIGHT) VALUES (?,?,?,?,?);'''
    cur = conn.cursor()
    cur.execute(sql, values)
    # commit_close(conn)
    return cur.lastrowid

def show_my_measurements(conn, user):
    """
    Queries the database for the measurements for a specified user
    """
    sql = '''SELECT * FROM measure WHERE USER_ID = ''' + str(user) + ";"
    print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    # commit_close(conn)
    return rows

def commit_close(conn):
    """
    Commits database changes and closes the connection
    """
    try:
        conn.commit()
        conn.close()
    except Error as e_error:
        print(e_error)
    return None

#Script debug variables
# myConn = create_connection('test.db')
# Values = (10,2,3,4,5)
# myUser = (1)
# print(save_my_measurements(myConn, Values))
# print(show_my_measurements(myConn, myUser))
# commit_close(myConn)