class Clip:
    year_released = 2021
    genre = "Unknown"

    def __init__(self, artist_name="Unknown", song_title="Unknown", duration=0, views=0, tvviews=0, allviews=0):
        self.__artist_name = artist_name
        self.__song_title = song_title
        self.__duration = duration
        self.__views = views
        self.__tvviews = tvviews
        self.__allviews = views + tvviews

    def get_artist_name(self):
        return self.__artist_name

    def set_artist_name(self, artist_name):
        self.__artist_name = artist_name

    def get_song_title(self):
        return self.__song_title

    def set_song_title(self, song_title):
        self.__song_title = song_title

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_views(self):
        return self.__views

    def set_views(self, views):
        self.__views = views
        self.set_allviews()
    
    def get_tvviews(self):
        return self.__tvviews
    
    def set_tvviews(self, tvviews):
        self.__tvviews = tvviews
        self.set_allviews()

    def get_allviews(self):
        return self.__allviews
    
    def set_allviews(self, allviews):
        self.__allviews = self.__views + self.__tvviews

    def __str__(self):
        return f"Clip('{self.__artist_name}', '{self.__song_title}', {self.__duration} sec, {self.__views} views, {self.__tvviews} tv views, {self.__allviews} all views)"

    def __repr__(self):
        return f"Clip(artist_name={self.__artist_name}, song_title={self.__song_title}, duration={self.__duration}, views={self.__views})"

    def __del__(self):
        print(f"Clip '{self.__song_title}' by '{self.__artist_name}' is being deleted.")

if __name__ == "__main__":
    clip1 = Clip("Artist1", "Song1", 210, 1000000, 500000)
    clip2 = Clip("Artist2", "Song2", 180, 500000, 100000)
    clip3 = Clip("Artist3", "Song3", 240, 2000000, 1000000)

    print(clip1)
    print(clip2)
    print(clip3)

    

    print("Clip1 artist name:", clip1.get_artist_name())
    print("Clip2 song title:", clip2.get_song_title())
    print("Clip3 views:", clip3.get_views())
    print("Clip1 all views:", clip1.get_allviews())
