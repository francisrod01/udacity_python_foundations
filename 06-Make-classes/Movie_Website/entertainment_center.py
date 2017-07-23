#!~/envs/udacity-python-env

import media

title = "Toy Story"
movie_storyline = "A story of a boy and his toys that come to life"
poster_image = "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=vwyZH85NQC4"

toy_story = media.Movie(title, movie_storyline, poster_image, trailer_youtube)
# print(toy_story.storyline)

title = "Avatar"
movie_storyline = "A marine on an alien planet"
poster_image = "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=-9ceBgWV8io"

avatar = media.Movie(title, movie_storyline, poster_image, trailer_youtube)
print(avatar.storyline)
