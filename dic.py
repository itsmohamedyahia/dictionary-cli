"""
This module contains functions for scraping dictionary data from specific websites.
"""
import textwrap
import argparse
import re
import requests
from bs4 import BeautifulSoup
SPACE = 2

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


def get_html(word):
    ''' get html page content of context.reverso.net and vocabulary.com of given word
    '''
    url_reverso = f"https://context.reverso.net/translation/english-arabic/{word}"
    url_vocab = f"https://www.vocabulary.com/dictionary/{word}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    # Send an HTTP GET request to the URL
    response_reverso = requests.get(url_reverso, headers=headers)
    response_vocab = requests.get(url_vocab, headers=headers)
    # Parse the HTML content of the response using BeautifulSoup
    soup_reverso = BeautifulSoup(response_reverso.content, "html.parser")
    soup_vocab = BeautifulSoup(response_vocab.content, "html.parser")
    return soup_reverso, soup_vocab


def print_words_arabic(words_ar_divs):
    ''' Print 5 Arabic words per line, words are seperated by a space
    '''
    print("------------------------------")
    for i in range(0, len(words_ar_divs), 5):
        line = " ".join(words_ar_divs[i:i+5])
        print(line.rjust(SPACE + len(line)))
    print("------------------------------")


def print_definitions(def_divs):
    ''' Print English definitions wrapped at 80 characters
    '''
    def_wrapped_list = textwrap.wrap(def_divs[0].text, width=80)
    for line in def_wrapped_list:
        line_spc = line.rjust(SPACE + len(line))
        print(line_spc)
    print("------------------------------")


def print_examples(sents_eng_divs, word_eng):
    ''' Print English example sentences with the search word highlighted in bold and red
    '''
    for sent in sents_eng_divs:
        sent_bold = re.sub(rf"\b{word_eng}\b",
                           "\033[1m\033[31m\\g<0>\033[0m", sent.text.strip())
        print(sent_bold.rjust(SPACE + len(sent_bold)))
    print("------------------------------")

####################
####### MAIN #######
####################


def main():
    word_eng = parse_word_arg()

    soup_reverso, soup_vocab = get_html(word_eng)

    words_ar_divs = [
        span.text for span in soup_reverso.select("span.display-term")]
    sents_eng_divs = soup_reverso.select("div.ltr span.text")
    def1_divs = soup_vocab.select("div.word-area p.short")
    def2_divs = soup_vocab.select("div.word-area p.long")

    print_words_arabic(words_ar_divs)
    print_definitions(def1_divs)
    print_definitions(def2_divs)
    print_examples(sents_eng_divs, word_eng)


if __name__ == '__main__':
    main()
