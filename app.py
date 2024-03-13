from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from src.events import EventType, EventContainer, EventEmitter
from src.randomUtils import read_events
from src.soundUtils import SoundChooser

class NoFriendsError(Exception):
    pass

if __name__ == "__main__":
    app = QApplication([])

    window = QMainWindow()
    window.setWindowTitle("Drink & Drive")

    mainWidget = QWidget()

    players = [
        "Joshi",
        "Samuel",
        "Marvin",
        "Jan",
        "Leon"
    ]

    if len(players) < 2:
        raise NoFriendsError("You have too few friends to play this game")

    events = EventContainer(players, 3)

    mainWidget.setLayout(events.layout)
    window.setCentralWidget(mainWidget)

    sounds = SoundChooser()
    for id, eventStr in enumerate(read_events()):
        eventType = EventType(id, eventStr, sounds.getRandom())
        events.addEventType(eventType)

    if len(events.eventTypes) == 0:
        raise ValueError("Need at least 1 event")

    timespan = int(input("Duration (in min): "))
    eventCount = int(input("Amount of events: "))

    if timespan < eventCount:
        raise ValueError("Cant play more than 1 event/min")
    
    if timespan == 0:
        raise ValueError("Timespan must be greater than 0")
    
    if timespan == 0:
        raise ValueError("Amount of events should be greater than 0")

    worker = EventEmitter(eventSize=len(events.eventTypes), eventCount=eventCount, timespan=timespan)

    worker.eventReady.connect(events.callEvent)
    worker.finished.connect(app.quit)

    worker.start()

    window.showFullScreen()
    
    app.exec()