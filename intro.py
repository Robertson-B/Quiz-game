import os
from terminaltexteffects.effects.effect_blackhole import Blackhole # Cool intro text effect
import time
import sys
import type
import music



def cool_title(): # This is the intro text effect
    os.system('cls||clear') # Clear the console for any system including stupid macs
    effect = Blackhole(" ██████╗ ██╗   ██╗██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗\n██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝\n██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  \n██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  \n╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗\n ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝\n======================================================================\n\n© 2025 BitRealm Studios. All right reserved.\nCreated by Benjamin Robertson")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    print("")


def loading():
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
        if i == 51 or i == 92 or i == 26 or i == 87:
            # Gives the loading percentage a stutter to be more realistic... and annoying...
            time.sleep(0.4)
        if i == 99:
            # Pauses on 100% just like in real life
            time.sleep(1)
    print("")
    
def intro():
    music.loading_music()
    loading()
    cool_title()
    name = type.typewriter_input("Enter your name: ") 
    type(f"Welcome to the greatest quiz in the world \u001b[34m\u001b[0m{name}")
    time.sleep(2)
    os.system('cls||clear')