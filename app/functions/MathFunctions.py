import math

def word_loop(word):
    first_parts = set()
    second_parts = set()
    for k in range(1, math.floor(len(word) / 2) + 1):
        first_parts.add(word[len(word) - 2 * k : len(word) - k])
        second_parts.add(word[len(word) - k : len(word)])
    return [first_parts, second_parts]

def is_repetition(word):
    """
    :param word: slowo, w ktorym sprawdzamy czy jest repetycja
    :return: True, jesli jest, False, jesli nie ma
    """
    loop_result = word_loop(word)
    if (loop_result[0] & loop_result[1]):
        return True
    else:
        return False

def begin_repetition(word):
    """
    :param word: slowo w ktorym wystepuje repetycja
    :return: zwraca na ktorej pozycji w slowie sie zaczyna repetycja z konca (czyli np abab zwraca 2, bo 0=a, 1=b, 2=a i tu sie zaczyna)
    """
    loop_result = word_loop(word)
    common_part = list(loop_result[0] & loop_result[1])
    return len(word)-len(common_part[0])
