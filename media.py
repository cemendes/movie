import webbrowser

class Movie():
    '''This class provides a way to store movie related information '''

    VALID_RATINGS = ["G", "PG", "PG-13","R" ]
    def __init__(self,move_title, movie_storyline, poster_image, trailer_youtube):
        '''This definition reads info about the movie as well as it trailer and poster image.'''
        self.title = move_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''This function calls the browser and plays the movie youtube trailer'''
        webbrowser.open(self.trailer_youtube_url)