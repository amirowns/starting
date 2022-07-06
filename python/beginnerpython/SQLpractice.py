import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as connection:
    # can also do sqlite3.connect(":memory:") to temp store it
    with closing(connection.cursor()) as cursor:

        # what if it already exists?
        cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")

        cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
        cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

        rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
        print(rows)
        print("")

        target_fish_name = "Jamie"
        rows = cursor.execute(
            "SELECT name, species, tank_number FROM fish WHERE name = ?",
            (target_fish_name,)
        ).fetchall()
        print(rows)
        print("")

        new_tank_number = 2
        moved_fish_name = "Sammy"
        cursor.execute(
            "UPDATE fish SET tank_number = ? WHERE name = ?",
            (new_tank_number, moved_fish_name)
        )

        rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
        print(rows)

        released_fish_name = "Sammy"
        cursor.execute(
            "DELETE FROM fish WHERE name = ?",
            (released_fish_name,)
        )

        rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
        print(rows)