import sqlite3
import json
from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())

with sqlite3.connect("db.sqlite3") as conn:
    # command = "INSERT INTO Movies VALUES(?, ?, ?)"
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # Alternative way of printing out the DB results.
    # for row in cursor:
    #     print(row)

    # for movie in movies:
    #     conn.execute(command, tuple(movie.values()))
    # conn.commit() #Only needed when writing to the database.
    movies = cursor.fetchall()
    print(movies)
