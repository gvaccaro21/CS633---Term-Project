"""
Module contains all database contructs for accessing health application database
"""
import sqlite3
from sqlite3 import Error
import json

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e_error:
        print(e_error)
    return None

def select_all_policies(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Policy")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def create_json(conn):
    """Return the pathname of the KOS root directory."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM Policy")
    json_string = json.dumps(cur.fetchall())
    print(json_string)

def select_json(conn, pn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Policy where PolicyNumber='" + pn + "'")
    PolicyNumber = 1
    Cycle = 1
    begindate = 2
    enddate = 3
    json_string = json.dumps({"PolicyNumber":PolicyNumber, "Result": \
    {"Cycle":Cycle, "begin_date":begindate, "end_date":enddate}})	
    r_var = [dict((cur.description[i][0], value) \
    for i, value in enumerate(row)) for row in cur.fetchall()]
    print(json_string)

def main():
    database = "C:\\sqllite\mydb.db"
 
    # create a database connection
    conn = create_connection(database)
    policy = "AOS24346281441"
    with conn:
        #print("1. Query all Policies")
        #select_all_policies(conn)
        print("2. Create JSON")
        select_json(conn,policy)
        conn.close
if __name__ == '__main__':
    main()
    
