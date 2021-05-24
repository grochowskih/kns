from classes.computer.RandomComputerPlayer import RandomComputerPlayer
from classes.gameplay.Gameplay import Gameplay
import pandas as pd

if __name__ == "__main__":

    results = pd.DataFrame(columns=["alphabet_length", "word_length", "game_time", "winner"])
    for i in range(10):
        print("Start test app for i = " + str(i))
        alphabet_length = 15
        alphabet = [chr(i) for i in range(97, 97 + alphabet_length)]

        word_length = 35
        game_time = 80

        type = "3"
        pseudo_real_player = RandomComputerPlayer()
        gameplay = Gameplay(pseudo_real_player, alphabet_length, alphabet, word_length, game_time, type)

        while True:
            computer_letter = gameplay.get_computer_player().choose_letter(gameplay)
            print("Ruch gracza komputerowego. Komputer kladzie literę " + computer_letter)
            gameplay.add_letter(computer_letter)
            print("Obecnie słowo to: ")
            print(gameplay.get_word())
            if gameplay.check_end_game() in [1,2]:
                print("Dodaję do df")
                df_to_add = pd.DataFrame({"alphabet_length" : [alphabet_length] , "word_length" : [word_length], "game_time" : [game_time], "winner" : [gameplay.check_end_game()]})
                results = results.append(df_to_add, ignore_index=True)
                break
            print("Ruch gracza pseudorzeczywistego. Dopisz literę do słowa: ")
            letter = gameplay.get_real_player().choose_letter(gameplay)
            gameplay.add_letter(letter)
            print("Obecnie słowo to: ")
            print(gameplay.get_word())
            gameplay.set_current_round()
            if gameplay.check_end_game() in [1,2]:
                print("Dodaję do df")
                df_to_add = pd.DataFrame({"alphabet_length" : [alphabet_length] , "word_length" : [word_length], "game_time" : [game_time], "winner" : [gameplay.check_end_game()]})
                results = results.append(df_to_add, ignore_index=True)
                break
    results.head(10)
    results.to_csv("Wyniki15-35-80.csv")