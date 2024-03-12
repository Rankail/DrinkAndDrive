import time
import random
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QThread, pyqtSignal

from .randomUtils import get_random_events_and_intervalls
from .soundUtils import play_sound

class EventEmitter(QThread):
    finished = pyqtSignal()
    eventReady = pyqtSignal(int)

    eventSize: int = None
    eventCount: int = None
    timespan: int = None

    def __init__(self, parent=None, eventSize: int = None, eventCount: int = 10, timespan: int = 60):
        QThread.__init__(self, parent)
        self.eventSize = eventSize
        self.eventCount = eventCount
        self.timespan = timespan

    def run(self):
        eventTiming = get_random_events_and_intervalls(range(0, self.eventSize), self.eventCount, self.timespan)
        for eventIdx, waitTime in eventTiming:
            time.sleep(60.0 * waitTime)
            self.eventReady.emit(eventIdx)
        time.sleep(30.0)
        self.finished.emit()

class EventType:
    id: int = None
    text: str = None
    sound: str = None

    def __init__(self, id: int, text: str, sound: str):
        self.id = id
        self.text = text
        self.sound = sound

    def getText(self, players: list[str]) -> str:
        playerCount = self.text.count("{}")
        selected = random.sample(players, playerCount)
        return self.text.format(*selected)
    

class EventContainer:
    labels: list[QLabel] = None
    eventTypes: list[EventType] = None
    layout: QVBoxLayout = None
    players: list[str] = None

    def __init__(self, players: list[str], size: int):
        self.labels = []
        self.eventTypes = []
        self.players = players

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        for i in range(size):
            label = QLabel("Hello there")
            label.setText("Hello there")
            importance = (i+1) / size
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setFixedHeight(200)
            label.setStyleSheet(f"font: {40 * importance}pt; font-weight: semi-bold; color: rgba(0, 0, 0, {importance * 255});")

            self.labels.append(label)
            self.layout.addWidget(label)

    def addEventType(self, eventType: EventType):
        self.eventTypes.append(eventType)

    def callEvent(self, eventId: int):
        event = next(et for et in self.eventTypes if et.id == eventId)

        for i in range(len(self.labels)-1):
            self.labels[i].setText(self.labels[i+1].text())

        self.labels[len(self.labels)-1].setText(event.getText(self.players))

        self.layout.update()

        play_sound(event.sound)