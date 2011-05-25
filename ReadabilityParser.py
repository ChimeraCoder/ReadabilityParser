from __future__ import division, print_function
import re

def whitespace_replacer(text):
    '''Replace all characters that are not letters in text with whitespace'''
    #This regex will remove punctuation (except periods), special characters, and numbers
    #Future versions should distinguish between decimal points and periods
    #Future versions should also distinguish between periods that delimit sentences and periods which designate letters of an acronym (like 'U.S.')
    regex = re.compile('[^A-Za-z. ]')
    return regex.sub(" ", text)

def sentence_splitter(text):
    '''Split text into a list of sentences'''
    #Remove whitespace
    text = whitespace_replacer(text)
    #Split along periods
    sentences = text.split('.')
    return sentences

def average_sentences_per_word(text):
    '''Determine the average number of sentences per word in a text'''
    
    sentences_list = sentence_splitter(text)
    num_sentences = len(sentences_list)
    num_words = 0
    for sentence in sentences_list:
        num_words += len(sentence.split())
    return num_sentences/num_words

def average_letters_per_word(text):
    '''Determine the average number of letters per word in the text'''
    #Create a list of all the words in the text
    words_list = text.split()
    num_words = len(words_list)
    total_characters = 0
    for word in words_list:
        total_characters += len(word)
    return total_characters/num_words

def coleman_liau(text):
    #Formula and notation taken from Wikipedia, by which L is average letters per 100 words, and S is average sentences per 100 words
    lpw = average_letters_per_word(text)
    spw = average_sentences_per_word(text)
    L = 100 * lpw
    S = 100 * spw
    return .0588 * L - .296 * S - 15.8

def main():
    pass

if __name__== '__main__': 
    main()
