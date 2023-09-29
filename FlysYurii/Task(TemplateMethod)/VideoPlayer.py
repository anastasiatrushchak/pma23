from abc import ABC, abstractmethod
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

class YouTubeVideoPlayer(VideoPlayer):
    def open_video(self):
        print("Open YouTube")
    def play_video(self):
        print("Play video in YouTube")
    def close_video(self):
        print("Close YouTube")