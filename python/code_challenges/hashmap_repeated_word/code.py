import re
words_pattern = '[a-zA-Z]+'


def repeated_word(string: str) -> str:
    string =string.lower()
    array_of_words = re.findall(words_pattern, string, flags=re.IGNORECASE)
    dic = {}
    for word in array_of_words:
        if word in dic:
            return word

        else:
            dic[word] = 0


string = 'Once upon a time, there was a brave princess who'
first_repeated_word = repeated_word(string)
print(first_repeated_word)
