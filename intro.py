import os
from terminaltexteffects.effects.effect_blackhole import Blackhole # Cool intro text effect
import time
import type
import music
from rich.progress import Progress



def cool_title(): # This is the intro text effect
    os.system('cls||clear') # Clear the console for any system including stupid macs
    time.sleep(0.5)
    effect = Blackhole(" ██████╗ ██╗   ██╗██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗\n██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝\n██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  \n██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  \n╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗\n ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝\n======================================================================\n\n© 2025 BitRealm Studios. All right reserved.\nCreated by Benjamin Robertson")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    print("")


def loading():
    os.system('cls||clear') 
    with Progress() as progress:
        task1 = progress.add_task("[red]Downloading Catagories...", total=1000)
        task2 = progress.add_task("[green]Processing Questions...", total=1000)
        task3 = progress.add_task("[cyan]Preparing Quiz...", total=1000)

        while not progress.finished:
            progress.update(task1, advance=2)
            progress.update(task2, advance=1.8)
            progress.update(task3, advance=1.65)
            time.sleep(0.02)
    time.sleep(1)
    type.type("\n\u001b[33mLoading complete!")
    time.sleep(0.5)
    type.type("\nWecome to the quiz!")
    time.sleep(1)
    print("\u001b[34m\u001b[0m")
    os.system('cls||clear')



def intro():
    music.loading_music()
    loading()
    cool_title()
    player_name = type.typewriter_input("Enter your name: ") 
    type.type(f"Welcome to the greatest quiz in the world \u001b[34m\u001b[0m{player_name}")
    time.sleep(2)
    os.system('cls||clear')
    return player_name