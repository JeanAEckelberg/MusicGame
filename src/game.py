from random import *
from src.utils import *
import os
import platform
from typing import Callable


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
        os_cls: Callable[[], int] = lambda: os.system('cls' if platform.system() == 'Windows' else 'clear')
        input(
            f'Room Seed: {self.seed}\nMax Capacity: {self.num_of_players}\nPlayer No: {self.player_number}\nPress Enter to Begin...')
        os_cls()
        while True:
            self.__round(os_cls)
            if input('Next Round? (Y/n)') not in 'Yy':
                break

    def __round(self, os_cls: Callable[[], int]):
        self.traitor = self.player_number == self.rand.randint(1, self.num_of_players)

        while True:
            self.__test()
            if input('Next Test? (Y/n)') not in 'Yy':
                break
            os_cls()

    def __test(self):
        max: int = get_rows(self.conn, 'SELECT COUNT(1) FROM CiviPrompt')[0][0]
        prompt: str
        r = self.rand.randint(1, max)

        print(f'Traitor: {self.traitor}')

        if self.traitor:
            prompt = Random().choice(get_rows(self.conn,
                    f'SELECT Prompt from TraitorPrompt WHERE CiviPromptId = {r}'))[0]
        else:
            prompt = get_rows(self.conn, f'SELECT Prompt from CiviPrompt WHERE Id = {r}')[0][0]

        print(prompt)
        input('Press Enter on round end...')

        if self.traitor:
            print(f'Civilian Prompt: { get_rows(self.conn, f"SELECT Prompt from CiviPrompt WHERE Id = {r}")[0][0]}')
