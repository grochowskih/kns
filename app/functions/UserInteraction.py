import math

def input_alphabet_length():
    alphabet_length = int(input("Wybierz liczbę liter w alfabecie dostępnym podczas rozgrywki: "))
    while alphabet_length < 1 and alphabet_length > 26:
            print("Długość alfabetu musi być liczbą z przedziału [2,26]! Spróbuj jeszcze raz!")
            alphabet_length = int(input("Wybierz długość alfabetu, na jakim ma rozgrywać się rozgrywka: "))
    return alphabet_length

def input_word_length():
    word_length = int(input("Wybierz dlugość słowa, której osiągnięcie skończy grę: "))
    while word_length < 2:
        print("Długość słowa musi być większa od 1! Spróbuj jeszcze raz!")
        word_length = int(input("Wybierz długość słowa, której osiągnięcie skończy grę: "))
    return word_length

def input_game_time(word_length):
    game_time = int(input("Wybierz przez ile rund ma toczyć sie gra: "))
    while game_time < word_length:
        print("Rund musi być co najmniej tyle ile wynosi długość słowa! Spróbuj jeszcze raz!")
        game_time = int(input("Wybierz przez ile rund ma toczyć sie gra: "))
    return game_time