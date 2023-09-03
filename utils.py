import sqlite3

CiviPrompts = [
    'Pick a happy song!',
    'Pick a sad song!',
]

TraitorPrompts = [
    ('1', 'Pick a song that make you feel like dancing!'),
    ('1', 'Pick a song with a funky beat!'),
    ('2', 'Pick a song to play at a funeral!'),
    ('2', 'Pick a song to play when you\'re stressed out!'),
]


def initial_db_insert(conn: sqlite3.Connection):
    conn.executemany('INSERT INTO CiviPrompt(Prompt) VALUES(?)', map(lambda x: (x,), CiviPrompts))
    conn.executemany('INSERT INTO TraitorPrompt(CiviPromptId, Prompt) VALUES (?, ?)',
                     TraitorPrompts)
    conn.commit()


def get_rows(conn: sqlite3.Connection, cmd: str) -> list:
    cur: sqlite3.Cursor = conn.execute(cmd)
    return cur.fetchall()
