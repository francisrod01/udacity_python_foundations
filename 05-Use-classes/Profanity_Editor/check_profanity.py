#!~/envs/udacity-python-env

import urllib.request as request
import urllib.parse as parse

def read_text():
    quotes = open("./files/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url = "http://www.wdylike.appspot.com/?q=" + parse.quote(text_to_check)
    connection = request.urlopen(url)
    output = connection.read()
    print(output)
    connection.close()

read_text()
