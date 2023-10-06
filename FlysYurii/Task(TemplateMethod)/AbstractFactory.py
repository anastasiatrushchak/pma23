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

class VideoPlayer(ABC):
    @abstractmethod
    def open_video(self):
        pass

    @abstractmethod
    def play_video(self):
        pass

    @abstractmethod
    def close_video(self):
        pass
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

class SpotifyMusicPlayer(MusicPlayer):
    def open_music(self):
        print("Open Spotify")
    def play_music(self):
        print("Play music in Spotify")
    def close_music(self):
        print("Close Spotify")

class YouTubeVideoPlayer(VideoPlayer):
    def open_video(self):
        print("Open YouTube")
    def play_video(self):
        print("Play video in YouTube")
    def close_video(self):
        print("Close YouTube")


factory = MusicOrVideoPlayerFactory()
music_player = factory.create_music_player()
video_player = factory.create_video_player()

music_player.open_music()
music_player.play_music()
music_player.close_music()
print('\n')
video_player.open_video()
video_player.play_video()
video_player.close_video()
