from classes.gameplay.Gameplay import Gameplay
from classes.real.RealPlayer import RealPlayer
from functions.UserInteraction import input_alphabet_length
from colorama import Fore, Back, Style

computer_players = {"1": "Losowy", "2": "Wykluczający", "3": "Przewidujący"}

if __name__ == "__main__":
    print("Witamy w grze Thuego. Wybierz rodzaj gracza komputerowego, z jakim się zmierzysz.")
    type = input("Jeśli chcesz zmierzyć się z graczem losowym - wybierz 1. Jeśli chcesz zmierzyć się z graczem wykluczajacym - wybierz 2. Jeśli chcesz zmierzyć się z graczem przewidującym - wybierz 3.")
    while type not in ["1", "2", "3"]:
        print("Dokonano zlego wyboru! Jeszcze raz!")
        type = input("Jeśli chcesz zmierzyć się z graczem losowym - wybierz 1. Jeśli chcesz zmierzyć się z graczem wykluczajacym - wybierz 2. Jeśli chcesz zmierzyć się z graczem przewidującym - wybierz 3.")
    print("Wybrałeś gracza komputerowego rodzaju: " + computer_players[type])

    try:
        alphabet_length = input_alphabet_length()
    except:
        print("Błędne dane. Ustawiam długość na 10.")
        alphabet_length = 10
    alphabet = [chr(i) for i in range(97, 97+alphabet_length)]

    print("Wybrany przez Ciebie alfabet to: " + str(alphabet))
    word_length = int(input("Wybierz dlugosc slowa, ktore konczy gre: "))
    # dolozyc obsluge wyjatku i wgl moze ladniej

    game_time = int(input("Wybierz przez ile rund ma toczyc sie gra: "))
    real_player = RealPlayer()

    gameplay = Gameplay(real_player, alphabet_length, alphabet,  word_length, game_time, type)

    while True:
        print("Obecnie słowo to: ")
        print(Fore.RED + gameplay.get_word())
        print(Style.RESET_ALL)
        print("Ruch gracza rzeczywistego. Połóż literę do słowa")
        letter = gameplay.get_real_player().choose_letter(alphabet)
        gameplay.add_letter(letter)
        print("Obecnie słowo to: ")
        print(Fore.RED + gameplay.get_word())
        print(Style.RESET_ALL)
        if gameplay.check_end_game():
            break
        print("Ruch gracza komputerowego.")
        computer_letter = gameplay.get_computer_player().choose_letter(gameplay)
        print("Komputer kladzie literę " + computer_letter)
        gameplay.add_letter(computer_letter)
        print("Obecnie słowo to: ")
        print(Fore.RED + gameplay.get_word())
        print(Style.RESET_ALL)
        if gameplay.check_end_game():
            break

