# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:27:02 2024

@author: Marvin
"""

import os

def read_events():
    duels = []
    games = []
    file_path = os.path.join("./Events/", "Duels.txt")
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            duels = file.read().split('\n\n')   
    else:
        print("'Duels.txt'nicht gefunden.")
    file_path = os.path.join("./Events/", "Games.txt")
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            games = file.read().split('\n\n')   
    else:
        print("'Games.txt'nicht gefunden.")
    return[games,duels];

def choose_random_events(count_events,,timespan):
    