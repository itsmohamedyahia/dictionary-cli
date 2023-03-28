import requests
from bs4 import BeautifulSoup
import re
import argparse
import textwrap

####################################
####### FUNCTION DEFINITIONS #######
####################################


def parse_word_arg():
    ''' parse command line arguments 

    Returns: 
    string: english word passed as an argument to cli '''

    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="word to look for")
    args = parser.parse_args()
    word_eng = args.word

    return word_eng


word_eng = parse_word_arg()

url_reverso = f"https://context.reverso.net/translation/english-arabic/{word_eng}"
url_vocab = f"https://www.vocabulary.com/dictionary/{word_eng}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Send an HTTP GET request to the URL
response_reverso = requests.get(url_reverso, headers=headers)
response_vocab = requests.get(url_vocab, headers=headers)
# Parse the HTML content of the response using BeautifulSoup
soup_reverso = BeautifulSoup(response_reverso.content, "html.parser")
soup_vocab = BeautifulSoup(response_vocab.content, "html.parser")

with open('output.html', 'w') as file:
    # Write text to the file
    file.write(f"{soup_reverso}\n")


with open('output_vocab.html', 'w') as file:
    # Write text to the file
    file.write(f"{soup_vocab}\n")


# Find all the divs that contain the definitions and examples
words_ar_divs = soup_reverso.select("span.display-term")
sents_eng_divs = soup_reverso.select("div.ltr span.text")

# Find vocab
def1_divs = soup_vocab.select("div.word-area p.short")
def2_divs = soup_vocab.select("div.word-area p.long")

# Print the definitions and examples

words_ar = [span.text for span in words_ar_divs]
sents_eng = [span.text.strip() for span in sents_eng_divs]

# print vocab

def1_eng = [item.text for item in def1_divs]
def2_eng = [item.text for item in def2_divs]


space = 2


print("------------------------------")
for i in range(0, len(words_ar), 5):
    line = " ".join(words_ar[i:i+5])
    print(line.rjust(space + len(line)))

print("------------------------------")

# for dfntn in def1_eng:
#     dfntn_wrapped_list = textwrap.wrap(dfntn, width=80)

dfntn1_wrapped_list = textwrap.wrap(def1_eng[0], width=80)

for line in dfntn1_wrapped_list:
    line_spc = line.rjust(space + len(line))
    print(line_spc)


print("------------------------------")

dfntn2_wrapped_list = textwrap.wrap(def2_eng[0], width=80)

for line in dfntn2_wrapped_list:
    line_spc = line.rjust(space + len(line))
    print(line_spc)

print("------------------------------")

for sent in sents_eng:
    sent_bold = re.sub(rf"\b{word_eng}\b",
                       "\033[1m\033[31m\\g<0>\033[0m", sent)
    print(sent_bold.rjust(space + len(sent_bold)))
print("------------------------------")
