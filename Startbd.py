import sqlite3
import pytest

conn = sqlite3.connect('Really_Good_db.db')
cursor = conn.cursor()


def add_user(user_id: int, user_name: str):
    cursor.execute('INSERT INTO test (user_id, user_name) VALUES (?, ?)',
                   (user_id, user_name))
    conn.commit()
    
def test_sql_lite3():
    add_user(1, 'Artur')


