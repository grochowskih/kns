class RealPlayer:

    def choose_letter(self, alphabet):
        letter = input("Podaj literę: ")
        while letter not in alphabet:
            letter = input("Litera nie z alfabetu. Podaj literę: ")
        return letter