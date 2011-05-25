from __future__ import division, print_function
import re



def whitespace_replacer(text):
    '''Replace all characters that are not letters in text with whitespace'''
    regex = re.compile('[^A-Za-z ]')
    return regex.sub(" ", text)




def main():
    pass


if __name__== '__main__': 
    main()
