import time
import random
from PyQt5.QtWidgets import QApplication, QtLayout, QLabel, QStackedLayout, QFormLayout, QVBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])

baseLayout = QStackedLayout()

players = [
    "Yoshi",
    "Samuel",
    "Marvin"
]

class Event:
    text: list[str] = None

    def __init__(self):
        self.text = []

    def getWidget(self, importance: float) -> QtLayout:
        pass

class Duel(Event):

    def __init__(self, text: str):
        self.text = text.splitlines()

    def getWidget(self, importance: float) -> QtLayout:
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        playerSet = players.copy()
        for line in self.text:
            playerCount = line.count("\{\}")
            selected = random.sample(playerSet, playerCount)
            for p in selected:
                playerSet.remove(p)
                
            label = QLabel(line.format(*selected))
            color = importance * 255
            label.setStyleSheet(f"font: {30 * importance}pt; color: rgb({color}, {color}, {color}, 255);")
            layout.addChildWidget(label)

        return layout

class Game(Event):
    def getWidget(self, importance: float) -> QtLayout:
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        for line in self.text:
            label = QLabel(line)
            color = importance * 255
            label.setStyleSheet(f"font: {30 * importance}pt; color: rgb({color}, {color}, {color}, 255);")
            layout.addChildWidget(label)

        return layout

app.exec()