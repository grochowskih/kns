from classes.computer.ComputerPlayer import ComputerPlayer


class RandomComputerPlayer(ComputerPlayer):

    def choose_letter(self, gameplay):
        return ComputerPlayer.return_random(gameplay.alphabet)
