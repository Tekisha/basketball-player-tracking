# app/main.py

from fastapi import FastAPI
from app.api.routers import main as main_router
from app.repositories.player_repository import create_in_memory_database, load_data_into_database

csv_file_path = "data/input_file_1.csv"

connection, cursor = create_in_memory_database()
load_data_into_database(cursor, csv_file_path)

cursor.execute('SELECT * FROM player_stats')
result = cursor.fetchall()

for row in result:
    print(row)

connection.close()

app = FastAPI()

# Include the router from the routers directory
app.include_router(main_router.router)