from random import *
import sqlite3
import utils


class Game:
    def __init__(self, conn: sqlite3, seed: int = Random().randint(0, 99999999), num_of_players: int = 1,
                 player_number=1):
        self.seed: int = seed
        self.rand: Random = Random(seed)
        self.num_of_players = num_of_players
        self.player_number = player_number
        self.traitor: bool = False
        self.conn: sqlite3.Connection = conn

    def run(self):
        input(f'Room Seed: {self.seed}\nMax Capacity: {self.num_of_players}\nPlayer No: {self.player_number}\nPress Enter to Begin...')
        while True:
            self.__round()
            if input('Next Round? (Y/n)') in 'Nn':
                break

    def __round(self):
        self.traitor = self.player_number == self.rand.randint(1, self.num_of_players)
        max: int = utils.get_rows(self.conn, "SELECT COUNT(1) FROM CiviPrompt")[0][0]

        prompt: str
        if self.traitor:
            prompt = Random().choice(utils.get_rows(self.conn,
                    f'SELECT Prompt from TraitorPrompt WHERE CiviPromptId = {self.rand.randint(1, max)}'))[0]
        else:
            prompt = utils.get_rows(self.conn, f'SELECT Prompt from CiviPrompt WHERE Id = {self.rand.randint(1, max)}')[0][0]

        print(f'Traitor: {self.traitor}')
        print(prompt)
        input('Press Enter on round end...')
