class Folder:
    def __init__(self):

        with open("metin.txt", "r") as file:

            content = file.read()

            words = content.split()

            self.simple_words = list()

            for word in words:
                word = word.strip(",.\n'- ")

                self.simple_words.append(word)

    def all_words(self):

        words_set = set()

        for word in self.simple_words:

            words_set.add(word)

        print("----------All words------------------")

        for word in words_set:

            print(word)

    def how_many_words(self):
        self.word_dict = dict()

        for word in self.simple_words:
            if word in self.word_dict:
                self.word_dict[word.lower()] += 1
            else:
                self.word_dict[word.lower()] = 1

        for word, index in self.word_dict.items():

            print(f"'{word}' word pass {index} times \n")


    def findword(self):
        strings = []
        for word in self.simple_words:
            strings.append(word)
        print(strings)
        a = input("Enter a word to check:")

        if any(a in word for word in strings):
            print(f'{a} is there inside the list!')
        else:
            print(f'{a} is not there inside the list')





folder = Folder()
#folder.all_words()
#folder.how_many_words()
folder.findword()

