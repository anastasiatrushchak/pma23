from PlayerFactory import MusicOrVideoPlayerFactory

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
