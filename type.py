import time
import sys
from terminaltexteffects.effects.effect_slide import Slide

def type(text, delay=0.03):
    for char in text:
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

def typewriter_input(prompt_text: str) -> str:
    effect = Slide(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    # Makes the slide effect for input happen frame by frame
    with effect.terminal_output(end_symbol=" \u001b[31;1m") as terminal:
        for frame in effect:
            terminal.print(frame)
    # Capture user input
    return input().strip()