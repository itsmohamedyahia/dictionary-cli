import requests
from bs4 import BeautifulSoup
import sys

word_eng = sys.argv[1]

# word_eng = input("what's the word?")

url = f"https://context.reverso.net/translation/english-arabic/{word_eng}"

# url = "https://context.reverso.net/translation/english-arabic/easy"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Send an HTTP GET request to the URL
response = requests.get(url, headers=headers)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")


with open('output.html', 'w') as file:
    # Write text to the file
    file.write(f"{soup}\n")

# Find all the divs that contain the definitions and examples
words_ar_divs = soup.select("span.display-term")


sents_eng_divs = soup.select("div.ltr span.text")

# Print the definitions and examples

words_ar = [span.text for span in words_ar_divs]
sents_eng = [span.text.strip() for span in sents_eng_divs]
# print(words_ar)
print(sents_eng)

# for item in sents_eng_divs:


# print(type(sents_eng_divs[0]))

# for example in examples:
#     print(example.text.strip())
