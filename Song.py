'''
https://www.testdome.com/questions/javascript/song/48414

A playlist is considered a repeating playlist if any of the songs contain a reference to a previous song in the playlist. Otherwise, the playlist will end with the last song which points to undefined.

Implement the method isRepeatingPlaylist that, efficiently with respect to time used, returns true if a playlist is repeating or false if it is not.
'''

class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        song = self
        playlist = {song}

        while True: 
            try: 
                song = song.next 
            
            except AttributeError:
                return False 

            else: 
                if song in playlist: 
                    return True 
                
                else:
                    playlist.add(song)

            

            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())

