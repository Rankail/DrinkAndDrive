# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:24:35 2024

@author: Marvin
"""
import pygame
import os
import random
import time

def read_sounds():
    sounds = []
    if os.path.isdir("../Sounds/"):
        sounds = os.listdir("../Sounds/")
        
    return sounds

def play_sound(sound_file):
    path = "../Sounds/" + sound_file
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    
def get_random_sounds(sounds,count_random_events):
    random_sounds= []
    for i in range(0,count_random_events):
        random_sounds.append(sounds[random.randint(0, len(sounds)-1)])        
    return random_sounds
