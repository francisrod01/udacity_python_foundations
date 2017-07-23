#!~/envs/udacity-python-env

def read_text():
    quotes = open("./files/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()


read_text()
