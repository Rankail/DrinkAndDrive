import pygame
import os
import random

def read_sounds():
    sounds = []
    if os.path.isdir("./Sounds/"):
        sounds = os.listdir("./Sounds/")

    if len(sounds) == 0:
        raise LookupError("No sounds found")
        
    return sounds

def play_sound(sound_file):
    path = "./Sounds/" + sound_file
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    
def choose_random_sounds(sounds,count_random_events):
    random_sounds= []
    for i in range(0,count_random_events):
        random_sounds.append(sounds[random.randint(0, len(sounds)-1)])        
    return random_sounds

def get_random_sounds(count_random_events):
    sounds = read_sounds()
    random_sounds = choose_random_sounds(sounds, count_random_events)
    return random_sounds

class SoundChooser:
    sounds: list[str] = None
    bag: list[str] = None

    def __init__(self):
        self.sounds = read_sounds()
        self.bag = []

    def getRandom(self):
        if len(self.bag) == 0:
            self.bag.extend(self.sounds)
            random.shuffle(self.bag)

        return self.bag.pop()