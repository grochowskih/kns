from classes.computer.ComputerPlayer import ComputerPlayer


class ForeseeingPlayer(ComputerPlayer):

    def choose_letter(self, gameplay):
        non_repetition = set()
        word = gameplay.get_word()
        ComputerPlayer.add_non_repetitive(gameplay.alphabet, word, non_repetition)
        if not non_repetition:
            return word[len(word)-1]
        else:
            short_repetition = set()
            for element in non_repetition:
                new_word = word+element
                is_non_repetitive = True
                for letter in gameplay.alphabet:
                    is_non_repetitive = ComputerPlayer.check_for_long_repetition(new_word, letter)
                if is_non_repetitive:
                    short_repetition.add(element)
            if not short_repetition:
                return ComputerPlayer.return_random(non_repetition)
            return ComputerPlayer.return_random(short_repetition)
