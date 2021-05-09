def input_alphabet_length():
    alphabet_length = int(input("Wybierz długość alfabetu, na jakim ma rozgrywać się rozgrywka: "))
    if alphabet_length <= 0:
        print("Długość alfabetu nie może być ujemna. Ustawiam długość na 10")
        alphabet_length = 10
    return alphabet_length