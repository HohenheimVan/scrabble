import random


SCRABBLES_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                    (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in SCRABBLES_SCORES
                 for letter in letters.split()}


class Dictionary(object):
    def __init__(self, path):
        with open(path) as file:
            self.words_list = [Word(line.rstrip("\n")) for line in file if Word(line.rstrip("\n")).score]

    def find_best_word(self):
        """Return most valuable word and the score as a str"""
        max_score = max([word.score for word in self.words_list])
        best_word = self.find_word_by_score(max_score)
        rep = str(max_score) + " " + str(best_word)
        return rep

    def find_word_by_score(self, score_to_find):
        """return from words list a random word with a certain(score_to_find) number of points
        if word doesn't exist return none"""
        try:
            score_to_find = int(score_to_find)
        except ValueError:
            print("Nieodpowiednia liczba")
        expected_words = [word for word in self.words_list if word.compare_score(score_to_find)]
        if not expected_words:
            return None
        elif len(expected_words) >= 1:
            found_word = random.choice(expected_words)
        else:
            found_word = expected_words[0]
        return found_word


class Game(Dictionary):
    def __init__(self, path="dictionary.txt"):
        super(Game, self).__init__(path)

    def check_score_by_word(self):
        """print word and score"""
        string = input("Podaj słowo, dla którego chcesz poznać wynik: ")
        word = Word(string)
        if not word.score:
            print("Słowo zawiera niedozwolone znaki")
        else:
            print("Wynik dla słowa", word, "to", word.score)

    def check_word_by_score(self):
        """print word with given value"""
        score_to_find = input("Podaj ilość pkt: ")
        found_word = self.find_word_by_score(score_to_find)
        if found_word:
            print(found_word)
        else:
            pass

    def print_menu(self):
        print("\n\tMENU\n")
        print("1. Zwraca najwyższy wynik z pliku dictionary.txt\n"
              "2. Liczy wynik dla słowa podanego jako argument z linii komend\n"
              "3. Zwróci słowo o podanej wartości:\n"
              "\tjeśli istnieje wiele słów, wybierze losowe\n"
              "\tb) jeśli nie istnieje takie słowo, nie wyświetli niczego")
        print("Aby zakończyć wpisz 'q'.")

    def check_best_score(self):
        print(self.find_best_word())


class Word(object):
    def __init__(self, string):
        self.string = string.upper()

    def compare_score(self, score_to_find):
        """check if word.score is the same as given score, return word object if True, return None if False"""
        if self.score == score_to_find:
            return self
        else:
            return None

    @property
    def score(self):
        score = 0
        for character in self.string:
            if character not in LETTER_SCORES:
                return None
            else:
                score += LETTER_SCORES[character]
        return score

    def __str__(self):
        return self.string


def main():
    scrabble = Game("dictionary.txt")
    order = None
    while order != "q":
        scrabble.print_menu()
        order = input("Wybór: ")
        if order == "1":
            scrabble.check_best_score()
        elif order == "2":
            scrabble.check_score_by_word()
        elif order == "3":
            scrabble.check_word_by_score()
        elif order == "q":
            print("Bye Bye")
        else:
            print("wystąpił błąd, podaj 1, 2, 3 lub q")


if __name__ == '__main__':
    main()
