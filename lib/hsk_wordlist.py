# %%
import csv
import os


# %%
wordlist_path = os.path.abspath('raw_data/cleaned_hsk_words.csv')

with open(wordlist_path) as wordlist:

    csv_parsed = csv.reader(wordlist, delimiter=',')

    content = {line[0]: line[2] for line in csv_parsed}

# %%


def get_word(word):
    return content[word]


# %%
if __name__ == '__main__':
    print(get_word('甚至'))
