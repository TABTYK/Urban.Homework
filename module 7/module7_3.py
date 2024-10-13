import re


class WordsFinder():
    def __init__(self,*file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = dict()
        spisok_slov = list()
        for x in self.file_names:
            #print(type(x))
            #print(x)
            with open(x,encoding = 'utf-8') as file:
                for line in file:
                    string = re.sub(r'[^a-zA-Zа-яА-Я0-9\s]+','',line)
                    spisok_slov.append(string.split())
            all_words[x] = spisok_slov
        return all_words

    def count(self,word):
        test = self.get_all_words()
        count_all_words = dict()
        for x in test.keys():
            count_words_2 = 0
            for spisok in test[x]:
                count_words = spisok.count(word.lower())
                count_words_2 += count_words
            count_all_words[x] = count_words_2
        return count_all_words


    def find(self,word):
        find_out_from_the_hell = self.get_all_words()
        number_string = 0
        result = dict()
        for x in find_out_from_the_hell.keys():
            index_string = None
            for spisok in find_out_from_the_hell[x]:
                for peremennaya in spisok:
                    if peremennaya.lower() == word.lower():
                        index_string = spisok.index(peremennaya) + 1
                        break
                if index_string != None:
                    #number_string = x.index(spisok)
                    break
            result[x] = index_string
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('texT')) # 4 слова teXT в тексте всего

