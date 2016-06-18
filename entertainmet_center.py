import fresh_tomatoes
import media

toy_story = media.Movie("Toy STory",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=uZNHIU3uHT4")

big_fish = media.Movie("Big Fish",
                    "Story of a son and father",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/3/35/Big-fish-movie-poster.jpg/220px-Big-fish-movie-poster.jpg",
                    "https://www.youtube.com/watch?v=M3YVTgTl-F0")

movies = [toy_story, avatar, big_fish]
fresh_tomatoes.open_movies_page(movies)
