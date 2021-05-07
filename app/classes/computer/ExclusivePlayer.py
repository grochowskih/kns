from app.classes.computer.ComputerPlayer import ComputerPlayer
from app.functions.MathFunctions import is_repetition
import random


class ExclusivePlayer(ComputerPlayer):

    def choose_letter(self, gameplay):
        non_repetition = set()
        word = gameplay.get_word()
        for k in range(0, len(gameplay.alphabet)-1):
            if not is_repetition(word+gameplay.alphabet[k]):
                non_repetition.add(gameplay.alphabet[k])
        if not non_repetition:
            return gameplay.get_word()[len(gameplay.get_word())-1]
        else:
            return random.sample(non_repetition, 1)
