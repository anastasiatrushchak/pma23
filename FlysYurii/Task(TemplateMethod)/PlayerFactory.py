from abc import ABC, abstractmethod
from MusicPlayer import MusicPlayer, SpotifyMusicPlayer
from VideoPlayer import VideoPlayer, YouTubeVideoPlayer
class PlayerFactory(ABC):
    @abstractmethod
    def create_music_player(self) -> MusicPlayer:
        pass

    @abstractmethod
    def create_video_player(self) -> VideoPlayer:
        pass

class MusicOrVideoPlayerFactory(PlayerFactory):
    def create_music_player(self) -> MusicPlayer:
        return SpotifyMusicPlayer()

    def create_video_player(self) -> VideoPlayer:
        return YouTubeVideoPlayer()