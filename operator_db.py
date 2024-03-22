import sqlite3
import time
import json
import random

def create_table():
    table_schema = '''
        CREATE TABLE IF NOT EXISTS hitokoto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            category TEXT,
            source TEXT,
            hitokoto TEXT
        );
    '''

    conn = sqlite3.connect('hitokoto.db')

    cursor = conn.cursor()
    cursor.execute(table_schema)
    
    conn.commit()
    conn.close()
    print("creation completed!")


def insert_records(json_data):
    """ json_data
    {
        "category": "",
        "source": "",
        "hitokotos": [
            "hitokoto", "hitokoto"
        ]
    }
    """

    conn = sqlite3.connect('hitokoto.db')
    cursor = conn.cursor()

    insert_statement = """
        INSERT INTO hitokoto(timestamp, category, source, hitokoto)
        VALUES(?, ?, ?, ?);
    """

    timestamp = int(time.time())
    records = json.loads(json_data)

    for hitokoto in records["hitokotos"]:
        cursor.execute(insert_statement, 
            (timestamp, records['category'], records['source'], hitokoto))

    conn.commit()
    conn.close()
    print("insertion completed!")

def fetch_random_sentence():
    hitokoto = "Not Found"
    
    conn = sqlite3.connect('hitokoto.db')
    cursor = conn.cursor()

    fetch_statement = """
        SELECT hitokoto from hitokoto;
    """
    cursor.execute(fetch_statement)
    records = cursor.fetchall()

    if records:
        record = random.choice(records)
        hitokoto = record

    conn.commit()
    conn.close()

    json_hitokoto = {"hitokoto": hitokoto}
    json_hitokoto_str = json.dumps(json_hitokoto, ensure_ascii=False)
    return json_hitokoto_str
    
        