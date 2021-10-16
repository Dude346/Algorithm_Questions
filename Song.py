'''
[s1 > s2 > s1 > s4] - True
[s1 > s2 > s3 > s4] - False

[s1 > s2 > s1] 
playlist = [s1, s2]
song = s1

[s1] 
playlist = [s1, None]
song = 
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

