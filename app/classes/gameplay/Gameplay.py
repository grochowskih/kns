from classes.computer.ExclusivePlayer import ExclusivePlayer
from classes.computer.ForeseeingPlayer import ForeseeingPlayer
from classes.computer.RandomComputerPlayer import RandomComputerPlayer
from functions.MathFunctions import is_repetition, begin_repetition



class Gameplay:
    def __init__(self, real_player, alphabet_length, alphabet,  word_length, game_time, computer_player):
        self.real_player = real_player
        self.alphabet_length = alphabet_length
        self.word_length = word_length
        if computer_player == "1":
            self.computer_player = RandomComputerPlayer()
        elif computer_player == "2":
            self.computer_player = ExclusivePlayer()
        elif computer_player == "3":
            self.computer_player = ForeseeingPlayer()
        self.word = ""
        self.game_time = game_time
        self.current_round = 1
        self.alphabet = alphabet

    def set_word(self, word):
        self.word = word

    def get_word(self):
        return self.word

    def get_computer_player(self):
        return self.computer_player

    def get_real_player(self):
        return self.real_player

    def set_current_round(self):
        self.current_round = self.current_round + 1

    def add_letter(self, letter):
        self.set_word(self.word+letter)
        self.update_word()

    def update_word(self):
        if is_repetition(self.word):
            print("Wystąpiła repetycja!")
            begin = begin_repetition(self.word)
            self.set_word(self.word[0:begin])

    def check_end_game(self):
        if len(self.word) >= self.word_length:
            print("Koniec gry, wygrał gracz komputerowy!")
            return True
        elif self.current_round > self.game_time:
            print("Wygrał gracz rzeczywisty, brawo!")
            return True
        else:
            print("Nie ma zwycięzcy, gra toczy się dalej.")
            return False
        return False




