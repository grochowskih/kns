from app.classes.computer.ComputerPlayer import ComputerPlayer
import random


class RandomComputerPlayer(ComputerPlayer):

    def choose_letter(self, gameplay):
        return random.sample(gameplay.alphabet, 1)
