#!/usr/bin/env python3
# coding = utf-8
import sqlite3
import sys
import os

# Create a default database path for connection.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, r'register.sqlite3' )

def get_conn():
    con = None
    try:
        con = sqlite3.connect( DB_PATH,
        detect_types = sqlite3.PARSE_COLNAMES | sqlite3.PARSE_DECLTYPES )
        # print( con )
        print( 'Sqlite3 Version: -> ', sqlite3.version )
        print( 'Successfull Connection!' )
        return( con )
    
    except sqlite3.Error as e:
        print( e )
        
def insert_registration( registration_information ):
    insert_registration_sql = '''
        INSERT OR IGNORE INTO registration(
            first_name,
            last_name,
            contact,
            email,
            question,
            answer,
            password )
        VALUES( ?,?,?,?,?,?,? ); '''
    conn = get_conn()
    cursor = conn.cursor()
    cursor.executemany( insert_registration_sql, registration_information )
    conn.commit()
    cursor.execute( 'SELECT max( id ) FROM registration' )
    max_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    print( 'Current Max ID -> ', max_id )
    return( max_id )
    
def check_email( user_email ):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute( 'SELECT email FROM registration WHERE email = ?', ( user_email, ))
    query_result = cursor.fetchone()
    cursor.close()
    conn.close()
    return( query_result )

        
def create_tables():
    setup_pragma_sql = '''
        PRAGMA count_changes     = True;
        PRAGMA foreign_keys      = True;
        PRAGMA full_column_names = True;
        PRAGMA locking_mode      = EXCLUSIVE;
        PRAGMA secure_delete     = True;
        PRAGMA auto_vacuum       = Full; '''
    
    setup_registration_table_sql = '''
        CREATE TABLE IF NOT EXISTS registration(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name NVARCHAR( 100 ) NOT NULL,
        last_name  NVARCHAR( 100 ) NOT NULL,
        contact    NVARCHAR( 100 ) NOT NULL,
        email      NVARCHAR( 100 ) NOT NULL,
        question   NVARCHAR( 100 ) NOT NULL,
        answer     NVARCHAR( 100 ) NOT NULL,
        password   NVARCHAR( 100 ) NOT NULL,
        modified   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP );'''
    
    conn = get_conn()
    cursor = conn.cursor()
    cursor.executescript( setup_pragma_sql )
    cursor.execute( setup_registration_table_sql )
    conn.commit()
    cursor.close()
    conn.close()
    
    print( 'Pragma and create registration table complete' )

if __name__ == '__main__':
    pass
    ### create_tables()  # Execute only once.
    
