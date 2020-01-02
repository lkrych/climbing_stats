import sqlite3
import os

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
 
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

def load_table_sql(filename):
    """ load sql from db folder into string
    :param filename: string, db file
    :return: sql as string
    """
    sql = ""
    with open('./migrations/' + filename, 'r') as file:
        sql = file.read()
    return sql
    

def main():
    dirname = os.path.dirname(__file__)
    database = os.path.join(dirname, 'climbing_stats.db')
 
    sql_create_users_table = load_table_sql('1_create_users.sql')
 
    sql_create_workouts_table = load_table_sql('2_create_workouts.sql')

    sql_create_climbs_table = load_table_sql('3_create_climbs.sql')
 
    # create a database connection
    conn = create_connection(database)
 
    # create tables
    if conn is not None:
        # create users table
        create_table(conn, sql_create_users_table)
 
        # create workouts table
        create_table(conn, sql_create_workouts_table)

        #create climbs table
        create_table(conn, sql_create_climbs_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()