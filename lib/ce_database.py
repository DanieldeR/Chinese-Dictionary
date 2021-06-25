import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None

    print("Connecting to DB")

    try:
        conn = sqlite3.connect(db_file)
        print("Connected to the DB")
        return conn
    except Error as e:
        print(e)


def add_word_to_database(conn, word):

    sql = ''' INSERT INTO ce(traditional,simplified,pinyin,english,hsk) 
              VALUES(?,?,?,?,?) '''

    print(f"Adding {word[2]}")

    cur = conn.cursor()
    cur.execute(sql, word)
    conn.commit()


if __name__ == '__name__':
    conn = create_connection('dictionary.sqlite')
    print(conn)

    test_word = ('test', 'test', 'test', 'test', 'test')
    add_word(conn, test_word)
