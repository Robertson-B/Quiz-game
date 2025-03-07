import os
from terminaltexteffects.effects.effect_blackhole import Blackhole # Cool intro text effect
from terminaltexteffects.effects.effect_slide import Slide
import time
import sys

def type(text):
    for char in text:
        time.sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

def cool_title(): # This is the intro text effect
    os.system('cls||clear') # Clear the console for any system including stupid macs
    effect = Blackhole(" ██████╗ ██╗   ██╗██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗\n██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝\n██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  \n██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  \n╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗\n ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝\n======================================================================\n\n© 2024 BitRealm Studios. All right reserved.\nCreated by Benjamin Robertson")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    print("")
    
def typewriter_input(prompt_text: str) -> str:
    effect = Slide(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    # Makes the slide effect for input happen frame by frame
    with effect.terminal_output(end_symbol=" \u001b[31;1m") as terminal:
        for frame in effect:
            terminal.print(frame)
    # Capture user input
    return input().lower().strip()

def loading():
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
        if i == 51 or i == 92 or i == 26 or i == 87:
            # Gives the loading percentage a stutter to be more realistic... and annoying...
            time.sleep(0.4)
        if i == 99:
            # Pauses on 99% just like in real life
            time.sleep(1)
    print("")
    
def intro():
    loading()
    cool_title()
    name = typewriter_input("Enter your name: ") 
    type(f"Welcome to the greatest quiz in the world \u001b[34m\u001b[0m{name}")
    time.sleep(2)
    os.system('cls||clear')