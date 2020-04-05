import nltk
from nltk import word_tokenize
import re
import inflect

f=open('magazine.txt','r')

def get_text(file):
#   normalizing whitespace
    text = open(file).read()
    text = re.sub('\s+', ' ', text)
    return text

def get_words(f):
    text=f.read()
    words = nltk.word_tokenize(text)
    return words

def find_number_and_convert_word(words):
    c = 0
    for i in words:
        if i.isdigit():
            i = inflect.engine().number_to_words(i)
            words[c] = i
        c += 1
    return words

def get_final_text(words) :
    finalText = ''
    for i in words:
        finalText += i + " "
    print(finalText)
    newFile = open("final.txt", "w+")
    newFile.write(finalText)


contents = get_text("magazine.txt")
words = get_words(f)
changed_words = find_number_and_convert_word(words)
get_final_text(changed_words)




