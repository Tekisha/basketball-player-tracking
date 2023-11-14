# app/main_routers.py

from fastapi import FastAPI
from app.api.routers import main_routers as main_router
from app.repositories.player_repository import create_in_memory_database, load_data_into_database, PlayerRepository

app = FastAPI()

# Include the router from the routers directory
app.include_router(main_router.router)


def setup_database():
    # Setup in-memory database and load data
    csv_file_path = "data/input_file_1.csv"
    connection, cursor = create_in_memory_database()
    load_data_into_database(cursor, csv_file_path)

    # Print loaded data
    cursor.execute('SELECT * FROM player_stats')
    result = cursor.fetchall()
    for row in result:
        print(row)

    # Close the database connection
    connection.close()

    return PlayerRepository(cursor)


# Run the setup_database function when the script is executed
setup_database()


