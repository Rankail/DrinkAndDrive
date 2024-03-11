from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from src.game import Event, EventWidget
from src.EventMaker import read_events, get_random_events_and_intervalls

if __name__ == "__main__":
    app = QApplication([])

    mainWidget = QWidget()
    baseLayout = QVBoxLayout(mainWidget)
    baseLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    players = [
        "Yoshi",
        "Samuel",
        "Marvin"
    ]

    eventHistory: list[EventWidget] = []
    historySize: int = 3

    def removeOldestEvent():
        oldest = eventHistory.pop()
        baseLayout.removeWidget(oldest.layout)
        for i, ew in enumerate(eventHistory):
            importance = (i + 1) / historySize
            ew.updateImportance(importance)

    def addEvent(event: Event):
        if len(eventHistory) >= historySize:
            removeOldestEvent()

        eventHistory.insert(0, event.getWidget())

    events: list[Event] = []
    eventStrs = read_events()
    for eventStr in eventStrs:
        print(eventStr)

    timespan = int(input("Dauer (in min): "))
    eventCount = int(input("Amount of events: "))

    get_random_events_and_intervalls(events, eventCount, timespan)

    mainWidget.show()
    app.exec()