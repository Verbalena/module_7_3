# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
# Задача "Найдёт везде"

class WordsFinder:
      #  список или кортеж из неограниченного количество названий файлов
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):    # возвращает словарь следующего вида:{'file1.txt': ['word1', 'word2']}
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, mode='r', encoding='utf8') as file:  # Переберите названия файлов и открывайте каждый из них,
                content = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(i, ' ')
            words = content.split()
            all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words() # принимаем результат метода get_all_words()
        for key, value in all_words.items():
            if word in value:
                result[key] = value.index(word)
            else:
                result[key] = -1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for key, value in all_words.items():
            result[key] = value.count(word.lower())
        return result


file_1 = 'test_file.txt'
f1 = WordsFinder(file_1)
print(f1.get_all_words())
print(f1.find('TEXT'))
print(f1.count('teXT'))
