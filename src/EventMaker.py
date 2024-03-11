# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:27:02 2024

@author: Marvin
"""

import os
import random

def read_events():
    events = []
    file_path = os.path.join("./Events/", "Events.txt")
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            events = file.read().split('\n\n')  
    else:
        print("'Events.txt'nicht gefunden.")
    return events

def choose_random_events(events,count_random_events):
    random_events= []
    for i in range(0,count_random_events):
        random_events.append(events[random.randint(0, len(events)-1)])        
    return random_events

def choose_random_intevalls(count_random_events,timespan):
    random_timestamp=random.sample(range(0,timespan), count_random_events)
    random_timestamp.sort()
    start = 0
    for index,timestamp in enumerate(random_timestamp):
        random_timestamp[index] = timestamp-start
        start = timestamp 
    return random_timestamp
    
def get_random_events_and_intervalls(events,count_random_events,timespan):
    random_events = choose_random_events(events, count_random_events)
    random_timestamp = choose_random_intevalls(count_random_events, timespan)
    return (random_events,random_timestamp)

print(choose_random_intevalls(10, 40))
print(sum(choose_random_intevalls(10, 40)))