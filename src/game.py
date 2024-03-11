import time
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLayout, QLabel, QStackedLayout, QFormLayout, QVBoxLayout
from PyQt5.QtCore import Qt

from .EventMaker import read_events, get_random_events_and_intervalls

class EventWidget:
    layout: QVBoxLayout = None

    def __init__(self, text: list[str]):
        self.createLabels(text)

    def createLabels(self, text: list[str]):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        playerSet = players.copy()
        for line in text:
            playerCount = line.count("{}")
            selected = random.sample(playerSet, playerCount)
            for p in selected:
                playerSet.remove(p)

        self.qtLayout = layout
        self.updateImportance(1.0)

        return layout

    def updateImportance(self, importance: float):
        for child in self.layout.children():
            child: QLabel = child
            child.setStyleSheet(f"font: {30 * importance}pt; color: rgb(0, 0, 0, {importance * 255});")


class Event:
    text: list[str] = None

    def __init__(self, text: str):
        self.text = text.splitlines()

    def getWidget(self, importance: float) -> EventWidget:
        return EventWidget(self.text)