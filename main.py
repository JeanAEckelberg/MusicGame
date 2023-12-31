import sqlite3
import os
from src import game, utils


def set_up():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, 'src/MusicGame.db')
    conn = sqlite3.connect(db)
    conn.execute("DROP TABLE IF EXISTS CiviPrompt")
    conn.execute("DROP TABLE IF EXISTS TraitorPrompt")
    conn.execute("CREATE TABLE IF NOT EXISTS CiviPrompt(Id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 " Prompt TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS TraitorPrompt(Id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 " Prompt TEXT,"
                 "CiviPromptId INTEGER FORIEGN KEY REFERENCES CiviPrompt(Id))")

    utils.initial_db_insert(conn)

    return conn


def get_settings() -> dict:
    seed: int | None = 0
    num_of_players: int = 1
    player_num: int = 1

    while True:
        temp = input("Enter Room Seed (-1 for new room): ")
        try:
            seed = int(temp)
            break
        except Exception:
            pass

    while True:
        temp = input("Enter Number of Players: ")
        try:
            num_of_players = int(temp)
            break
        except Exception:
            pass

    while True:
        temp = input("Enter Player Number: ")
        try:
            player_num = int(temp)
            break
        except Exception:
            pass

    temp = {"num_of_players": num_of_players, "player_number": player_num}
    if seed != -1:
        temp["seed"] = seed
    return temp


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        conn = set_up()
        g = game.Game(conn, **get_settings())
        g.run()

    except Exception as e:
        input(e)
