#!~/envs/udacity-python-env

import media
import fresh_tomatoes

title = "Toy Story"
movie_storyline = "A story of a boy and his toys that come to life"
poster_image = "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=vwyZH85NQC4"

toy_story = media.Movie(title, movie_storyline, poster_image, trailer_youtube)
# print(toy_story.storyline)

##################

title = "Avatar"
movie_storyline = "A marine on an alien planet"
poster_image = "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=-9ceBgWV8io"

avatar = media.Movie(title, movie_storyline, poster_image, trailer_youtube)
# print(avatar.storyline)
# avatar.show_trailer()

##################

title = "Vikings - Season 5"
movie_storyline = "Vikings is inspired by the sagas of Viking Ragnar Lothbrok"
poster_image = "https://upload.wikimedia.org/wikipedia/en/9/99/Vikings_Title.png"
trailer_youtube = "https://www.youtube.com/watch?v=Ts_8uk1ddJI"

vikings = media.Movie(title, movie_storyline, poster_image, trailer_youtube)
# vikings.show_trailer()

##################

title = "School of Rock"
movie_storyline = "Storyline"
poster_image = "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=3PsUJFEBC74"

school_of_rock = media.Movie(title, movie_storyline, poster_image, trailer_youtube)

##################

title = "Midnight in Paris"
movie_storyline = "Storyline"
poster_image = "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=atLg2wQQxvU"

midnight_in_paris = media.Movie(title, movie_storyline, poster_image, trailer_youtube)

##################

title = "Hunger Games"
movie_storyline = "Storyline"
poster_image = "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=PbA63a7H0bo"

hunger_games = media.Movie(title, movie_storyline, poster_image, trailer_youtube)

##################

movies = [toy_story, avatar, vikings, school_of_rock, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
