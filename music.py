from pygame import mixer # Music engine

def loading_music():
    mixer.init()
    mixer.music.load('loading.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play(loops = -1) 


def main_music():
    mixer.init()
    mixer.music.load('main_music.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play(loops = -1) 