from app.classes.computer.ComputerPlayer import ComputerPlayer


class ExclusivePlayer(ComputerPlayer):

    def choose_letter(self, gameplay):
        non_repetition = set()
        word = gameplay.get_word()
        ComputerPlayer.add_non_repetitive(gameplay.alphabet, word, non_repetition)
        if not non_repetition:
            return word[len(word)-1]
        else:
            return ComputerPlayer.return_random(non_repetition)
