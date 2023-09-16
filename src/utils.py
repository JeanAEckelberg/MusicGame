import sqlite3

CiviPrompts = [
    'Pick a happy song!',
    'Pick a sad song!',
    'Pick a funny song!',
    'Pick a hype song!',
    'Pick a rock song!',
]

TraitorPrompts = [
    ('1', 'Pick a song that make you feel like dancing!'),
    ('1', 'Pick a song with a funky beat!'),
    ('1', 'Pick a song you used to like a lot!'),
    ('1', 'Pick a song you like that you think the person being tested with you would like!'),
    ('2', 'Pick a song to play at a funeral!'),
    ('2', 'Pick a song to play when you\'re stressed out!'),
    ('2', 'Pick a song for a nighttime drive!'),
    ('2', 'Pick an emotional song!'),
    ('2', 'Pick a song you like that you think the person being tested with you would like!'),
    ('3', 'Pick a children\'s song!'),
    ('3', 'Pick a song that you would hear in a carnival!'),
    ('3', 'Pick a song you like that you think the person to your left would like!'),
    ('4', 'Pick a song that you repeat often!'),
    ('4', 'Pick a song you like that you think the person to your right would like!'),
    ('4', 'Pick a song with a meaningful message'),
    ('4', 'Pick a song that makes mundane tasks feel epic'),
    ('5', 'Pick a song for drive for a road trip!'),
    ('5', 'Pick a song you like that you think the person across from you would like!'),
    ('5', 'Pick a song that makes mundane tasks feel epic'),
    ('5', 'Pick a song you\'d workout to')

]


def initial_db_insert(conn: sqlite3.Connection):
    conn.executemany('INSERT INTO CiviPrompt(Prompt) VALUES(?)', map(lambda x: (x,), CiviPrompts))
    conn.executemany('INSERT INTO TraitorPrompt(CiviPromptId, Prompt) VALUES (?, ?)',
                     TraitorPrompts)
    conn.commit()


def get_rows(conn: sqlite3.Connection, cmd: str) -> list:
    cur: sqlite3.Cursor = conn.execute(cmd)
    return cur.fetchall()
