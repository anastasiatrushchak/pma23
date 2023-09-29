from abc import ABC, abstractmethod


# from abc import ABC, abstractmethod
# class MusicPlayer(ABC):
#     @abstractmethod
#     def open_music(self):
#         pass
#
#     @abstractmethod
#     def play_music(self):
#         pass
#
#     @abstractmethod
#     def close_music(self):
#         pass
#
# class VideoPlayer(ABC):
#     @abstractmethod
#     def open_video(self):
#         pass
#
#     @abstractmethod
#     def play_video(self):
#         pass
#
#     @abstractmethod
#     def close_video(self):
#         pass
# class PlayerFactory(ABC):
#     @abstractmethod
#     def create_music_player(self) -> MusicPlayer:
#         pass
#
#     @abstractmethod
#     def create_video_player(self) -> VideoPlayer:
#         pass
#
# class MusicOrVideoPlayerFactory(PlayerFactory):
#     def create_music_player(self) -> MusicPlayer:
#         return SpotifyMusicPlayer()
#
#     def create_video_player(self) -> VideoPlayer:
#         return YouTubeVideoPlayer()
#
# class SpotifyMusicPlayer(MusicPlayer):
#     def open_music(self):
#         print("Open Spotify")
#     def play_music(self):
#         print("Play music in Spotify")
#     def close_music(self):
#         print("Close Spotify")
#
# class YouTubeVideoPlayer(VideoPlayer):
#     def open_video(self):
#         print("Open YouTube")
#     def play_video(self):
#         print("Play video in YouTube")
#     def close_video(self):
#         print("Close YouTube")
#
#
# factory = MusicOrVideoPlayerFactory()
# music_player = factory.create_music_player()
# video_player = factory.create_video_player()
#
# music_player.open_music()
# music_player.play_music()
# music_player.close_music()
# print('\n')
# video_player.open_video()
# video_player.play_video()
# video_player.close_video()
class Recipe(ABC):
    def template_method(self):
        self.step1()
        self.step2()
        self.step3()

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass


class Omelet(Recipe):
    def step1(self):
        print("1. Beat the eggs while melting the butter on pan")

    def step2(self):
        print("2. Add the beaten eggs to the pan and fill it with cheese or sausages")

    def step3(self):
        print("3. Fold the omelette in half and serve it on the plate")

    def __init__(self):
        self.template_method()


class Sandwich(Recipe):
    def step1(self):
        print("1. Assemble your sandwich by layering deli meat,"
              " cheese, and any desired veggies between two slices of bread.")

    def step2(self):
        print("2. Add condiments like mayo or mustard if you like")

    def step3(self):
        print("3. Serve and enjoy")




print("Omlet recipe:")
a = Omelet()
a.template_method()

print("\nSandwich recipe:")
b = Sandwich()
b.template_method()