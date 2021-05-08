from app.classes.computer.ComputerPlayer import ComputerPlayer
from app.functions.MathFunctions import is_repetition, begin_repetition
import random

class ForeseeingPlayer(ComputerPlayer):

    def choose_letter(self, gameplay):
        non_repetition = set()
        word = gameplay.get_word()
        for k in range(0, len(gameplay.alphabet)-1):
            if not is_repetition(word+gameplay.alphabet[k]):
                non_repetition.add(gameplay.alphabet[k])
        if not non_repetition:
            return gameplay.get_word()[len(gameplay.get_word())-1]
        else:
            short_repetition = set()
            for k in range(0, len(non_repetition) - 1):
                new_word = word + non_repetition[k]
                is_non_repetitive = True
                for m in range (0, len(gameplay.alphabet)-1):
                    if is_repetition(new_word+gameplay.alphabet[m]):
                        if begin_repetition(new_word+gameplay.alphabet[m]) < len(new_word+gameplay.alphabet[m])-2:
                            is_non_repetitive = False
                if is_non_repetitive:
                    short_repetition.add(gameplay.alphabet[k])
            if not short_repetition:
                return random.sample(non_repetition, 1)
            return random.sample(short_repetition, 1)
