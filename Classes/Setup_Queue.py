# Creates queue 
class Setup_Queue:
    def __init__(self):
        # Define attributes for queue
        self.volume = 1.0 # Volume to play at
        self._queue = [] # The server's queue/playlist
        self.vote_skip = set() # Keep track of skip votes
        self.now_playing = None # Current playing audio
        self.next_song = None # Next song
        self.playeer = None # Current player
    
    # ---------------------------------------------------

    # Get the requestor of audio
    def is_requestor(self, user):
        return self.now_playing.requested_by == user

    # ---------------------------------------------------
    