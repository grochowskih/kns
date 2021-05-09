from functions.MathFunctions import is_repetition, begin_repetition
import random


class ComputerPlayer:

    def choose_letter(self, gameplay):
        """
        :param gameplay: obiekt klasy Gameplay realizujący rozgrywkę
        :return: litera, ktora mamy dodac do slowa wg komputera
        """
        pass

    @staticmethod
    def return_random(collection):
        """
        :param collection: dowolny zbiór
        :return: element ze zbioru wybrany losowo
        """
        return random.choice(tuple(collection))

    @staticmethod
    def add_non_repetitive(alphabet, word, collection):
        """
        :param alphabet: zbiór słow
        :param word: pewne słowo składające się z liter z alphabet
        :param collection: zbiór liter z alphabet dla których po dopisaniu do word nie powstanie repetycja
        :return: element ze zbioru wybrany losowo
        """
        for element in alphabet:
            if not is_repetition(word+element):
                collection.add(element)

    @staticmethod
    def check_for_long_repetition(word, letter):
        """
        :param word: pewne słowo
        :param letter: pewna litera
        :return: False jeśli po dopisaniu letter to word wystąpi repetycja dłuższa niż 1, True wpp
        """
        if is_repetition(word + letter):
            if begin_repetition(word + letter) < len(word + letter) - 2:
                return False
        return True
