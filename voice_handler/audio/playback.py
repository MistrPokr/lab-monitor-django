from pydub import AudioSegment
from pydub.playback import play


def play_audio(file_path):
    sound = AudioSegment.from_mp3(file_path)
    play(sound)
