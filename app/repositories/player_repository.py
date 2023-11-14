import csv
import sqlite3

def create_in_memory_database():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE player_stats (
                PLAYER TEXT,
                POSITION TEXT,
                FTM INTEGER,
                FTA INTEGER,
                "2PM" INTEGER,
                "2PA" INTEGER,
                "3PM" INTEGER,
                "3PA" INTEGER,
                REB INTEGER,
                BLK INTEGER,
                AST INTEGER,
                STL INTEGER,
                TOV INTEGER
            )
        ''')

    return conn, cursor

def load_data_into_database(cursor,csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cursor.execute('''
                INSERT INTO player_stats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''' , (
                row['PLAYER'],
                row['POSITION'],
                row['FTM'],
                row['FTA'],
                row['2PM'],
                row['2PA'],
                row['3PM'],
                row['3PA'],
                row['REB'],
                row['BLK'],
                row['AST'],
                row['STL'],
                row['TOV']
            ))

    cursor.connection.commit()