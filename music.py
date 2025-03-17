from pygame import mixer # Music engine

def loading_music():
    mixer.init()
    mixer.music.load('loading.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play(loops = -1) 


def quiz_theme():
    mixer.init()
    mixer.music.load('quiz_theme.mp3')
    mixer.music.set_volume(1)
    mixer.music.play(loops = 1) 
    
def stop_music():
    mixer.init()
    mixer.music.stop()

def correct_answer():
    mixer.init()
    mixer.music.load('correct_answer.mp3')
    mixer.music.set_volume(1)
    mixer.music.play(loops = 1)

def wrong_answer():
    mixer.init()
    mixer.music.load('wrong_answer.mp3')
    mixer.music.set_volume(1)
    mixer.music.play(loops = 1)