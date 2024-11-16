# -*- coding: utf-8 -*-
from app.Pixmap import load
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGridLayout,
    QGroupBox
)

class StartStopUI(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Group Box
        groupbox = QGroupBox("Start/Stop")

        # Configure group layout
        grouplayout = QGridLayout()
        grouplayout.rowStretch(1)
        grouplayout.columnStretch(1)
        groupbox.setLayout(grouplayout)

        # Configure widget layout
        widgetlayout = QVBoxLayout()
        widgetlayout.addWidget(groupbox)
        self.setLayout(widgetlayout)

        # relay button
        self.bt_start = QPushButton()
        self.bt_start.setText('Off')
        self.bt_start.setIcon(load('OFF_BUTTON'))
        self.bt_start.pressed.connect(self.on_pressed)
        grouplayout.addWidget(self.bt_start, 0, 0)

    def on_pressed(self) -> None:
        if self.bt_start.text() == 'Off' :
            self.bt_start.setText('On')
            self.bt_start.setIcon(load('ON_BUTTON'))
        else:
            self.bt_start.setText('Off')
            self.bt_start.setIcon(load('OFF_BUTTON'))
