from abc import ABC, abstractmethod
class MusicPlayer(ABC):
    @abstractmethod
    def open_music(self):
        pass

    @abstractmethod
    def play_music(self):
        pass

    @abstractmethod
    def close_music(self):
        pass

class SpotifyMusicPlayer(MusicPlayer):
    def open_music(self):
        print("Open Spotify")
    def play_music(self):
        print("Play music in Spotify")
    def close_music(self):
        print("Close Spotify")