"""
This module contains functions for scraping dictionary data from specific websites.
"""
import textwrap
import argparse
import re
import requests
from bs4 import BeautifulSoup

# num of spaces before each line of print (styling purposes)
SPACE = 2

####################################
####### FUNCTION DEFINITIONS #######
####################################


def parse_word_arg():
    ''' parse command line arguments 

    Returns: 
    string: english word passed as an argument to cli 
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="word to look for")
    args = parser.parse_args()
    parsed_word = args.word

    return parsed_word


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


############
# UTILITIES
############

def print_divider():
    print("------------------------------")


def x_word_per_line(elements, x):
    lines_list = []

    for i in range(0, len(elements), x):
        lines_list.append(" ".join(elements[i:i+x]))
    return lines_list


def add_padding(line, space):
    ''' Returns a str line with left padding of 'space'
    '''
    return line.rjust(space + len(line))


def wrap_string(string):
    ''' Returns: a list of strings of max 80ch
    '''
    return textwrap.wrap(string, width=80)


def highlight_word(word, sentence):
    '''Returns:
       Sentence with word being red and bold'''
    return re.sub(rf"\b{word}\b",
                  "\033[1m\033[31m\\g<0>\033[0m", sentence.text.strip())


####################
####### MAIN #######
####################

def main():
    '''
    Print a definition of a word to the terminal
    '''
    eng_word = parse_word_arg()

    soup_reverso, soup_vocab = get_html(eng_word)

    ar_words_list = [
        el.text for el in soup_reverso.select("span.display-term")]
    eng_sents_el_list = soup_reverso.select("div.ltr span.text")
    short_def = soup_vocab.select("div.word-area p.short")[0].text
    long_def = soup_vocab.select("div.word-area p.long")[0].text

    sections_list = [
        x_word_per_line(ar_words_list, 5),
        wrap_string(short_def),
        wrap_string(long_def),
        [highlight_word(eng_word, sent) for sent in eng_sents_el_list]
    ]

    for section in sections_list:
        print_divider()
        for line in section:
            print(add_padding(line, SPACE))


if __name__ == '__main__':
    main()
