# %%
import os
import re
from lib.tone_marks import convert_from_numerical_pinyin
from lib.ce_database import create_connection, add_word_to_database
from lib.hsk_wordlist import get_word

# %%
cedict_path = os.path.abspath('raw_data/cedict_ts.u8')

# %%
content = []

with open(cedict_path, 'r') as cedict:

    for line in cedict:
        if '#' not in line:
            content.append(line)

# %%
cleaned_content = []
for entry in content:

    parsed = re.split(" \[|\]| \/|\/\\n", entry)

    traditional, simple = parsed[0].split(' ')
    english = parsed[3]

    try:
        pinyin = convert_from_numerical_pinyin(parsed[1])
    except:
        pinyin = parsed[1]

    try:
        hsk = get_word(simple)
    except:
        hsk = ''

    entry = {
        "traditional": traditional,
        "simplified": simple,
        "pinyin": pinyin,
        "english": english,
        "hsk": str(hsk)}

    cleaned_content.append(entry)

# %%
conn = create_connection('dictionary.sqlite')

for word in cleaned_content:

    with conn:
        word_to_insert = (
            word['traditional'],
            word['simplified'],
            word['pinyin'],
            word['english'],
            word['hsk'])

        add_word_to_database(conn, word_to_insert)

# %%
if __name__ == '__main__':
    pass
